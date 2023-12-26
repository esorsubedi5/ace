from django.urls import path
from .views import UserRegisterAPIView, UserLoginAPIView, UserLogoutAPIView

app_name = 'register'

urlpatterns = [
    path('api/register/', UserRegisterAPIView.as_view(), name='api-register'),
    path('api/login/', UserLoginAPIView.as_view(), name='api-login'),
    path('api/logout/', UserLogoutAPIView.as_view(), name='api-logout'),
]
