# ace/views.py
from django.shortcuts import render
from django.urls import reverse

def home(request):
    context = {
        'register_url': reverse("register:api-register"),  # Corrected name to 'api-register'
    }
    return render(request, "registration/home.html", context)
