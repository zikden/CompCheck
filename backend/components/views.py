from django.shortcuts import render
from .models import Components_processor

# Create your views here.
def components(request):
    processors = Components_processor.objects.all()
    context = {
        "processors": processors,
    }
    return render(request, "archive/archive.html", context=context)
