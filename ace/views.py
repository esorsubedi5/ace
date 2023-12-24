# ace/views.py
from django.shortcuts import render
from django.urls import reverse

def home(request):
    context = {
        'register_url': reverse("register:register"),  # Make sure the namespace is used correctly
    }
    return render(request, "registration/home.html", context)
