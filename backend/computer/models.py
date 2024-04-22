from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.
class Computer(models.Model):  # TODO переписать класс под карты
    description = models.CharField(max_length=100)
    processor = models.ForeignKey(
        "components.Components_processor",
        verbose_name="processor",
        on_delete=models.CASCADE,
    )
    videocard = models.ForeignKey(
        "components.Components_VideoCard",
        verbose_name="videocard",
        on_delete=models.CASCADE,
    )
    ram = models.ForeignKey(
        "components.Components_RAM",
        verbose_name="ram",
        on_delete=models.CASCADE
    )
    motherboard = models.ForeignKey(
        "components.Components_motherboard",
        verbose_name="motherboard",
        on_delete=models.CASCADE,
    )
    memory = models.ForeignKey(
        "components.Components_Memory",
        verbose_name="memory",
        on_delete=models.CASCADE,
    )
    power_supply = models.IntegerField(validators=[MinValueValidator(1)])
    price = models.IntegerField(validators=[MinValueValidator(1)])
    raiting = models.IntegerField(validators=[MinValueValidator(1)])

    def create_description(self) -> None:
        self.description = f'Цена компьютера {self.price}, рейтинг производительности компьютера{self.raiting}'
        self.save()

    def get_tdp(self) -> None:
        self.power_supply = (
                self.processor.tdp
                + self.videocard.tdp
                + self.ram.tdp
                + self.motherboard.tdp
                + self.memory.tdp
        )
        self.save()

    def get_price(self) -> None:
        self.price = (
                self.processor.price
                + self.videocard.price
                + self.ram.price
                + self.motherboard.price
                + self.memory.price
        )
        self.save()

    def __str__(self) -> str:
        return f'Computer: {self.id}'
