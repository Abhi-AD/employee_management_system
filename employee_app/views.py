from django.shortcuts import render
from .models import *
from django.contrib.auth import login, logout, authenticate


# Create your views here.


def index(request):
    return render(request, "index.html")


def registration(request):
    error = ""
    if request.method == "POST":
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        empcode = request.POST["empcode"]
        email = request.POST["email"]
        password = request.POST["password"]

        try:
            user = User.objects.create_user(
                first_name=firstname,
                last_name=lastname,
                username=email,
                password=password,
            )
            EmployeeDetail.objects.create(user=user, empcode=empcode)
            error = "no"
        except:
            error = "yes"

    return render(request, "registration.html", locals())


def emp_login(request):
    error = ""
    if request.method == "POST":
        username1 = request.POST["emailid"]
        pass1 = request.POST["password"]
        user = authenticate(username=username1, password=pass1)
        if user:
            login(request, user)
            error = "no"
        else:
            error = "yes"

    return render(request, "emp_login.html", locals())


def emp_home(request):
    return render(request, "emp_home.html")
