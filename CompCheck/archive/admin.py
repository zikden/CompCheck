from django.contrib import admin
from .models import (
    Proccesor,
    VideoCard,
    ProccesorBrend,
    ProccesorModel,
    Soket,
    Memory_type,
    VideocardBrand,
    VideoChipset,
)


# Register your models here.
admin.site.register(Proccesor)
admin.site.register(ProccesorBrend)
admin.site.register(ProccesorModel)
admin.site.register(Soket)
admin.site.register(Memory_type)

admin.site.register(VideoCard)
admin.site.register(VideocardBrand)
admin.site.register(VideoChipset)
