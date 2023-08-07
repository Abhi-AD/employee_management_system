from django.shortcuts import render, redirect
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
            EmployeeExperience.objects.create(user=user)
            EmployeeEducation.objects.create(user=user)
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
        return redirect("emp_login")
    return render(request, "emp/emp_home.html")


def emp_profile(request):
    if not request.user.is_authenticated:
        return redirect("emp_login")
    error = ""
    user = request.user
    employee = EmployeeDetail.objects.get(user=user)
    if request.method == "POST":
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        empcode = request.POST["empcode"]
        department = request.POST["department"]
        designation = request.POST["designation"]
        gender = request.POST["gender"]
        contact = request.POST["contact"]
        jdate = request.POST["jdate"]

        employee.user.first_name = firstname
        employee.user.last_name = lastname
        employee.empcode = empcode
        employee.contact = contact
        employee.designation = designation
        employee.empdept = department
        employee.gender = gender

        if jdate:
            employee.join_date = jdate

        try:
            employee.save()
            employee.user.save()
            error = "no"
        except:
            error = "yes"

    return render(request, "emp/emp_profile.html", locals())


def emp_logout(request):
    logout(request)
    return redirect("index")


def admin_login(request):
    return render(request, "admin/admin_login.html")


def emp_experiences(request):
    if not request.user.is_authenticated:
        return redirect("emp_login")
    user = request.user
    experience = EmployeeExperience.objects.get(user=user)
    return render(request, "emp/emp_details/emp_experience.html", locals())


def emp_edit_experiences(request):
    if not request.user.is_authenticated:
        return redirect("emp_login")
    error = ""
    user = request.user
    experience = EmployeeExperience.objects.get(user=user)

    if request.method == "POST":
        first_comany_name = request.POST["first_comany_name"]
        first_comany_designation = request.POST["first_comany_designation"]
        first_comany_duration = request.POST["first_comany_duration"]
        first_comany_salary = request.POST["first_comany_salary"]

        second_comany_name = request.POST["second_comany_name"]
        second_comany_designation = request.POST["second_comany_designation"]
        second_comany_duration = request.POST["second_comany_duration"]
        second_comany_salary = request.POST["second_comany_salary"]

        third_comany_name = request.POST["third_comany_name"]
        third_comany_designation = request.POST["third_comany_designation"]
        third_comany_duration = request.POST["third_comany_duration"]
        third_comany_salary = request.POST["third_comany_salary"]


        experience.first_comany_name = first_comany_name
        experience.first_comany_designation = first_comany_designation
        experience.first_comany_duration = first_comany_duration
        experience.first_comany_salary = first_comany_salary   
             
        experience.second_comany_name = second_comany_name
        experience.second_comany_designation = second_comany_designation
        experience.second_comany_duration = second_comany_duration
        experience.second_comany_salary = second_comany_salary   
             
        experience.third_comany_name =third_comany_name
        experience.third_comany_designation = third_comany_designation
        experience.third_comany_duration = third_comany_duration
        experience.third_comany_salary = third_comany_salary


        try:
            experience.save()
            error = "no"
        except:
            error = "yes"
    return render(request, "emp/emp_details/emp_experience_update.html", locals())
