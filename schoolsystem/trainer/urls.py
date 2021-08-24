from django.urls import path
from .views import register_trainer,trainer_list

urlpatterns = [
    path("register/", register_trainer, name="register_trainer"),
    path("list/", trainer_list, name="trainer_list"),
]
