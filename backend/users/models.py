from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Extended User model
    """
    username = models.CharField("Логин пользователя", unique=True, max_length=255)

    def __str__(self):
        return self.email + ' ' + self.username

class UserEmail(models.Model):
    """Collect emails"""
    email = models.CharField("User email", max_length=100)

    status = models.CharField("User status", 
                              max_length=50, 
                              choices=(('subscribe', 'subscribe'), ('report', 'report')),
                              default='report')

    def __str__(self) -> str:
        return self.email