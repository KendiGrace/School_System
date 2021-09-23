from django.db import models

# Create your models here.
class Event(models.Model):
    event_name=models.CharField(max_length=12,null=True)
    event_date=models.DateField(null=True)
    event_planner=models.CharField(max_length=12,null=True)
    event_duration=models.CharField(max_length=12,null=True)
    event_participant=models.PositiveSmallIntegerField(null=True)
    event_approved_by=models.CharField(max_length=13,null=True)
    event_id=models.CharField(max_length=13,null=True)

    title=models.CharField(max_length=100)
    description=models.TextField()
    start_time=models.DateField()
    end_time=models.DateField()


