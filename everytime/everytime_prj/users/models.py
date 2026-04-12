from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    university = models.CharField(max_length=50)
    email = models.EmailField(max_length=30, unique=True)
    nickname = models.CharField(max_length=20, unique = True)