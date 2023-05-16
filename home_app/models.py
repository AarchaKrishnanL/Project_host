import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db.models import Count
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.

class CustomUser(AbstractBaseUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField('User Email')
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + self.email + self.phone_number


class Services(models.Model):
    ser_name = models.CharField(max_length=100,unique=True)
    ser_description = models.TextField()
    ser_image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.ser_name

class Doctors(models.Model):
    doc_name = models.CharField(max_length=200,unique=True)
    doc_spec = models.CharField(max_length=200)
    ser_name = models.ForeignKey(Services,on_delete=models.CASCADE)
    doc_image = models.ImageField(upload_to='doctors')

    def __str__(self):
        return self.doc_name


class Time_slot(models.Model):
    time_slot = models.CharField(max_length=100,null=True,blank=True,unique=True)

    def __str__(self):
            return self.time_slot




class Booking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True,blank=True)
    doc_name= models.ForeignKey(Doctors,on_delete=models.CASCADE,null=True,blank=True)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)
    time_slot = models.ForeignKey(Time_slot, on_delete=models.CASCADE,null=True,blank=True)
    description = models.TextField(blank=True)


    def __str__(self):
        return self.description


    def clean(self):
            # count the number of existing appointments for the specified time slot and date
            existing_appointments = Booking.objects.filter(
                booking_date=self.booking_date,
                time_slot=self.time_slot
                ).aggregate(num_appointments=Count('id'))['num_appointments']

           # limit the number of appointments to 2 per time slot
            if existing_appointments >= 2:
                raise ValidationError(f"Sorry, the time slot '{self.time_slot}' is already fully booked.")

class Patients(models.Model):
    GENDER_CHOICES = [
        ('female', 'Female'),
        ('male', 'Male'),
        ('other', 'Other'),
    ]

    BLOOD_GROUP_CHOICES = [
        ('O+', 'O+'),
        ('A+', 'A+'),
        ('B+', 'B+'),
        ('AB+', 'AB+'),
        ('O-', 'O-'),
        ('A-', 'A-'),
        ('B-', 'B-'),
        ('AB-', 'AB-'),
    ]

    SUPPLIMENT_CHOICES = [
        ('Multivitamin','Multivitamin'),
        ('Omega3', 'Omega3'),
        ('Vitamin3', 'Vitamin3'),
        ('BComplex', 'BComplex'),
        ('Vitamin D/D3', 'Vitamin D/D3'),
        ('Zinc', 'Zinc'),
        ('Folic Acid', 'Folic Acid'),
        ('Melatonin', 'Melatonin'),
        ('Biotin', 'Biotin'),
        ('Coenzyme', 'Coenzyme'),
        ('None', 'None'),
        ('Other', 'Other'),
    ]

    ISSUES_CHOICES = [
        ('Hormone Imbalance','Hormone Imbalance'),
        ('Asthma', 'Asthma'),
        ('Cancer/Systemic disease', 'Cancer/Systemic disease'),
        ('Epilepsy/Seizure', 'Epilepsy/Seizure'),
        ('High Blood Pressure', 'High Blood Pressure'),
        ('Diabetes', 'Diabetes'),
        ('Heart Problems', 'Heart Problems'),
        ('HIV/AIDS', 'HIV/AIDS'),
        ('Auto immune Disorder', 'Auto immune Disorder'),
        ('Depression', 'Depression'),
        ('HeadAches/Migrations', 'HeadAches/Migrations'),
        ('Other', 'Other'),
        ('None', 'None'),
    ]

    ALLERGY_CHOICES = [
        ('Aspirin','Aspirin'),
        ('Shellfish', 'Shellfish'),
        ('Tree Nuts', 'Tree Nuts'),
        ('Iodine', 'Iodine'),
        ('Latex', 'Latex'),
        ('Dairy', 'Dairy'),
        ('Fruits', 'Fruits'),
        ('Vegetables', 'Vegetables'),
        ('Other', 'Other'),
        ('None', 'None'),
    ]

    SMOKER_CHOICES = [
        ('yes','yes'),
        ('no', 'no'),
    ]
    BEVARAGE_CHOICES = [
        ('yes', 'yes'),
        ('no', 'no'),
    ]
    CLAUSTROPHOBIC_CHOICES = [
        ('yes', 'yes'),
        ('no', 'no'),
    ]
    PAIN_CHOICES = [
        ('low', 'low'),
        ('medium', 'medium'),
        ('high','high'),
    ]

    gender = models.CharField(max_length=6, choices=GENDER_CHOICES,null=True,blank=True)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES,null=True,blank=True)
    date_of_birth = models.DateField(auto_now=False,auto_now_add=False,null=True,blank=True)
    previous_report = models.FileField(upload_to='previous_reports/',null=True,blank=True)
    supplements = models.CharField(choices=SUPPLIMENT_CHOICES,max_length=50,blank=True,null=True)
    health_issues = models.CharField(choices=ISSUES_CHOICES,max_length=50,blank=True, null=True)
    allergies = models.CharField(choices=ALLERGY_CHOICES,max_length=50,blank=True,null=True)
    smoker = models.CharField(choices=SMOKER_CHOICES,max_length=50,blank=True,null=True)
    beverages = models.CharField(choices=BEVARAGE_CHOICES,max_length=50,blank=True,null=True)
    claustrophobic = models.CharField(choices=CLAUSTROPHOBIC_CHOICES,max_length=50,blank=True,null=True)
    pain = models.CharField(choices=PAIN_CHOICES,max_length=50,blank=True,null=True)
    photo1 = models.ImageField(upload_to='photos/',blank=True,null=True)
    photo2 = models.ImageField(upload_to='photos/',blank=True,null=True)
    photo3 = models.ImageField(upload_to='photos/',blank=True,null=True)













class Details_Doctor(models.Model):

    gender = models.CharField(max_length=10, null=True, blank=True)
    age = models.CharField(max_length=3,null=True,blank=True)
    address = models.CharField(max_length=200,null=True,blank=True)
    year_of_experience = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return   self.gender + self.age + self.address + self.year_of_experience


class Update_Booking(models.Model):
    doc_name= models.ForeignKey(Doctors,on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)
    time_slot = models.ForeignKey(Time_slot, on_delete=models.CASCADE,null=True,blank=True)
    description = models.TextField(blank=True)


    def __str__(self):
        return self.booked_on






