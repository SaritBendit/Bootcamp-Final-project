# Generated by Django 3.0.3 on 2020-02-20 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_workday_hours'),
    ]

    operations = [
        migrations.DeleteModel(
            name='WorkHours',
        ),
    ]