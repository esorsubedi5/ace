from django.urls import path
from .views import CustomUserCreationView

urlpatterns = [
    path('register/', CustomUserCreationView.as_view(), name='register'),
]
