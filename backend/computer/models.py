from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
class Computer(models.Model): #TODO переписать класс под карты
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
