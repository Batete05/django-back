from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

def get_default_user():
    CustomUser = get_user_model()  # Get the custom user model
    return CustomUser.objects.first()  

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    organizer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="organized_events",
    )
    # participants = models.ManyToManyField(
    #     settings.AUTH_USER_MODEL,
    #     through="EventParticipation",
    #     through_fields=('event', 'participant'),  # Ensure correct fields are specified
    #     related_name="events",
    #     blank=True,
    # )

    def __str__(self):
        return self.name


class Organizer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.user.get_full_name()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class EventParticipation(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='event_participations',
        default=get_default_user  # Correct default user assignment
    )
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    participant = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='participations'  # Unique related_name
    )
    registration_date = models.DateTimeField(auto_now_add=True)
    date_joined = models.DateTimeField(default=timezone.now)  # Only default, no auto_now_add

    class Meta:
        unique_together = ('participant', 'event')

    def __str__(self):
        return f"{self.user} - {self.event}"
