# Generated by Django 3.0.3 on 2020-02-24 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20200224_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
