from courses .models import Courses
from django.shortcuts import render,redirect
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

def edit_courses(request,id):
    courses=Courses.objects.get(id=id)
    if request.method=='POST':
        form=CoursesRegistrationForm(request.POST,instance=courses)
        if form.is_valid():
            form.save()
    else:
        form=CoursesRegistrationForm(instance=courses)
        return render(request,"edit_courses.html", {"form":form})
def courses_profile(request,id):
    courses=Courses.objects.get(id=id)
    return render(request,"courses_profile.html",{"courses": courses})
    
def delete_courses(request,id):
    courses=Courses.objects.get(id=id)
    courses.delete()
    return redirect("courses_list")

# Create your views here.
