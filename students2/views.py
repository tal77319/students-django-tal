from django.shortcuts import render
from .models import Course, User
from django.contrib import messages
# Create your views here.

def home(request,methods=["POST ,GET"]):
    return render(request,"home.html")

def add_course(request):
    if request.method=='POST':
        name=request.POST["course_name"]
        description=request.POST["description"]
        course=Course(name=name, description=description)
        course.save()
        request.session["user"]="anonymous"
    return render(request, "add_course.html", {"user":request.session.get("user", "not logged in")})


def show_users(request):
    users=User.objects.all()
    return render(request, "users.html", {"users":users})




