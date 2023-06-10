from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

class Family(models.Model):
    name = models.CharField(max_length=100)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_of_families') # Admin user of the family
    secret_code = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name
        
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(null=True, blank=True)
    families = models.ManyToManyField(Family, related_name='memberships', blank=True) # User's families
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
    def save(self, *args, **kwargs):
        is_new = not self.pk  # Check if the instance is being created
        super().save(*args, **kwargs)
        if is_new:
            # Create an Attendee instance when a UserProfile is added to an Event
            for event in self.event_set.all():
                Attendee.objects.create(user=self, event=event)
    
class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE) # User who created the event
    attendees = models.ManyToManyField(UserProfile)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'event_id': self.id})
    
class Attendee(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user} is attending {self.event}'