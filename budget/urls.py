from django.contrib import admin
from django.urls import path
from . import views

app_name = 'budget'

urlpatterns = [
    path('', views.home, name='homepage'),
    path('aboutus', views.aboutus, name='aboutus')
]