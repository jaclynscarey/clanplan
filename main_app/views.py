from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import Event

def home(request):
    return render(request, 'home.html')

@login_required
def events_index(request):
    events = Event.objects.all()
    return render(request, 'events/index.html', {
        'events': events
        })

@login_required
def events_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, 'events/detail.html', {
        'event': event
        })

class EventCreate(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['title', 'description', 'date', 'time', 'location', 'attendees']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)    

class EventUpdate(LoginRequiredMixin, UpdateView):
    model = Event
    fields = ['title', 'description', 'date', 'time', 'location', 'attendees']

class EventDelete(LoginRequiredMixin, DeleteView):
    model = Event
    fields = '__all__'
    success_url = '/events/'

