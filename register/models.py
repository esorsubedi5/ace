from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null =True)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.username
