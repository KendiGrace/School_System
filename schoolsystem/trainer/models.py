from django.db import models
from django.http import request

class Trainer(models.Model):
    image=models.ImageField(upload_to="images")
    first_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=12)
    email = models.EmailField()
    company = models.CharField(max_length=20)
    profession = models.CharField(max_length=20)
    courses = models.CharField(max_length=20)
    id_number = models.CharField(max_length=12)
    bank_account = models.CharField(max_length=16)
    resume = models.FileField()
    country = models.CharField(max_length=12)
    salary = models.PositiveBigIntegerField()
    # Lessons = models.PositiveSmallIntegerField()
    gender = ((u'M', u'Male'), (u'F', u'Female'), (u'O', u'Other'))
    gender = models.CharField(max_length=1, choices=gender)

    def __str__(self):
        return self.first_name


# Create your models here.
