from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Event, CustomUser
from main_app.models import CustomUser

# Register your models here.
admin.site.register(CustomUser, UserAdmin)
admin.site.register(Event)