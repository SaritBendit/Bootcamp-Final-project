from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render

from .forms import AForm, SignUpForm
from .models import Business, TreatmentType
from django.template import loader, RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
import datetime


def business_page(request):
    business = Business.objects.all()
    context = {'obj_list': business}
    return render(request, 'core/business.html', context)


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
    return render(request, 'core/treatments.html', context)


# @login_required
def search(request):
    return render(request, 'core/search.html')


def signup(request):
    print(request.user.username)
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create(
                username=data['username'],
                email=data['email']
            )
            user.set_password(data['password'])
            user.save()
            login(request, user)
    else:
        form = SignUpForm
    return render(request, 'registration/signup.html', {'form': form})
