from django.shortcuts import render,redirect,get_object_or_404
from event_management.models import Event
from django.http import HttpResponse
from .models import Participant
from django.contrib.auth.decorators import login_required

def volunteer_management_view(request):
    return render(request, 'volunteer_management/volunteer_management.html', {'message': 'Welcome to the Volunter page activities Management page!'})

def volunteer_welcome(request):
    events=Event.objects.all()

    return render(request, 'volunteer_management/welcome.html',{'events':events})


@login_required
def event_list(request):
    events=Event.objects.all()
    return render(request, 'volunteer_management/event_list.html',{'events':events})

@login_required
def event_details(request, event_id):
    # Get the event object
    event = get_object_or_404(Event, id=event_id)

    # Check if the user is a participant
    try:
        participant = Participant.objects.get(user=request.user)
    except Participant.DoesNotExist:
        participant = None

    # Prepare the context
    context = {
        'event': event,
        'participant': participant,
    }

    return render(request, 'volunteer_management/event_details.html', context)

@login_required
def profile_view(request):
    participant=Participant.objects.get(user=request.user)
    return render(request,'volunteer_management/profile_view.html',{'participant':participant})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')