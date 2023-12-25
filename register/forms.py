from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if not user:
                raise forms.ValidationError('User Does Not Exist')

            if not user.check_password(password):
                raise forms.ValidationError('Incorrect Password')

        return cleaned_data

class UserRegisterForm(UserCreationForm):
    mobile = forms.CharField(max_length=15)
    email = forms.EmailField(label='Email Address')
    email2 = forms.EmailField(label='Confirm Email Address')
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = [
            'username',
            'mobile',
            'email',
            'email2',
            'first_name',
            'last_name',
            'password1',
            'password2',
        ]

    def clean(self, *args, **kwargs):
        cleaned_data = super().clean()
        mobile = cleaned_data.get('mobile')
        email = cleaned_data.get('email')
        email2 = cleaned_data.get('email2')

        if email != email2:
            raise forms.ValidationError("Emails Don't Match")

        email_qs = User.objects.filter(email=email)
        mobile_qs = User.objects.filter(mobile=mobile)
        if email_qs.exists():
            raise forms.ValidationError("Email is already in use")
        if mobile_qs.exists():
            raise forms.ValidationError("Mobile Number is already in use")

        return cleaned_data
