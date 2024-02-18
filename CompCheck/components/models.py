from django.core.validators import MinValueValidator
from django.db import models

from archive.models import Processor, VideoCard


# Create your models here.
class Components_processor(Processor):
    price = models.DecimalField(decimal_places=2, max_digits=8)
    raiting_for_price = models.DecimalField(decimal_places=2, max_digits=8)
    url = models.URLField(max_length=255, unique=True)

    def rfp_calculation(self):
        self.raiting_for_price = self.raiting/self.price
        self.save()


class Components_VideoCard(VideoCard):
    price = models.DecimalField(decimal_places=2, max_digits=8)
    raiting_for_price = models.DecimalField(decimal_places=2, max_digits=8)
    url = models.URLField(max_length=255, unique=True)

    def rfp_calculation(self):
        self.raiting_for_price = self.raiting/self.price
        self.save()


class Components_RAM(models.Model):
    memory_type = models.ForeignKey(
        "archive.Memory_type",
        on_delete=models.CASCADE
    )
    ram = models.IntegerField(validators=[MinValueValidator(1)])
    mfs = models.IntegerField(validators=[MinValueValidator(1)])
    amount = models.IntegerField(validators=[MinValueValidator(1)])
    tdp = models.IntegerField(validators=[MinValueValidator(1)])
    url = models.URLField(max_length=255, unique=True)
    price = models.IntegerField(validators=[MinValueValidator(1)])

    def tdp_calculation(self):
        self.tdp = self.amount * 4
        self.save()


class Components_motherboard(models.Model):
    soket = models.ForeignKey(
        "archive.Soket",
        on_delete=models.CASCADE
    )
    memory_type = models.ForeignKey(
        "archive.Memory_type",
        on_delete=models.CASCADE
    )
    url = models.URLField(max_length=255, unique=True)
    price = models.IntegerField(validators=[MinValueValidator(1)])


class Components_Memory(models.Model):
    amount = models.IntegerField(validators=[MinValueValidator(1)])
    tdp = models.IntegerField(validators=[MinValueValidator(1)])
    url = models.URLField(max_length=255, unique=True)
    price = models.IntegerField(validators=[MinValueValidator(1)])

    def tdp_calculation(self):
        self.tdp = self.amount * 5
        self.save()


class Computer(models.Model):
    description = models.CharField(max_length=100)
    processor = models.ForeignKey(
        "components.Components_processor",
        verbose_name=("processor"),
        on_delete=models.CASCADE,
    )
    videocart = models.ForeignKey(
        "components.Components_VideoCard",
        verbose_name=("videocart"),
        on_delete=models.CASCADE,
    )
    ram = models.ForeignKey(
        "components.Components_RAM",
        verbose_name=("ram"),
        on_delete=models.CASCADE
    )
    motherboard = models.ForeignKey(
        "components.Components_motherboard",
        verbose_name=("motherboard"),
        on_delete=models.CASCADE,
    )
    memory = models.ForeignKey(
        "components.Components_Memory",
        verbose_name=("memory"),
        on_delete=models.CASCADE,
    )
    power_supply = models.IntegerField(validators=[MinValueValidator(1)])
    price = models.IntegerField(validators=[MinValueValidator(1)])
    raiting = models.IntegerField(validators=[MinValueValidator(1)])

    def create_description(self):
        self.description = f'Цена компьютера {self.price}, рейтинг производительности компьютера{self.raiting}'
        self.save()

    def tdp_calculation(self):
        self.power_supply = (
            self.processor.tdp
            + self.videocart.tdp
            + self.ram.tdp
            + self.motherboard.tdp
            + self.memory.tdp
        )
        self.save()

    def price_calculation(self):
        self.price = (
            self.processor.price
            + self.videocart.price
            + self.ram.price
            + self.motherboard.price
            + self.memory.price
        )
        self.save()
