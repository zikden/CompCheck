from django.contrib import admin
from .models import (
    Components_processor,
    Components_VideoCard,
    Components_RAM,
    Components_motherboard,
    Components_Memory
)

# Register your models here.
admin.site.register(Components_processor)
admin.site.register(Components_VideoCard)
admin.site.register(Components_RAM)
admin.site.register(Components_motherboard)
admin.site.register(Components_Memory)
