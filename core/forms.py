import datetime

from django import forms
from django.utils import timezone


class AForm(forms.Form):
    dt = timezone.now()
    dates = []
    for x in range(30):
        dates.append(dt + datetime.timedelta(days=x))
    l = [x.date().strftime('%d/%m/%Y') for x in dates]
    expChoices = [(x, x) for x in l]
    dates = forms.ChoiceField(label='choose date', choices=expChoices)
    hours = []
    for x in range(24):
        hours.append(str(x) + ":00")
    expChoices = [(x, x) for x in hours]
    hoursF = forms.ChoiceField(label='choose hour', choices=expChoices)
