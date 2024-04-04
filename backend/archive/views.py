from django.shortcuts import render

from .models import Processor, VideoCard

# Create your views here.


def archive(request):
    context = {
        "title": "Архив"
        }
    return render(request, "archive/archive.html", context=context)

def CPU(request):
    processors = Processor.objects.all()
    context = {
        "title": "Процессоры",
        "processors": processors
        }
    return render(request, "archive/CPU.html", context=context)

def GPU(request):
    videocards = VideoCard.objects.all()
    context = {
        "title": "Видеокарты",
        "videocards": videocards
        }
    return render(request, "archive/GPU.html", context=context)
