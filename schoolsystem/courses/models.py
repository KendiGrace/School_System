from django.db import models
from django.db.models.fields import CharField
from django.http import request

class Courses(models.Model):
    course_name=models.CharField(max_length=16)
    course_code=models.CharField(max_length=12)
    course_description=models.CharField(max_length=30)
    course_trainer=models.CharField(max_length=18)
    course_syllabus=models.FileField()
    course_notes=models.FileField()
    course_duration=models.DateTimeField()

def __str__(self):
    return self.course_name


# Create your models here.
