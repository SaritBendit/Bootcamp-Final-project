import datetime

from django import forms
from django.utils import timezone

from core.models import TreatmentType


class AForm(forms.Form):
    # experienceYears = Field(max_length=2, choices=expChoices, default=0, blank=True)
    treatments = forms.ChoiceField(label='treatments', widget=forms.RadioSelect)
    dates = forms.ChoiceField(label='choose date')
    hours = forms.ChoiceField(label='choose hour')

    def __init__(self, treatments_obj, expChoices, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['treatments'].choices = ((t.id, t.name) for t in treatments_obj)
        self.fields['dates'].choices = expChoices
        self.fields['hours'].choices = expChoices


class SignUpForm(forms.Form):
    username = forms.CharField(
        label='User name',
        max_length=200, widget=forms.TextInput(attrs={'class': 'from-control'}))
    email = forms.EmailField(label='Email', max_length=200)
    password = forms.CharField(label='Password', max_length=200, widget=forms.PasswordInput)
