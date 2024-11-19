# event_management/views.py
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import get_user_model
from .models import Event,Organizer
from .forms import EventForm
from django import forms
# from datetime import datetime,date
from django.contrib import messages

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_management/event_list.html',{'events':events})


def add_event(request):
    if request.method == 'POST':
        # print("Form submitted")
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            # print("Form saved")
            return redirect('event_li')  
    else:
        form = EventForm()

    return render(request, 'event_management/add_event.html', {'form': form})

def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')  
    else:
        form = EventForm(instance=event)
    
    return render(request, 'event_management/edit_event.html', {'form': form})


def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)  
    if request.method == 'POST':
        event.delete()
        messages.success(request, 'Event deleted successfully!')
        return redirect('event_list')  
    return render(request, 'event_management/delete_event.html', {'event': event})

def organizer_dashboard(request):

    if not request.user.is_authenticated:
        return redirect('login')

    events = Event.objects.filter(organizer=request.user)

    context = {
        'events': events,
    }

    return render(request, 'event_management/organizer_dashboard.html', context)