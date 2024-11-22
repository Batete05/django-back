from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        # ('admin','Admin'),
        ('volunteer', 'Volunteer'),
        ('organizer', 'Organizer'),
    ]
    role= models.CharField(max_length=20, choices=ROLE_CHOICES, default='')
    


    def __str__(self):
        return self.username

