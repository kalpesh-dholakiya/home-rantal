from django.contrib import admin
from django.urls import path
from Home_Rental_System import views

urlpatterns = [
    path("",views.index,name='home'),
    path("about",views.about,name='about'),
    path("contact",views.contact,name='contact'),
    path("apartment",views.apartment,name='apartment')
]