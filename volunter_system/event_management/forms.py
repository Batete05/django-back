from django import forms
from .models import Event, Organizer
from user_auth.models import CustomUser

class EventForm(forms.ModelForm):
    organizer = forms.ModelChoiceField(
        queryset=CustomUser.objects.filter(role='organizer'),
        required=True,
        label="Select Organizer",
    )

    class Meta:
        model = Event
        fields = ['name', 'description','date', 'organizer','participants']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),

        }

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        # Filter organizers based on CustomUser's role
        # self.fields['organizer'].queryset = Organizer.objects.filter(
        #     user__role='organiser'  # Access related CustomUser role field
        # )
