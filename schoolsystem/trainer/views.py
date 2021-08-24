from django.shortcuts import render
from.models import Trainer

from.forms import TrainerRegistrationForm


def register_trainer(request):
    if request.method == "POST":
        form = TrainerRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form = TrainerRegistrationForm
    return render(request, "register-trainer.html", {"form": form})


def trainer_list(request):
    trainers = Trainer.objects.all()
    return render(request, "trainer_list.html", {"trainers": trainers})

# Create your views here.
