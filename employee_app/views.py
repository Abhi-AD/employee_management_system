from django.shortcuts import render, redirect, get_object_or_404
from employee_app.models import *
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.views import View
from django.contrib import messages


# Create your views here.



class RegistrationView(View):
    template_name = "registration.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        error = ""
        if request.method == "POST":
            firstname = request.POST.get("firstname")
            lastname = request.POST.get("lastname")
            empcode = request.POST.get("empcode")
            email = request.POST.get("email")
            password = request.POST.get("password")

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

        return render(request, self.template_name, {"error": error})


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
        first_comany_years = request.POST["first_comany_years"]

        second_comany_name = request.POST["second_comany_name"]
        second_comany_designation = request.POST["second_comany_designation"]
        second_comany_duration = request.POST["second_comany_duration"]
        second_comany_years = request.POST["second_comany_years"]

        third_comany_name = request.POST["third_comany_name"]
        third_comany_designation = request.POST["third_comany_designation"]
        third_comany_duration = request.POST["third_comany_duration"]
        third_comany_years = request.POST["third_comany_years"]

        experience.first_comany_name = first_comany_name
        experience.first_comany_designation = first_comany_designation
        experience.first_comany_duration = first_comany_duration
        experience.first_comany_years = first_comany_years

        experience.second_comany_name = second_comany_name
        experience.second_comany_designation = second_comany_designation
        experience.second_comany_duration = second_comany_duration
        experience.second_comany_years = second_comany_years

        experience.third_comany_name = third_comany_name
        experience.third_comany_designation = third_comany_designation
        experience.third_comany_duration = third_comany_duration
        experience.third_comany_years = third_comany_years

        try:
            experience.save()
            error = "no"
        except:
            error = "yes"
    return render(request, "emp/emp_details/emp_experience_update.html", locals())


def emp_education(request):
    if not request.user.is_authenticated:
        return redirect("emp_login")
    user = request.user
    education = EmployeeEducation.objects.get(user=user)
    return render(request, "emp/emp_details/emp_education.html", locals())


from django.core.exceptions import ObjectDoesNotExist


def emp_edit_education(request):
    if not request.user.is_authenticated:
        return redirect("emp_login")
    error = ""
    user = request.user
    try:
        education = EmployeeEducation.objects.get(user=user)
    except ObjectDoesNotExist:
        education = EmployeeEducation(user=user)

    if request.method == "POST":
        coursepg = request.POST["coursepg"]
        schoolpg = request.POST["schoolpg"]
        yearofpassingpg = request.POST["yearofpassingpg"]
        percentagepg = request.POST["percentagepg"]

        coursegra = request.POST["coursegra"]
        schoolgra = request.POST["schoolgra"]
        yearofpassinggra = request.POST["yearofpassinggra"]
        percentagegra = request.POST["percentagegra"]

        coursessc = request.POST["coursessc"]
        schoolssc = request.POST["schoolssc"]
        yearofpassingssc = request.POST["yearofpassingssc"]
        percentagessc = request.POST["percentagessc"]

        coursehsc = request.POST["coursehsc"]
        schoolhsc = request.POST["schoolhsc"]
        yearofpassinghsc = request.POST["yearofpassinghsc"]
        percentagehsc = request.POST["percentagehsc"]

        education.coursepg = coursepg
        education.schoolpg = schoolpg
        education.yearofpassingpg = yearofpassingpg
        education.percentagepg = percentagepg

        education.coursegra = coursegra
        education.schoolgra = schoolgra
        education.yearofpassinggra = yearofpassinggra
        education.percentagegra = percentagegra

        education.coursessc = coursessc
        education.schoolssc = schoolssc
        education.yearofpassingssc = yearofpassingssc
        education.percentagessc = percentagessc

        education.coursehsc = coursehsc
        education.schoolhsc = schoolhsc
        education.yearofpassinghsc = yearofpassinghsc
        education.percentagehsc = percentagehsc

        try:
            education.save()
            error = "no"
        except:
            error = "yes"
    return render(request, "emp/emp_details/emp_education_update.html", locals())


def change_password(request):
    if not request.user.is_authenticated:
        return redirect("emp_login")
    error = ""
    user = request.user
    if request.method == "POST":
        currentpassword = request.POST["currentpassword"]
        newpassword = request.POST["newpassword"]

        try:
            if user.check_password(currentpassword):
                user.set_password(newpassword)
                user.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"
    return render(request, "emp/emp_change_password.html", locals())


def admin_login(request):
    error = ""
    if request.method == "POST":
        username1 = request.POST["username"]
        pass1 = request.POST["password"]
        user = authenticate(username=username1, password=pass1)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"

    return render(request, "admin/admin_login.html", locals())


def admin_home(request):
    # user = request.user
    if not request.user.is_superuser:
        return redirect("admin_login")
    return render(request, "admin/admin_home.html")


def admin_change_password(request):
    if not request.user.is_superuser:
        return redirect("admin_login")
    error = ""
    user = request.user
    if request.method == "POST":
        currentpassword = request.POST["currentpassword"]
        newpassword = request.POST["newpassword"]

        try:
            if user.check_password(currentpassword):
                user.set_password(newpassword)
                user.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"
    return render(request, "admin/admin_change_password.html", locals())


def all_employee(request):
    if not request.user.is_superuser:
        return redirect("admin_login")
    employee = EmployeeDetail.objects.all()
    return render(request, "admin/all_employee.html", locals())


def edit_admin_education(request):
    if not request.user.is_authenticated:
        return redirect("emp_login")
    error = ""
    user = request.user
    try:
        education = EmployeeEducation.objects.get(user=user)
    except ObjectDoesNotExist:
        education = EmployeeEducation(user=user)

    if request.method == "POST":
        coursepg = request.POST["coursepg"]
        schoolpg = request.POST["schoolpg"]
        yearofpassingpg = request.POST["yearofpassingpg"]
        percentagepg = request.POST["percentagepg"]

        coursegra = request.POST["coursegra"]
        schoolgra = request.POST["schoolgra"]
        yearofpassinggra = request.POST["yearofpassinggra"]
        percentagegra = request.POST["percentagegra"]

        coursessc = request.POST["coursessc"]
        schoolssc = request.POST["schoolssc"]
        yearofpassingssc = request.POST["yearofpassingssc"]
        percentagessc = request.POST["percentagessc"]

        coursehsc = request.POST["coursehsc"]
        schoolhsc = request.POST["schoolhsc"]
        yearofpassinghsc = request.POST["yearofpassinghsc"]
        percentagehsc = request.POST["percentagehsc"]

        education.coursepg = coursepg
        education.schoolpg = schoolpg
        education.yearofpassingpg = yearofpassingpg
        education.percentagepg = percentagepg

        education.coursegra = coursegra
        education.schoolgra = schoolgra
        education.yearofpassinggra = yearofpassinggra
        education.percentagegra = percentagegra

        education.coursessc = coursessc
        education.schoolssc = schoolssc
        education.yearofpassingssc = yearofpassingssc
        education.percentagessc = percentagessc

        education.coursehsc = coursehsc
        education.schoolhsc = schoolhsc
        education.yearofpassinghsc = yearofpassinghsc
        education.percentagehsc = percentagehsc

        try:
            education.save()
            error = "no"
        except:
            error = "yes"
    return render(request, "admin/admin_education_update.html", locals())



from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

class EmployeeProfileDeleteView(DeleteView):
    model = EmployeeDetail
    template_name = 'employee_profile_confirm_delete.html'
    success_url = reverse_lazy('employee_profile_list') 

def admin_emp_view_detail(request, pk):
    if not request.user.is_superuser:
        return redirect("admin_login")
    employee = EmployeeDetail.objects.get(id=pk)
    return render(request, "admin/emp_profile_view.html", {"employee": employee})
