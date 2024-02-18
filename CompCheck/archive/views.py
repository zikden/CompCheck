from django.shortcuts import render

from .models import Proccesor

# Create your views here.


def archive(request):
    context = {
        "title": "Архив"
        }
    return render(request, "archive/archive.html", context=context)

def CPU(request):
    processors = Proccesor.objects.all()
    context = {
        "title": "Процессоры",
        "processors": processors
        }
    return render(request, "archive/CPU.html", context=context)

def GPU(request):
    context = {
        "title": "Видеокарты"
        }
    return render(request, "archive/GPU.html", context=context)
