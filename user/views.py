from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import LoginForm, RegisterForm
from user import forms

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout #Kayıt olduktan sonra login olmasını sağlamak için
# authenticate := username ve password var mı yok mu sorguluyor
# Create your views here.

def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        newUser = User(username = username)
        newUser.set_password(password)
        newUser.save()
        login(request, newUser)
        messages.success(request, "Başarıyla kayıt olundu. Giriş işleminiz otomatik olarak yapıldı.")
        return redirect("index")
    context = {
            "form" : form
        }
    return render(request, 'register.html', context)

def loginUser(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        form = LoginForm(request.POST or None)
        context = {
            "form": form
        }
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password") 
            user = authenticate(username=username, password=password)

            if user is None:
                messages.info(request, "Kullanıcı adı veya parola hatalı !")
                return render(request, "login.html", context)
            
            messages.success(request, "Başarıyla giriş yapıldı !")
            login(request, user)
            return redirect("index")
        return render(request, "login.html", context)

def logoutUser(request):
    logout(request)
    messages.success(request, "Çıkış başarıyla yapıldı.")
    return redirect("index")