import datetime

from django import forms
from django.utils import timezone
from phone_field import PhoneField

from core.models import TreatmentType, WorkDay, Business, Client


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


class SignUpBusinessForm(forms.ModelForm):
    username = forms.CharField(
        label='User name',
        max_length=200, widget=forms.TextInput(attrs={'class': 'from-control'}))
    first_name = forms.CharField(label='first_name',max_length=100)
    email = forms.EmailField(label='Email', max_length=200)
    password = forms.CharField(label='Password', max_length=200, widget=forms.PasswordInput)

    class Meta:
        model= Business
        fields = ['username','first_name','email','password','phone','location','description','treatments','days','start_hour','end_hour']
        widgets = {
            'start_hour' : forms.Select(
                attrs={'class': 'from-control'},
                choices=((f'{x}:00', f'{x}:00') for x in range(6, 24))),
            'end_hour': forms.Select(choices=((f'{x}:00', f'{x}:00') for x in range(6, 24)))
        }


class SignUpClientForm(forms.ModelForm):
    username = forms.CharField(
        label='User name',
        max_length=200, widget=forms.TextInput(attrs={'class': 'from-control'}))
    first_name = forms.CharField(max_length=100)
    email = forms.EmailField(label='Email', max_length=200)
    password = forms.CharField(label='Password', max_length=200, widget=forms.PasswordInput)

    class Meta:
        model= Client
        fields = ['username','first_name','email','password','phone','location']
