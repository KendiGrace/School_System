from . import views
from django import urls
from django.conf.urls import url
from django.urls import path
from .views import register_event, event_list


urlpatterns = [
    path('register', register_event, name='register_event'),
    path('list/', event_list, name="event_list"),

    path('calendar/', views.CalendarView.as_view(), name="calendar"),
    path('register/', views.event, name='event_list'),
]
