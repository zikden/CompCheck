from django.shortcuts import render
from .models import (
    Components_Memory,
    Components_motherboard,
    Components_processor,
    Components_RAM,
    Components_VideoCard,
)


# Create your views here.
def CardsComponentsViews(request):
    components_memory = Components_Memory.objects.all().order_by(
        "-created_at"
    )
    components_motherboard = Components_motherboard.objects.all().order_by(
        "-created_at"
    )
    components_processor = Components_processor.objects.all().order_by(
        "-created_at"
    )
    components_ram = Components_RAM.objects.all().order_by(
        "-created_at"
    )
    components_videocard = Components_VideoCard.objects.all().order_by(
        "-created_at"
    )

    cards = (
        list(components_memory)
        + list(components_motherboard)
        + list(components_processor)
        + list(components_ram)
        + list(components_videocard)
    )
    cards.sort(key=lambda card: card.created_at, reverse=True)

    context = {
        "title": "Компоненты",
        "cards": cards,
    }
    return render(request, "components/components.html", context=context)
