from django.urls import path,include
from django.urls.resolvers import URLPattern
from rest_framework import routers, urlpatterns
from .views import StudentViewSet,TrainerViewSet,CoursesViewSet,EventViewSet
from .serializers import StudentSerializer,TrainerSerializer,CoursesSerializer

router=routers.DefaultRouter()
router.register("students/",StudentViewSet)
router.register("trainers/",TrainerViewSet)
router.register("courses/",CoursesViewSet)
router.register("events/",EventViewSet)
urlpatterns=[
    path("",include(router.urls))
]