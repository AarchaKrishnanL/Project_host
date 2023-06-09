# Generated by Django 4.1.1 on 2023-04-12 15:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home_app', '0008_booking_patient_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='patient_name',
        ),
        migrations.AddField(
            model_name='booking',
            name='booked_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booked_appointments', to=settings.AUTH_USER_MODEL),
        ),
    ]
