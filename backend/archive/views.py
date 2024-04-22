from django.shortcuts import render
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from .models import Processor, VideoCard
from .serealizers import ProcessorSerializer, VideoCardSerializer


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


class ProcessorViewSet(ModelViewSet):
    queryset = Processor.objects.all()
    serializer_class = ProcessorSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    permission_classes = [IsAdminUser]
    search_fields = []
    ordering_fields = []


class VideoCardViewSet(ModelViewSet):
    queryset = VideoCard.objects.all()
    serializer_class = VideoCardSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    permission_classes = [IsAdminUser]
    search_fields = []
    ordering_fields = []
