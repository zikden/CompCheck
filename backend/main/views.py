from django.shortcuts import render


def main_page(request):
    context = {
        "title": "Главная",
    }
    return render(request, "main/main.html", context=context)


def about(request):
    context = {
        "title": "О нас",
    }
    return render(request, "main/about.html", context=context)
