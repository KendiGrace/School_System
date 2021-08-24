from courses .models import Courses
from django.shortcuts import render
from .forms import CoursesRegistrationForm
from courses.models import Courses
# Create your views here.


def register_courses(request):
    if request.method == "POST":
        form = CoursesRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = CoursesRegistrationForm()
        print(form.errors)
    return render(request, "register-course.html", {"form": form})


def courses_list(request):
    courses = Courses.objects.all()
    return render(request, "courses_list.html", {"courses": courses})

# Create your views here.
