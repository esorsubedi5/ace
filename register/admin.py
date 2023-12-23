# admin.py

from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'mobile', 'email', 'first_name', 'last_name')

admin.site.register(UserProfile, UserProfileAdmin)
