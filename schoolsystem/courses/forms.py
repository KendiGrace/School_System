from django import forms
# from django.db import models
# from django.db.models.base import Model
from.models import Courses
class CoursesRegistrationForm(forms.ModelForm):
    class Meta:
        model=Courses
        fields="__all__"