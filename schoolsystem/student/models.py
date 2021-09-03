from django.db import models
from django.forms.fields import CharField
from django.forms.widgets import NumberInput
from django.http import response
# Create your models here.


class Student(models.Model):
    # image = models.ImageField(upload_to="images")
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    age = models.PositiveSmallIntegerField()
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=13)
    email = models.EmailField()
    national_id = models.CharField(max_length=12)
    country = models.CharField(max_length=12, default="Valid")
    gender = ((u'M', u'Male'),
              (u'F', u'Female'),
              (u'O', u'Others'),)
    gender = models.CharField(max_length=1, choices=gender)
    guardian = models.CharField(max_length=18)
    class_name = models.CharField(max_length=10)
    room = models.CharField(max_length=8)
    big_sister = models.CharField(max_length=18, default="Valid")
    mentors_name = models.CharField(max_length=18)
    laptop_number = models.PositiveSmallIntegerField()
    # medical_report=models.FileField()
    # device_number=models.ForeignKey('device_number',on_delete=models.CASCADE)

    # null used when we don't know the number/something


def __str__(self):  # List first names only.
    return self.first_name
