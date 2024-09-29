from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=10, blank=True, null=True)


class Country(models.Model):
    country_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.country_name}"


class City(models.Model):
    city_name = models.CharField(max_length=50)
    country = models.ForeignKey(
        "users.Country",
        verbose_name="Country",
        related_name="country",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.city_name}"


class District(models.Model):
    district_name = models.CharField(max_length=50)
    city = models.ForeignKey(
        "users.City",
        verbose_name="disctrict",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.district_name}"
