from django.db import models
from django.conf import settings  # Correct import for user model reference
from event_management.models import Event  # Import the Event model

class Participant(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Corrected field
    events = models.ManyToManyField(Event, related_name='registered_participants')  # Event relationship

    def __str__(self):
        return self.user.username
