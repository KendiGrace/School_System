from django import forms
from django.db.models.base import Model
from .models import EventsRegistration

class EventsRegistrationForm(forms.ModelForm):
    class Meta:
        model=EventsRegistration
        fields="__all__"