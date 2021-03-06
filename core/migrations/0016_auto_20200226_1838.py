# Generated by Django 3.0.3 on 2020-02-26 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20200225_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='business',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='core.Business'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='core.Client'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='day',
            field=models.DateField(default="2020-02-20"),
            preserve_default=False,
        ),
    ]
