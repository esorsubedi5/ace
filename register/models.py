from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, EmailValidator

class UserProfile(AbstractUser):
    mobile_validator = RegexValidator(
        regex=r'^\d{10,15}$',
        message='Mobile number must be between 10 and 15 digits.',
        code='invalid_mobile'
    )
    email_validator = EmailValidator(message='Enter a valid email address.', code='invalid_email')

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    mobile = models.CharField(max_length=15, unique=True, validators=[mobile_validator])
    email = models.EmailField(unique=True, validators=[email_validator])
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.username
