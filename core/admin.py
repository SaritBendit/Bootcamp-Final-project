from django.contrib import admin

from . import models

admin.site.register(models.Business)
admin.site.register(models.TreatmentType)
admin.site.register(models.WorkDay)
admin.site.register(models.Client)
admin.site.register(models.Appointment)