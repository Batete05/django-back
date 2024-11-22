from django import forms
from .models import Participant



class ParticipantDataForm(forms.ModelForm):
    
    class Meta:
        model = Participant
        fields=['user','event']

