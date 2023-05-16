from django.template.context_processors import static
from django.urls import path, include

from dental_project import settings
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.demo,name='home'),
    path('about/', views.about,name='about'),
    path('front', views.front,name='front'),
    path('booking', views.booking,name='booking'),
    path('doctors', views.doctors,name='doctors'),
    path('contact', views.contact,name='contact'),
    path('services', views.services,name='services'),
    path('time_slot', views.time_slot,name='time_slot'),
    path('login', views.user_login,name='login'),
    path('register', views.register,name='register'),
    path('index', views.index,name='index'),
    path('indexx', views.indexx, name='indexx'),
    path('payment', views.payment,name='payment'),
    path('details_successfull', views.details_successfull,name='details_successfull'),
    path('thanks', views.thanks,name='thanks'),
    path('consultation_view', views.consultation_view, name='consultation_view'),
     path('doctorlogin', views.doctorlogin, name='doctorlogin'),
    path('doctor_patient', views.doctor_patient, name='doctor_patient'),
    path('patient_form', views.patient_form.as_view(), name='patient_form'),
    path('user', views.user,name='user'),
    path('logout', views.logout, name='logout'),
    path('toconsult_form', views.toconsult_form, name='toconsult_form'),
    path('my_bookings', views.my_bookings, name='my_bookings'),
    path('update_booking', views.update_booking, name='update_booking'),
    path('update_details', views.update_details, name='update_details'),
    path('loginn', views.loginn, name='loginn'),
    path('predict', views.predict, name='predict'),
    path('doctor_page', views.doctor_page, name='doctor_page'),
    path('doctors_search', views.doctors_search, name='doctors_search'),
    path('services_search', views.services_search, name='services_search'),
    path('doctor_bookings', views.doctor_bookings, name='doctor_bookings'),
    path('<int:id>', views.update_details, name='update_details'),
    path('details_doctor', views.details_doctor, name='details_doctor'),
    path('view_receipt/<id>', views.view_receipt, name='view_receipt'),
    path('view_receipts', views.view_receipts, name='view_receipts'),
    # path('generate_pdf', views.generate_pdf, name='generate_pdf'),
    path('doctor_register', views.doctor_register, name='doctor_register'),
    path('<int:id>', views.update_doctor, name='update_doctor'),
    path("__reload__/", include("django_browser_reload.urls")),

    # CRUD
    path('delete/<str:id>', views.Delete, name='delete'),
    # path('<str:id>', views.Update, name='update'),

    path('bonding', views.bonding, name='bonding'),
    path('crown', views.crown, name='crown'),
    path('veeners', views.veeners, name='veeners'),
    path('cleaning', views.cleaning, name='cleaning'),
    path('filling', views.filling, name='filling'),
    # path('veeners', views.veeners, name='veeners'),


####reset password urls####
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),


]