from django.contrib import admin
from django.urls import path

from . import views #from .  = şuanki klasör anlamında
app_name = "user"

urlpatterns = [
    path('register/', views.register, name="register"), 
    path('login/', views.loginUser, name="login"), 
    path('logout/', views.logoutUser, name="logout"), 
]