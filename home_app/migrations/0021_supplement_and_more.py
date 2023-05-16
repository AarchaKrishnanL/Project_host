# Generated by Django 4.1.1 on 2023-05-15 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0020_remove_cart_product_remove_cart_user_delete_mymodel_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='patients',
            old_name='allergies',
            new_name='past_medical_history',
        ),
        migrations.RemoveField(
            model_name='patients',
            name='beverages',
        ),
        migrations.RemoveField(
            model_name='patients',
            name='claustrophobic',
        ),
        migrations.RemoveField(
            model_name='patients',
            name='health_issues',
        ),
        migrations.RemoveField(
            model_name='patients',
            name='medications',
        ),
        migrations.RemoveField(
            model_name='patients',
            name='pain',
        ),
        migrations.RemoveField(
            model_name='patients',
            name='photo1',
        ),
        migrations.RemoveField(
            model_name='patients',
            name='photo2',
        ),
        migrations.RemoveField(
            model_name='patients',
            name='photo3',
        ),
        migrations.RemoveField(
            model_name='patients',
            name='previous_report',
        ),
        migrations.RemoveField(
            model_name='patients',
            name='smoker',
        ),
        migrations.AddField(
            model_name='patients',
            name='dental_image1',
            field=models.ImageField(blank=True, null=True, upload_to='dental_images/'),
        ),
        migrations.AddField(
            model_name='patients',
            name='dental_image2',
            field=models.ImageField(blank=True, null=True, upload_to='dental_images/'),
        ),
        migrations.AddField(
            model_name='patients',
            name='dental_image3',
            field=models.ImageField(blank=True, null=True, upload_to='dental_images/'),
        ),
        migrations.AddField(
            model_name='patients',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='patients',
            name='is_smoker',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patients',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='patients',
            name='pdf_file',
            field=models.FileField(blank=True, null=True, upload_to='patient_pdfs/'),
        ),
        migrations.AlterField(
            model_name='patients',
            name='blood_group',
            field=models.CharField(blank=True, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='patients',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1, null=True),
        ),
        migrations.RemoveField(
            model_name='patients',
            name='supplements',
        ),
        migrations.AddField(
            model_name='patients',
            name='supplements',
            field=models.ManyToManyField(blank=True, null=True, to='home_app.supplement'),
        ),
    ]
