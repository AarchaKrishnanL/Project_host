# Generated by Django 4.1.1 on 2022-11-21 16:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home_app', '0002_remove_booking_p_name_booking_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='details_user',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
