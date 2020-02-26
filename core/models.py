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
    daychoices = (
        (7, 'Sunday'),
        (1, 'Monday'),
        (2, 'Tuesday'),
        (3, 'Wednesday'),
        (4, 'Thursday'),
        (5, 'Friday'),
        (6, 'Saturday'),
    )
    day = models.CharField(default="" ,max_length=15)
    # day_int = models.IntegerField(blank=True, null=True, choices=daychoices)

    def __str__(self):
        return self.day
        # return self.get_day_int_display()


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
        return reverse('core:business_detail',kwargs={'pk':self.pk})


class Client(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='client')
    location = models.CharField(max_length=200)
    phone = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.user.username

class Appointment(models.Model):
    business = models.ForeignKey(Business,on_delete=models.CASCADE,related_name='appointments')
    client = models.ForeignKey(Client,on_delete=models.CASCADE,related_name='appointments')
    treatment = models.ForeignKey(TreatmentType,on_delete=models.CASCADE)
    day = models.DateField()
    time = models.TimeField(default="08:00")

    def get_absolute_url(self):
        return reverse('core:appointment-form',kwargs={'pk':self.pk})

    # def __str__(self):
    #     return self.business.user.username , self.client.user.username
