from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Extended User model
    """
    username = models.CharField("Логин пользователя", unique=True, max_length=255)

    def __str__(self):
        return self.email + ' ' + self.username