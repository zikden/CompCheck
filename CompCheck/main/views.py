from django.shortcuts import render


def main_page(request):
    context = {
        "title": "home",
    }
    return render(request, "main/main.html", context=context)


def about(request):
    context = {
        "title": "about",
    }
    return render(request, "main/about.html", context=context)
