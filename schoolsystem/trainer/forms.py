from django import forms
from django.db.models.base import Model
from.models import Trainer


class TrainerRegistrationForm(forms.ModelForm):
    class Meta:
        model= Trainer
        fields = "__all__"
