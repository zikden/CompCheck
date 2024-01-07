from django.shortcuts import render

def profile(request):
    context = {
        "title": "Твой профиль",
    }
    return render(request, "users/profile.html", context=context)

def login(request):
    context = {
        "title": "Авторизация",
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
