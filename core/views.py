from django.contrib import auth
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView

from .forms import AForm, SignUpBusinessForm, SignUpClientForm
from .models import Business, TreatmentType, User, Client
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
import datetime


# @login_required
class BusinessList(ListView):
    template_name = 'core/business.html'
    queryset = Business.objects.all()


class BusinessDetail(DetailView):
    template_name = 'core/busines_detail.html'
    queryset = Business.objects.all()


def treatments_page(request, pk):
    dt = timezone.now()
    dates = []
    for x in range(30):
        a = dt + datetime.timedelta(days=x)
        # if a.isoweekday() in [1,2,3]:
        dates.append(a)
    l = [x.date().strftime('%d/%m/%Y') for x in dates]
    expChoices = [(x, x) for x in l]
    treatments_obj = Business.objects.get(id=pk).treatments.all()
    daysWork_obj = Business.objects.get(id=pk).days.all()
    context = {'form': AForm(treatments_obj=treatments_obj, expChoices=expChoices)}
    return render(request, 'core/busines_detail.html', context)


def search(request):
    return render(request, 'core/search.html')

class NoneLoginPermitted(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            raise Http404
        return super().dispatch(request, *args, **kwargs)

class SignUpBusinessView(NoneLoginPermitted,FormView):
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

class AppointmentView():




def logout(request):
    auth.logout(request)
    return render(request, 'core/search.html')


def admin_page(request):
    if not request.user.is_authenticated():
        return redirect('login')
    return render(request, 'core/search.html')
