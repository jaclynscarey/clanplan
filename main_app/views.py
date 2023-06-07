from django.shortcuts import render
from .models import Event

# Create your views here.
def home(request):
    return render(request, 'home.html')

def events_index(request):
    events = Event.objects.all()
    return render(request, 'events/index.html', {
        'events': events
        })

def events_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, 'events/detail.html', {
        'event': event
        })

