from django.core.validators import MinValueValidator
from django.db import models


class Processor(models.Model):
    brand = models.ForeignKey(
        "app.archive.ProcessorBrand",
        related_name="brand",
        on_delete=models.CASCADE
    )
    processor_models = models.ForeignKey(
        "app.archive.ProcessorModel",
        related_name="processor_model",
        on_delete=models.CASCADE
    )
    soket = models.ForeignKey(
        "app.archive.Soket",
        related_name="soket",
        on_delete=models.CASCADE
    )
    memory_type = models.ManyToManyField(
        "app.archive.Memory_type",
        related_name="memory_type",
    )
    mfs = models.IntegerField()
    tdp = models.IntegerField()
    raiting = models.DecimalField(decimal_places=2, max_digits=8)

    class Meta:
        verbose_name = "Processor"
        verbose_name_plural = "Processors"

    def __str__(self):
        return f"processor {self.brand} {self.processor_models}"


class ProcessorBrand(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"

    def __str__(self):
        return self.name


class ProcessorModel(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "ProcessorModel"
        verbose_name_plural = "ProcessorModels"

    def __str__(self):
        return self.name


class Soket(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Soket"
        verbose_name_plural = "Sokets"

    def __str__(self):
        return self.name


class Memory_type(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Memory_type"
        verbose_name_plural = "Memory_types"

    def __str__(self):
        return self.name


class VideoCard(models.Model):
    brand = models.ForeignKey(
        "app.archive.VideocardBrand",
        related_name="brand",
        on_delete=models.CASCADE
    )
    videochipset = models.ForeignKey(
        "app.archive.VideoChipset",
        related_name="videochipset",
        on_delete=models.CASCADE
    )
    gram = models.IntegerField(validators=[MinValueValidator(1)])
    tdp = models.IntegerField(validators=[MinValueValidator(1)])
    raiting = models.DecimalField(decimal_places=2, max_digits=8)

    class Meta:
        verbose_name = "VideoCard"
        verbose_name_plural = "VideoCards"

    def __str__(self):
        return f"{self.brand} {self.videochipset}"


class VideocardBrand(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "VideocardBrand"
        verbose_name_plural = "VideocardBrands"

    def __str__(self):
        return self.name


class VideoChipset(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "VideoChipset"
        verbose_name_plural = "VideoChipsets"

    def __str__(self):
        return self.name
