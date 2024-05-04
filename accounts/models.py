from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True ,max_length=254)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name']

    objects = CustomUserManager()

    def __str__(self) :
        return self.email