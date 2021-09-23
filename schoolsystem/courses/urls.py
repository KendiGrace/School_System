
from django.urls import path
from .views import courses_list, edit_courses, register_courses,courses_profile,delete_courses

urlpatterns=[
    path("register/",register_courses,name="register_courses"),
    path("list/",courses_list,name="courses_list"),
    path("edit/<int:id>/",edit_courses,name="edit_courses"),
    path("profile/<int:id>/", courses_profile,name="courses_profile"),
    path("delete/<int:id>/", delete_courses,name="delete_courses"),
]