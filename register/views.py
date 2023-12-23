from django.contrib.auth import login
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from .models import UserProfile
from ace.views import home

class CustomUserCreationView(CreateView):
    model = UserProfile
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy(home)

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
