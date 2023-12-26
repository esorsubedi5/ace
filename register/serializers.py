from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator, EmailValidator

User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    mobile_validator = RegexValidator(
        regex=r'^\d{10,15}$',
        message='Mobile number must be between 10 and 15 digits.',
        code='invalid_mobile'
    )
    email_validator = EmailValidator(message='Enter a valid email address.', code='invalid_email')

    mobile = serializers.CharField(validators=[mobile_validator])
    email = serializers.EmailField(validators=[email_validator])
    email2 = serializers.EmailField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'mobile', 'email', 'email2', 'first_name', 'last_name', 'password', 'password2']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data['email'] != data['email2']:
            raise serializers.ValidationError("Emails Don't Match")

        email_qs = User.objects.filter(email=data['email'])
        mobile_qs = User.objects.filter(mobile=data['mobile'])
        if email_qs.exists():
            raise serializers.ValidationError("Email is already in use")
        if mobile_qs.exists():
            raise serializers.ValidationError("Mobile Number is already in use")

        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords Don't Match")

        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            mobile=validated_data['mobile'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password']
        )
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)
