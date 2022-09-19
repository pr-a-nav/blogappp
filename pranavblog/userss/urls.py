from django.urls import path 
from .views import UserRegisterView
import django.contrib.auth.urls

urlpatterns = [
    path('register/',UserRegisterView.as_view(), name='register'),
   
   
]