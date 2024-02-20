from django.contrib import admin
from .models import (
    Processor,
    VideoCard,
    ProcessorBrand,
    ProcessorModel,
    Soket,
    Memory_type,
    VideocardBrand,
    VideoChipset,
)

# Register your models here.
admin.site.register(Processor)
admin.site.register(ProcessorBrand)
admin.site.register(ProcessorModel)
admin.site.register(Soket)
admin.site.register(Memory_type)

admin.site.register(VideoCard)
admin.site.register(VideocardBrand)
admin.site.register(VideoChipset)
