from django.db import models


class Proccesor(models.Model):
    brend = models.ForeignKey("archive.ProccesorBrend", on_delete=models.CASCADE)
    proccesor_models = models.ForeignKey(
        "archive.ProccesorModel", on_delete=models.CASCADE
    )
    soket = models.ForeignKey("archive.Soket", on_delete=models.CASCADE)
    memory_type = models.ManyToManyField("archive.Memory_type")
    mfs = models.IntegerField()
    tdp = models.IntegerField()
    raiting = models.DecimalField(decimal_places=2, max_digits=8)

    class Meta:
        verbose_name = "Proccesor"
        verbose_name_plural = "Proccesors"

    def __str__(self):
        return f"Proccesor {self.brend} {self.proccesor_models}"


class ProccesorBrend(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Brend"
        verbose_name_plural = "Brends"

    def __str__(self):
        return self.name


class ProccesorModel(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "ProccesorModel"
        verbose_name_plural = "ProccesorModels"

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
    brand = models.ForeignKey("archive.VideocardBrand", on_delete=models.CASCADE)
    videochipset = models.ForeignKey("archive.VideoChipset", on_delete=models.CASCADE)
    gram = models.IntegerField()
    tdp = models.IntegerField()
    raiting = models.PositiveIntegerField()

    class Meta:
        verbose_name = "VideoCard"
        verbose_name_plural = "VideoCards"

    def __str__(self):
        return "VideoCard"


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
