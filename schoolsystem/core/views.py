from student.models import Student
from courses.models import Courses
from trainer.models import Trainer
from django.shortcuts import render

def home(request):
    students = Student.objects.count()
    trainers = Trainer.objects.count()
    courses = Courses.objects.count()
    data = {"students": students, "trainers": trainers, "courses": courses}
    return render(request, "home.html", data)
# Create your views here.
