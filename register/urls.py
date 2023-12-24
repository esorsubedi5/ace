# register/urls.py
from django.urls import path
from .views import login_view, register_view, logout_view

app_name = 'register'  # Make sure the app_name is set to 'register'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
]
