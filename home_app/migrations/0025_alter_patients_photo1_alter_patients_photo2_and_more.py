# Generated by Django 4.1.1 on 2023-05-15 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0024_alter_patients_photo1_alter_patients_photo2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='photo1',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
        migrations.AlterField(
            model_name='patients',
            name='photo2',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
        migrations.AlterField(
            model_name='patients',
            name='photo3',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
    ]
