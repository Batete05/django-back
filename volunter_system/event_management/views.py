# event_management/views.py
from datetime import timezone
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import get_user_model
from .models import Event,EventParticipation
from django.contrib.auth.decorators import login_required
from .forms import EventForm
from django.http import HttpResponse
from django import forms
import json
from django.db.models import Count
# from datetime import datetime,date
from django.contrib import messages

from volunteer_management.models import Participant

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
            return redirect('event_li')  
    else:
        form = EventForm(instance=event)
    
    return render(request, 'event_management/edit_event.html', {'form': form})


def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)  
    if request.method == 'POST':
        event.delete()
        messages.success(request, 'Event deleted successfully!')
        return redirect('event_li')  
    return render(request, 'event_management/delete_event.html', {'event': event})

def organizer_dashboard(request):

    if not request.user.is_authenticated:
        return redirect('login')

    events = Event.objects.filter(organizer=request.user)

    context = {
        'events': events,
    }

    return render(request, 'event_management/organizer_dashboard.html', context)


@login_required
def volunteer_for_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    user = request.user  # Assuming user is logged in

    # # Check if the user is already participating in the event (optional)
    # if not EventParticipation.objects.filter(event=event, user=user).exists():
    #     EventParticipation.objects.create(
    #         user=user,
    #         event=event,
    #         date_joined=timezone.now()
    #     )

    # return redirect('event_statistics') 
    participation, created = EventParticipation.objects.get_or_create(
        user=user,
        # participant=user;
        event=event,
        defaults={'date_joined': timezone.now()},
    )

    if created:
        print(f"Participation created: {participation}")
    else:
        print("Participation already exists.")

    return redirect('event_statistics')

# def event_volunteers(request, event_id):
#     event = get_object_or_404(Event, id=event_id)
    
    
#     return render(request, 'event_management/event_volunteers.html', {'event': event, 'participants': participants})

# def event_statistics(request):
#     # Get all events
#     events = Event.objects.all()
#     event_data = []

#     for event in events:
#         # Count the number of volunteers for each event using EventParticipation model
#         volunteer_count = EventParticipation.objects.filter(event=event).count()

#         event_data.append({
#             'event_name': event.name,
#             'participant_count': volunteer_count  # Store the volunteer count for each event
#         })

#     # Pass the event data to the template
#     context = {
#         'event_data': event_data,
#     }
#     return render(request, 'event_management/event_statistics.html', context)

def event_statistics(request):
    events = Participant.objects.values('event__name').annotate(
        participant_count=Count('event')).order_by('event_id')
    
    particionts = Participant.objects.all()

    for event in events:    
        print(f"{event['event__name']}: {event['participant_count']} participation")

    event_data = [
        {'event': event['event__name'], 
         'participant_count':event['participant_count'],
         }

        for event in events
    ]


    context = {
        'event_data': json.dumps(event_data),
    }

    return render(request, 'event_management/event_statistics.html', context)