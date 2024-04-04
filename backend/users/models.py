from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(max_length=10, blank=True, null=True)


class Country(models.Model):
    country_name = models.CharField(max_length=50)


class City(models.Model):
    city_name = models.CharField(max_length=50)
    country = models.ForeignKey(
        "users.Country",
        verbose_name="Country",
        related_name="country",
        on_delete=models.CASCADE,
    )


class District(models.Model):
    district_name = models.CharField(max_length=50)
    city = models.ForeignKey(
        "users.City",
        verbose_name="disctrict",
        on_delete=models.CASCADE
    )
