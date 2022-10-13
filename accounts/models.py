from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=70)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']


