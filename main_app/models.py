from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

class Family(models.Model):
    name = models.CharField(max_length=100)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_of_families') # Admin user of the family
    family_code = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name
        
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(null=True, blank=True)
    family = models.ForeignKey(Family, on_delete=models.CASCADE, related_name='members', null=True) # User's family
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250, blank=True)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=250, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) # User who created the event
    attendees = models.ManyToManyField(UserProfile, blank=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'event_id': self.id})
    
class Attendee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ManyToManyField(Event, blank=True)
    
    def __str__(self):
        return f'{self.user} is attending {self.event}'