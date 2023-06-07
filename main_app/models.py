from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    date_time = models.DateTimeField('Date & Time')
    location = models.CharField(max_length=250)

    def __str__(self):
        return self.title
    
