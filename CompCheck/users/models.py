from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    user_telephone = models.CharField(max_length=12)
