# Generated by Django 4.1.1 on 2023-04-17 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0014_booking_booked_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='booked_user',
            new_name='first_name',
        ),
    ]