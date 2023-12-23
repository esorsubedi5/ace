# forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import EmailValidator, RegexValidator
from .models import UserProfile

class CustomUserCreationForm(UserCreationForm):
    mobile = forms.CharField(max_length=15, validators=[RegexValidator(r'^\d{1,15}$')])
    email = forms.EmailField(validators=[EmailValidator()])
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = UserProfile
        fields = ['username', 'mobile', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data['username']
        if UserProfile.objects.filter(username=username).exists():
            raise forms.ValidationError('This username is already in use. Please choose a different one.')
        return username

