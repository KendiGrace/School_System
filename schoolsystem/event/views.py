from django.http.response import HttpResponseRedirect
from .forms import EventRegistrationForm
from django.shortcuts import redirect, render,get_object_or_404
from datetime import date, datetime
from django.shortcuts import render
from.forms import EventRegistrationForm
from django.shortcuts import render
from.models import Event
def register_event(request):
    form=EventRegistrationForm()
    return render(request,"register_event.html",{
        "form":form,
        "name":"Anastasia",
    })
def register_event(request):
    if request.method=="POST":
        form=EventRegistrationForm(request.POST,request.FILES)
from django.views import generic
from django.utils.safestring import mark_safe
from django.urls import reverse
from .models import *
from .utils import Calendar
# Create your views here.


class CalendarView(generic.ListView):
    model = Event
    template_name = 'event_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('day', None))
        event = Calendar(d.year, d.month)
        html_cal = event.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context
def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()
def event(request,event_id=None):
    instance=Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance =Event()
    form = EventRegistrationForm(instance=instance)  #init
    if request.method == "POST":
        form = EventRegistrationForm(request.POST,request.FILES)   
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('event:calendar'))
        else:
            print(form.errors)

    else:
        form=EventRegistrationForm()
    return render(request,"register_event.html",{"form":form})
def event_list(request):
    events=Event.objects.all()
    return render(request,"event_list.html",{ "events":events})
    
