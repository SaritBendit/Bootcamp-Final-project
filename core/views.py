from django.contrib import auth
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView

from .forms import AForm, SignUpBusinessForm, SignUpClientForm
from .models import Business, TreatmentType, User
from django.template import loader, RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
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


class SignUpBusinessView(FormView):
    template_name = 'registration/signup_business.html'
    form_class = SignUpBusinessForm
    success_url = reverse('core:search')

    def form_valid(self, form):
            data = form.cleaned_data
            user = User.objects.create(
                username=data['username'],
                first_name=data['first_name'],
                email=data['email'],
            )
            user.set_password(data['password'])
            user.save()
            login(self.request, user)
            return super(SignUpBusinessView, self).form_valid(form)


class SignUpClientView(FormView):
    template_name = 'registration/signup_client.html'
    form_class = SignUpClientForm
    success_url = 'core:search'

    def form_valid(self, form):
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create(
                username=data['username'],
                first_name=data['first_name'],
                email=data['email'],
            )
            user.set_password(data['password'])
            user.save()
            form.save()
            login(self.request, user)
            return super(SignUpClientView, self).form_valid(form)

def logout(request):
    auth.logout(request)
    return render(request, 'core/search.html')

def admin_page(request):
    if not request.user.is_authenticated():
        return redirect('login')
    return render(request, 'core/search.html')
