# ace/register/tests.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .forms import UserRegisterForm, UserLoginForm

User = get_user_model()

class RegisterTests(TestCase):
    def setUp(self):
        self.register_url = reverse('register:register')
        self.login_url = reverse('register:login')
        self.logout_url = reverse('register:logout')

        self.user_data = {
            'username': 'testuser',
            'mobile': '1234567890',
            'email': 'testuser@example.com',
            'email2': 'testuser@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
    }

        self.login_data = {
            'username': 'testuser',
            'password': 'testpassword123',
        }

    def test_register_view(self):
        response = self.client.post(self.register_url, data=self.user_data)
        if response.status_code != 302:
            print(response.content.decode('utf-8'))
        self.assertRedirects(response, self.login_url)
        self.assertEqual(User.objects.count(), 1)
        self.assertTrue(User.objects.filter(username='testuser').exists())

        # Log in the user
        login_response = self.client.post(self.login_url, data=self.login_data)
        self.assertEqual(login_response.status_code, 302)  # 302 indicates a successful redirect

        # Check if the user is logged in
        self.assertTrue(self.client.user.is_authenticated)


    def test_logout_view(self):
        user = User.objects.create_user(**self.user_data)
        self.client.login(**self.login_data)
        
        response = self.client.post(self.logout_url)
        self.assertEqual(response.status_code, 302)  # 302 indicates a successful redirect
        self.assertFalse(self.client.user.is_authenticated)


    def test_user_register_form(self):
        form = UserRegisterForm(data=self.user_data)
        self.assertTrue(form.is_valid(), form.errors)  # Print form errors if the test fails

    def test_user_login_form(self):
        User.objects.create_user(**self.user_data)
        form = UserLoginForm(data=self.login_data)
        self.assertTrue(form.is_valid(), form.errors)
