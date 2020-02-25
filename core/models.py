from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class TreatmentType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class WorkDay(models.Model):
    day = models.CharField(default="" ,max_length=15)

    def __str__(self):
        return self.day


class Business(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='business',default=None )
    phone = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField()
    treatments = models.ManyToManyField(TreatmentType, blank=True)
    days = models.ManyToManyField(WorkDay, blank=True)
    location = models.CharField(max_length=20)
    start_hour = models.TimeField(default="08:00")
    end_hour = models.TimeField(default="16:00")

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('core:business-detail',kwargs={'pk':self.pk})


class Client(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='client')
    location = models.CharField(max_length=200)
    phone = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.user.username

class Appointment(models.Model):
    business = models.ForeignKey(Business,on_delete=models.CASCADE,related_name='appointment')
    client = models.ForeignKey(Client,on_delete=models.CASCADE,related_name='appointment')
    treatment = models.ForeignKey(TreatmentType,on_delete=models.CASCADE)
    day = models.DateTimeField(null=True)
    time = models.TimeField(default="08:00")


    def __str__(self):
        return self.business.user.name , self.client.user.name
