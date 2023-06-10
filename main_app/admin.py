from django.contrib import admin
from .models import Event, Family, UserProfile, Attendee

# Register your models here.
admin.site.register([Event, Family, UserProfile, Attendee])