from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin
from django.http import Http404
from django.views.generic import ListView, DetailView, FormView
from .forms import AForm, SignUpBusinessForm, SignUpClientForm, AppointmentForm
from .models import Business, TreatmentType, User, Client, Appointment
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
import datetime


class BusinessList(ListView):
    template_name = 'core/business.html'
    model = Business
    def get_queryset(self):
        qs = super().get_queryset()
        treatment = self.request.GET.get('treatment')
        fname = self.request.GET.get('fname')
        bname = self.request.GET.get('bname')
        location = self.request.GET.get('location')
        if treatment:
            qs = qs.filter(treatments__name__icontains=treatment)
        if fname:
            qs = qs.filter(user__first_name__icontains=fname)
        if bname:
            qs = qs.filter(user__name__icontains=bname)
        if location:
            qs = qs.filter(location__icontains=location)

        return qs


class BusinessDetail(DetailView):
    template_name = 'core/busines_detail.html'
    model = Business
    # queryset = Business.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['apo_list'] = self.get_object().appointments.all()
        return context



def search(request):
    return render(request, 'core/search.html')


class NoneLoginPermitted(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            raise Http404
        return super().dispatch(request, *args, **kwargs)


class SignUpBusinessView(NoneLoginPermitted, FormView):
    template_name = 'registration/signup_business.html'
    form_class = SignUpBusinessForm
    success_url = reverse_lazy('core:search')

    def form_valid(self, form):
        data = form.cleaned_data
        user = User.objects.create(
            username=data['username'],
            first_name=data['first_name'],
            email=data['email'],
        )

        user.set_password(data['password'])
        user.save()
        # treatments_qs = TreatmentType.objects.filter(name__contains=data['treatments'])
        print(data['treatments'])
        business = Business.objects.create(
            user=user,
            phone=data['phone'],
            location=data['location'],
            description=data['description'],
            start_hour=data['start_hour'],
            end_hour=data['end_hour']
        )
        business.treatments.set(data['treatments']),
        business.days.set(data['days']),

        business.save()
        login(self.request, user)
        return super(SignUpBusinessView, self).form_valid(form)


class SignUpClientView(NoneLoginPermitted, FormView):
    template_name = 'registration/signup_client.html'
    form_class = SignUpClientForm
    success_url = reverse_lazy('core:search')

    def form_valid(self, form):
        data = form.cleaned_data
        user = User.objects.create(
            username=data['username'],
            first_name=data['first_name'],
            email=data['email'],
        )
        user.set_password(data['password'])
        user.save()
        Client.objects.create(
            user=user,
            phone=data['phone'],
            location=data['location']
        )
        login(self.request, user)
        return super(SignUpClientView, self).form_valid(form)


class AppointmentView(LoginRequiredMixin, FormView):
    template_name = 'core/appointment.html'
    form_class = AppointmentForm
    success_url = reverse_lazy('core:search')

    def hours(self):
        bid = self.kwargs['business_id']
        b = get_object_or_404(Business, pk=bid)
        appointments_for_business = b.appointments.all()
        return [(
            a.day,
            a.time.strftime("%H:%M"),
        ) for a in appointments_for_business]


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        dt = timezone.now()
        dates = []
        bid = self.kwargs['business_id']
        b = get_object_or_404(Business, pk=bid)

        daysWork_obj = Business.objects.get(id=bid).days.all()
        day_list = [x.day for x in daysWork_obj]
        for x in range(30):
            a = dt + datetime.timedelta(days=x)
            if a.date().strftime('%A') in day_list:
                dates.append(a)
        l = [x.date() for x in dates ]
        expChoices = [(x, x.strftime('%d/%m/%Y %A')) for x in l]
        treatments_obj = Business.objects.get(id=bid).treatments.all()

        kwargs['treatments_obj'] = treatments_obj
        kwargs['expChoices'] = expChoices

        start_hour = Business.objects.get(id=bid).start_hour.hour
        end_hour = Business.objects.get(id=bid).end_hour.hour
        hours = []
        for hour in range(start_hour , end_hour+1):
            hours.append((hour,datetime.time(hour,00).strftime("%H:%M")))
        kwargs['hours'] =hours
        return kwargs
    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.is_authenticated and Client.objects.filter(user=self.request.user).exists():
    #         return super().dispatch(request, *args, **kwargs)
    #     return redirect(reverse('core:search'))

    def form_valid(self, form):
        data = form.cleaned_data
        business_id = self.kwargs['business_id']
        treat_id = self.kwargs['treat_id']
        treatment_id = data['treatments']
        user = self.request.user
        date_input =  data['dates']
        day = datetime.datetime.strptime(date_input, '%Y-%m-%d').date()
        time =  data['hours']
        a = Appointment.objects.create(
            business_id=business_id,
            client=user.client,
            treatment_id=treatment_id,
            day=day,
            time=datetime.time(int(time),00).strftime("%H:%M")

        )
        return super(AppointmentView, self).form_valid(form)


