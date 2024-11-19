from django.shortcuts import render
from django.http import HttpResponse

def participant_records_view(request):
    return render(request, 'participant_records/participant_records.html', {'message': 'Welcome to the Event Management page!'})
