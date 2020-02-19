from django.shortcuts import render

from .forms import AForm
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
        dates.append(dt + datetime.timedelta(days=x))
    l = [x.date().strftime('%d/%m/%Y') for x in dates]
    expChoices = [(x, x) for x in l]
    # experienceYears = Field(max_length=2, choices=expChoices, default=0, blank=True)
    treatments = TreatmentType.objects.filter(business__id=pk)
    context = {'obj_list': treatments, 'dates': l, 'form': AForm}
    return render(request, 'core/treatments.html', context)
