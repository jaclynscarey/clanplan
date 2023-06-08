from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=250)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'event_id': self.id})
    
class CustomUser(AbstractUser):
    birthdate = models.DateField(null=True)
    
    def __str__(self):
        return self.username