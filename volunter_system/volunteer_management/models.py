from django.db import models
from django.conf import settings  # Correct import for user model reference
from event_management.models import Event  # Import the Event model

def get_default_event():
    return Event.objects.first().id

class Participant(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Corrected field
    event = models.ForeignKey(Event, on_delete=models.CASCADE,default=get_default_event)


    def __str__(self):
        return f"{self.user.username},{self.event.name}"
    
    class Meta:
        db_table = 'participants_data'