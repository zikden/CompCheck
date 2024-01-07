from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from users.forms import UserLoginForm

def profile(request):
    context = {
        "title": "Твой профиль",
    }
    return render(request, "users/profile.html", context=context)

def registration(request):
    context = {
        "title": "Регистрация",
    }
    return render(request, "users/registration.html", context=context)

def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {
        "title": "Авторизация",
        "form": form
    }
    return render(request, "users/login.html", context=context)


def logout(request):
    context = {
        "title": "Выход из системы",
    }
    return render(request, "users/logout.html", context=context)

def password_reset(request):
    context = {
        "title": "Востановление пароля",
    }
    return render(request, "users/password_reset.html", context=context)
