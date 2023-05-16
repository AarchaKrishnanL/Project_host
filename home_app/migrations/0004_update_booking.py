# Generated by Django 4.1.1 on 2022-11-22 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0003_details_user_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Update_Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateField()),
                ('booked_on', models.DateField(auto_now=True)),
                ('description', models.TextField(blank=True)),
                ('doc_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_app.doctors')),
                ('time_slot', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home_app.time_slot')),
            ],
        ),
    ]