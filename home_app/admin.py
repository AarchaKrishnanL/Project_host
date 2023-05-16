from django.contrib import admin
from .models import Services, Doctors, Booking, Patients, Appointment, Time_slot, Details_User, Details_Doctor,Patients
from django.contrib.auth.models import Group
# Register your models here.


admin.site.register(Services)
admin.site.register(Doctors)
# admin.site.register(Patient)
#admin.site.register(Appointment)
admin.site.register(Time_slot)
admin.site.unregister(Group)



class BookingAdmin(admin.ModelAdmin):
    list_display = ('doc_name', 'booking_date', 'booked_on','time_slot','description')

admin.site.register(Booking, BookingAdmin)

# class DetailsUserAdmin(admin.ModelAdmin):
#     list_display = ('blood_group','gender','age','address','allergies')

# admin.site.register(Details_User, DetailsUserAdmin)

class DetailsDoctorAdmin(admin.ModelAdmin):
    list_display = ('gender','age','address','year_of_experience')

admin.site.register(Details_Doctor, DetailsDoctorAdmin)

class PatientsModelAdmin(admin.ModelAdmin):
    list_display = ['id','gender','blood_group','date_of_birth','previous_report','supplements','health_issues',
                    'allergies','smoker','beverages','claustrophobic','pain','photo1','photo2','photo3']


admin.site.register(Patients)