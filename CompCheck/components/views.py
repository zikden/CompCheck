from django.shortcuts import render

# Create your views here.
def components(request):
    context = {

    }
    return render(request, "archive/archive.html", context=context)
