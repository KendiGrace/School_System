
from django.urls import path
from .views import courses_list, register_courses
urlpatterns=[
    path("register/",register_courses,name="register_courses"),
    path("list/",courses_list,name="courses_list")
]