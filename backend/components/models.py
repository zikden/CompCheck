from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.
# TODO Добавить класс для карточек компонентов
class CardsComponents(models.Model):
    category_componetns = models.CharField(max_length=63)

    def __str__(self):
        return f"{self.category_componetns}"


class Components_processor(models.Model):
    category = models.ForeignKey(
        "components.CardsComponents",
        verbose_name="component_processor",
        related_name="category_processor",
        on_delete=models.CASCADE
    )
    processor = models.ForeignKey(
        "archive.Processor",
        verbose_name="processor",
        related_name="components_processor",
        on_delete=models.CASCADE
    )
    raiting_for_price = models.DecimalField(decimal_places=2, max_digits=8)
    tdp = models.IntegerField(validators=[MinValueValidator(1)], default=80)
    url = models.URLField(max_length=255, unique=True)
    city = models.ForeignKey("users.City", on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=8)

    def rfp_calculation(self):
        self.raiting_for_price = self.processor.raiting/self.price
        self.save()
        return self.raiting_for_price

    def __str__(self) -> str:
        return f'{self.processor}'

    class Meta:
        verbose_name = "CardsComponent"
        verbose_name_plural = "CardsComponents"


class Components_VideoCard(models.Model):
    category = models.ForeignKey(
        "components.CardsComponents",
        verbose_name="component_videocard",
        related_name="category_videocard",
        on_delete=models.CASCADE
    )
    videocard = models.ForeignKey(
        "archive.VideoCard",
        verbose_name="videocard",
        related_name="components_videocard",
        on_delete=models.CASCADE
    )
    raiting_for_price = models.DecimalField(decimal_places=2, max_digits=8)
    tdp = models.IntegerField(validators=[MinValueValidator(1)], default=150)
    url = models.URLField(max_length=255, unique=True)
    city = models.ForeignKey("users.City", on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=8)

    def rfp_calculation(self):
        self.raiting_for_price = self.raiting/self.price
        self.save()
        return self.raiting_for_price

    class Meta:
        verbose_name = "Component_VideoCard"
        verbose_name_plural = "Components_VideoCard"

    def __str__(self):
        return f"{self.videocard}"


class Components_RAM(models.Model):
    memory_type = models.ForeignKey(
        "archive.Memory_type",
        on_delete=models.CASCADE
    )
    ram = models.IntegerField(validators=[MinValueValidator(1)])
    mfs = models.IntegerField(validators=[MinValueValidator(1)])
    amount = models.IntegerField(validators=[MinValueValidator(1)], default=1)
    tdp = models.IntegerField(validators=[MinValueValidator(1)], default=15)
    url = models.URLField(max_length=255, unique=True)
    city = models.ForeignKey("users.City", on_delete=models.CASCADE)
    price = models.IntegerField(validators=[MinValueValidator(1)])

    def tdp_calculation(self):
        self.tdp = self.amount * 4
        self.save()

    class Meta:
        verbose_name = "Component_RAM"
        verbose_name_plural = "Components_RAM"


class Components_motherboard(models.Model):
    soket = models.ForeignKey(
        "archive.Soket",
        on_delete=models.CASCADE
    )
    memory_type = models.ForeignKey(
        "archive.Memory_type",
        on_delete=models.CASCADE
    )
    tdp = tdp = models.IntegerField(validators=[MinValueValidator(1)], default=50)
    url = models.URLField(max_length=255, unique=True)
    city = models.ForeignKey("users.City", on_delete=models.CASCADE)
    price = models.IntegerField(validators=[MinValueValidator(1)])


class Components_Memory(models.Model):
    amount = models.IntegerField(validators=[MinValueValidator(1)])
    tdp = models.IntegerField(validators=[MinValueValidator(1)])
    url = models.URLField(max_length=255, unique=True)
    city = models.ForeignKey("users.City", on_delete=models.CASCADE)
    price = models.IntegerField(validators=[MinValueValidator(1)])

    def tdp_calculation(self):
        self.tdp = self.amount * 5
        self.save()
