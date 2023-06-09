# Generated by Django 4.1.1 on 2023-05-15 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0025_alter_patients_photo1_alter_patients_photo2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='allergies',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='patients',
            name='beverages',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='patients',
            name='blood_group',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='patients',
            name='claustrophobic',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='patients',
            name='gender',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='patients',
            name='health_issues',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='patients',
            name='pain',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='patients',
            name='smoker',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='patients',
            name='supplements',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
