# models.py

from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group

class UserProfile(AbstractUser):
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='user_profiles',
        verbose_name='user profile permissions',
    )
    groups = models.ManyToManyField(
        Group,
        blank=True,
        related_name='user_profiles',
        verbose_name='user profile groups',
    )

    def __str__(self):
        return self.username
