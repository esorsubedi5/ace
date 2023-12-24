# register/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http import HttpResponse

from .forms import UserLoginForm, UserRegisterForm
from ace.views import home
User = get_user_model()

def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return HttpResponse('<script>window.opener.location.reload(); window.close();</script>')
        else:
            return HttpResponse('<script>window.opener.location.reload(); window.close();</script>')

    context = {'form': form}
    return render(request, "registration\login.html", context)

def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.save()
        print("User created:", user)
        
        # Check if authentication is successful
        new_user = authenticate(username=user.username, password=user.password)
        print("Authenticated user:", new_user)

        if new_user is not None:
            login(request, new_user)
        else:
            print("Authentication failed")

        if next:
            return redirect(next)
        return redirect('register:login')

    context = {'form': form}
    return render(request, "registration/register.html", context=context)


def logout_view(request):
    logout(request)
    return redirect(home)
