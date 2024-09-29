from django.db.models.functions import Cast
from django.shortcuts import render

from .models import (Components_processor,
                     Components_VideoCard,
                     Components_Memory,
                     Components_motherboard,
                     Components_RAM
                     )


def ComponentsViews(request):
    # TODO дописать запрос ко всем карточкам
    processors = Components_processor.objects.annotate(
        name=Cast("")
    ).values(
        "id",
        "price",
        "name"
    )
    videocards = Components_VideoCard.objects.all()
    memorys = Components_Memory.objects.all()
    motherboars = Components_motherboard.objects.all()
    rams = Components_RAM.objects.all()
    components = processors | videocards | memorys | \
        motherboars | rams
    context = {
        "title": "Компоненты",
        "components": components,
    }
    return render(request, "components/components.html", context=context)
