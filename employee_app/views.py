from django.shortcuts import render,redirect
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

    return render(request, "emp/emp_login.html", locals())

def emp_home(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    return render(request, "emp/emp_home.html")

def emp_profile(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    user = request.user
    employee = EmployeeDetail.objects.get(user=user)
    if request.method == "POST":
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        empcode = request.POST["empcode"]
        email = request.POST["email"]
        password = request.POST["password"]
        contact = request.POST["contact"]
        department = request.POST["department"]
        jdate = request.POST["jdate"]
        designation = request.POST["designation"]
        gender = request.POST["gender"]
        
        employee.user.first_name = firstname
        employee.user.last_name = lastname
        employee.empcode = empcode
        employee.user.email = email
        employee.contact = contact     
        employee.designation = designation
        employee.user.password = password
        employee.department = department
        
        

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

    return render(request, "emp/emp_profile.html", locals())


def emp_logout(request):
    logout(request)
    return redirect('index')
