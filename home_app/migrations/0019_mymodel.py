# Generated by Django 4.1.1 on 2023-05-09 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0018_alter_cart_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf_file', models.FileField(upload_to='pdfs/')),
            ],
        ),
    ]
