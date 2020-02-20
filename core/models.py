from django.db import models


class TreatmentType(models.Model):
    name = models.CharField(max_length=200)
    # time = models.IntegerField(default=10)

    def __str__(self):
        return self.name

# class appoitment(models.Model):
#     business
#     date = models.DateTimeField()


class WorkDay(models.Model):
    day =models.CharField(default="" ,max_length=15)

    def __str__(self):
        return self.day
# class Customer(models.Model):
#     email = models.ForeignKey(on_delete=models.CASCADE)
#     full_name = models.CharField(max_length=200)
#     phone = models.IntegerField(default=0)
#
#     def __str__(self):
#         return f"{self.full_name}"

class Business(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField()
    treatments = models.ManyToManyField(TreatmentType, blank=True)
    days = models.ManyToManyField(WorkDay, blank=True)
    start_hour = models.TimeField(default="08:00")
    end_hour = models.TimeField(default="16:00")


    # full_name = models.CharField(max_length=200)
    # location = models.CharField(max_length=200)
    # facebook_link = models.CharField(max_length=200)

    def __str__(self):
        return self.name




