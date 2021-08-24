
from django.urls import path
from django import urls
from django.urls.resolvers import URLPattern
from .views import register_events, events_list

urlpatterns = [
    path("register/", register_events, name="register_events"),
    path("list/", events_list, name="events_list"),

]
