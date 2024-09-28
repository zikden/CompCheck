from django.shortcuts import render
from .models import CardsComponents


# Create your views here.
def CardsComponentsViews(request):
    components = CardsComponents.objects.all()
    component_processors = components
    context = {
        "title": "Компоненты",
        "component_processors": component_processors,
    }
    return render(request, "components/components.html", context=context)
