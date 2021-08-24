from django.db import models
# Create your models here.
from django.http import response
from django.forms.fields import CharField
from django.forms.widgets import NumberInput

class EventsRegistration(models.Model):
    event_name=models.CharField(max_length=10)
    event_date=models.DateTimeField()
    event_organizer=models.CharField(max_length=10)
    event_agenda=models.CharField(max_length=14)
    event_duration=models.TimeField()
    event_venue=models.CharField(max_length=14)
    event_attendees=models.CharField(max_length=30)
    
def __str__(self):
    return self.event_name
