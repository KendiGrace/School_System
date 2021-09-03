from django.conf.urls import url
from .import views
app_name = 'event'
urlpatterns = [
    # url(r'index/', views.index, name='index'),
    url(r'calendar', views.CalendarView.as_view(), name='calendar'),
    url(r'eventform', views.event, name='event_list'),
]