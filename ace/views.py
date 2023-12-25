# ace/views.py
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

def home(request):
    context = {
        'register_url': reverse("register:register"),
    }
    return render(request, "registration/home.html", context)
