
from django.db import models
from django.forms import fields
from rest_framework import serializers
from student.models import Student
from trainer.models import Trainer
from courses.models import Courses
from event.models import Event


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        models=Student
        fields=("first_name","last_name","age")

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        models=Trainer
        fields=("first_name","last_name","phone_number")

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        models=Courses
        fields=("course_name","course_description","course_trainer")

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        models=Event
        fields=("event_name","event_date","event_planner")