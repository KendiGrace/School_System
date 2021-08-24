from django.urls import path
from django import urls
from django.urls.resolvers import URLPattern
from .views import register_student, students_list
urlpatterns = [
    path("register/", register_student, name="register_student"),
    path("list/", students_list, name="students_list"),
]
