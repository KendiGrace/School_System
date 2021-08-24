from events_calendar.models import EventsRegistration
from django.shortcuts import render
from .forms import EventsRegistrationForm
from .models import EventsRegistration
# Create your views here.


def register_events(request):
    if request.method == "POST":
        form = EventsRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form = EventsRegistrationForm()

    return render(request, "register_event.html", {"form": form})


def events_list(request):
    events_calendars = EventsRegistration.objects.all()
    return render(request, "events_list.html", {"events_calendar": events_calendars})

# Create your views here.
