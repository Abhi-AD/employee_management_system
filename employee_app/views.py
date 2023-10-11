from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from employee_app.models import *
from web_app.model import *
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.views import View
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from web_app.forms import *
from employee_app.forms import *
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

# Create your views here.


# add new  view

# without the forms

# class RegistrationView(View):
#     template_name = "registration.html"

#     def get(self, request):
#         return render(request, self.template_name)

#     def post(self, request):
#         error = ""
#         if request.method == "POST":

#             firstname = request.POST.get("firstname")
#             lastname = request.POST.get("lastname")
#             empcode = request.POST.get("empcode")
#             email = request.POST.get("email")
#             password = request.POST.get("password")
#             feature_image = request.FILES.get("feature_image")

#             try:
#                 user = User.objects.create_user(
#                     first_name=firstname,
#                     last_name=lastname,
#                     username=email,
#                     password=password,
#                 )


#                 EmployeeDetail.objects.create(
#                     user=user, empcode=empcode, feature_image=feature_image
#                 )
#                 EmployeeExperience.objects.create(user=user)
#                 EmployeeDetail.objects.create(user=user)
#                 error = "no"
#             except:
#                 error = "yes"

#         return render(request, self.template_name, {"error": error})

# class NewEmployeeRegistrationView(View):
#     template_name = "admin/registration.html"

#     def get(self, request):
#         return render(request, self.template_name)

#     def post(self, request):
#         error = ""
#         if request.method == "POST":
#             firstname = request.POST.get("firstname")
#             lastname = request.POST.get("lastname")
#             empcode = request.POST.get("empcode")
#             email = request.POST.get("email")
#             password = request.POST.get("password")
#             feature_image = request.FILES.get("feature_image")

#             try:
#                 user = User.objects.create_user(
#                     first_name=firstname,
#                     last_name=lastname,
#                     username=email,
#                     password=password,
#                 )
#                 EmployeeDetail.objects.create(
#                     user=user, empcode=empcode, feature_image=feature_image
#                 )
#                 EmployeeExperience.objects.create(user=user)
#                 EmployeeDetail.objects.create(user=user)
#                 error = "no"
#             except:
#                 error = "yes"

#         return render(request, self.template_name, {"error": error})


# using the forms

class RegistrationView(FormView):
    template_name = "user_registation.html"
    form_class = RegistrationForm
    success_url = reverse_lazy("emp_login")  # Replace with the actual login URL

    def form_valid(self, form):
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
            # Get data from the form
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            empcode = form.cleaned_data["empcode"]
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            image = form.cleaned_data["image"]

            try:
                # Create a new user
                user = User.objects.create_user(
                    username=username,
                    password=password,
                    first_name=first_name,
                    last_name=last_name,
                )

                # Create related EmployeeDetail instance
                EmployeeDetail.objects.create(
                    user=user, empcode=empcode, feature_image=image
                )

                # Create related EmployeeExperience and EmployeeDetail instances
                EmployeeExperience.objects.create(user=user)
                EmployeeDetail.objects.create(user=user)

                return super().form_valid(form)
            except Exception as e:
                # Handle any errors here
                # You can add error messages to the form or use a different approach to display errors
                form.add_error(None, "An error occurred during registration.")
                return self.form_invalid(form)
        else:
            return self.form_invalid(form)

class NewEmployeeRegistrationView(FormView):
    template_name = "admin/user_registation.html"
    form_class = RegistrationForm
    success_url = reverse_lazy("all_employee")  # Replace with the actual login URL

    def form_valid(self, form):
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
            # Get data from the form
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            empcode = form.cleaned_data["empcode"]
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            image = form.cleaned_data["image"]

            try:
                # Create a new user
                user = User.objects.create_user(
                    username=username,
                    password=password,
                    first_name=first_name,
                    last_name=last_name,
                )

                # Create related EmployeeDetail instance
                EmployeeDetail.objects.create(
                    user=user, empcode=empcode, feature_image=image
                )

                # Create related EmployeeExperience and EmployeeDetail instances
                EmployeeExperience.objects.create(user=user)
                EmployeeDetail.objects.create(user=user)

                return super().form_valid(form)
            except Exception as e:
                # Handle any errors here
                # You can add error messages to the form or use a different approach to display errors
                form.add_error(None, "An error occurred during registration.")
                return self.form_invalid(form)
        else:
            return self.form_invalid(form)




def add_job_posting(request):
    if request.method == "POST":
        form = JobPostingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(
                "all_job"
            )  # Redirect to a job list page after successful submission
    else:
        form = JobPostingForm()

    return render(request, "admin/job_add.html", {"form": form})



























# login/logout view


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


def emp_logout(request):
    logout(request)
    return redirect("index")


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






# show view emp


def emp_home(request):
    if not request.user.is_authenticated:
        return redirect("emp_login")
    return render(request, "emp/emp_home.html")


def emp_profile(request):
    if not request.user.is_authenticated:
        return redirect("emp_login")

    user = request.user
    employee = EmployeeDetail.objects.get(user=user)
    error = ""

    if request.method == "POST":
        form = EmployeeProfileForm(request.POST, request.FILES, instance=employee)

        if form.is_valid():
            form.save()
            error = "no"
        else:
            error = "yes"
    else:
        form = EmployeeProfileForm(instance=employee)

    return render(request, "emp/emp_profile.html", {"form": form, "error": error})


def emp_experiences(request):
    if not request.user.is_authenticated:
        return redirect("emp_login")

    user = request.user

    try:
        experience = EmployeeExperience.objects.get(user=user)
    except EmployeeExperience.DoesNotExist:
        experience = None

    if request.method == "POST":
        form = EmployeeExperienceForm(request.POST, instance=experience)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.user = user
            experience.save()
    else:
        form = EmployeeExperienceForm(instance=experience)

    return render(request, "emp/emp_details/emp_experience.html", {"form": form})


def emp_education(request):
    if not request.user.is_authenticated:
        return redirect("emp_login")

    user = request.user
    try:
        education = EmployeeDetail.objects.get(user=user)
    except EmployeeDetail.DoesNotExist:
        education = None

    if request.method == "POST":
        form = EmployeeEducationForm(request.POST, instance=education)
        if form.is_valid():
            education = form.save(commit=False)
            education.user = user
            education.save()
    else:
        form = EmployeeEducationForm(instance=education)

    return render(request, "emp/emp_details/emp_education.html", {"form": form})


# show view admin


def admin_home(request):
    # user = request.user
    if not request.user.is_superuser:
        return redirect("admin_login")
    return render(request, "admin/admin_home.html")


def all_employee(request):
    if not request.user.is_superuser:
        return redirect("admin_login")
    employee = EmployeeDetail.objects.all()
    return render(request, "admin/all_employee.html", locals())


def admin_emp_view_detail(request, pk):
    if not request.user.is_superuser:
        return redirect("admin_login")
    employee = EmployeeDetail.objects.get(id=pk)
    return render(request, "admin/emp_profile_view.html", {"employee": employee})


def all_job(request):
    if not request.user.is_superuser:
        return redirect("admin_login")
    employee = JobPosting.objects.all()
    return render(request, "admin/all_job.html", locals())


def admin_job_view_detail(request, pk):
    if not request.user.is_superuser:
        return redirect("admin_login")
    employee = JobPosting.objects.get(id=pk)
    return render(request, "admin/job_profile_view.html", {"employee": employee})





# edit view


# with out forms

def emp_profile_edit(request):
    if not request.user.is_authenticated:
        return redirect("emp_login")
    error = ""
    user = request.user
    employee = EmployeeDetail.objects.get(user=user)
    if request.method == "POST":
        firstname = request.POST["first_name"]
        lastname = request.POST["last_name"]
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

    return render(request, "emp/emp_profile_edit.html", locals())



# def emp_profile_edit(request):
#     if not request.user.is_authenticated:
#         return redirect("emp_login")

#     user = request.user
#     education = EmployeeDetail.objects.get(user=user)

#     if request.method == "POST":
#         form = EmployeeProfileEditForm(request.GET, instance=education)
#         if form.is_valid():
#             print("Sucess update")
#             messages.success(request, "Sucess")
#             form.save()
#             return redirect("emp_experiences")
#         else:
#             print("Failed update")
#             messages.error(request, "failed")
#             return render(
#                 request, "emp/emp_details/emp_profile_edit1.html", {"form": form}
#             )
#     else:
#         form = EmployeeProfileEditForm(instance=education)

#         return render(
#             request, "emp/emp_details/emp_education_update.html", {"form": form}
#         )







# using the forms
# def emp_profile_edit(request):
#     # Check if the user is authenticated
#     if not request.user.is_authenticated:
#         return redirect("emp_login")

#     user = request.user
#     employee = EmployeeDetail.objects.get(user=user, instance = employee)

#     if request.method == "POST":
#         form = EmployeeProfileEditForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Success")
#             return redirect("emp_experiences")
#         else:
#             messages.error(request, "Failed to update. Please check the form.")
#     else:
#         form = EmployeeProfileEditForm()

#     return render(request, "emp/emp_profile_edit1.html", {"employee":employee})









# with out forms

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



# using the forms

# def emp_edit_experiences(request):
#     if not request.user.is_authenticated:
#         return redirect("emp_login")

#     user = request.user
#     experience = EmployeeExperience.objects.get(user=user)

#     if request.method == "POST":
#         form = EmployeeExperienceEditForm(request.POST, instance=experience)
#         if form.is_valid():
#             print("vdshsddsf")
#             messages.success(request, "Sucess")
#             form.save()
#             return redirect("emp_profile")
#         else:
#             print("failed")
#             messages.error(request, "failed")
#             return render(
#                 request, "emp/emp_details/emp_experience_update.html", {"form": form}
#             )
#     else:
#         form = EmployeeExperienceForm(instance=experience)

#         return render(
#             request, "emp/emp_details/emp_experience_update.html", {"form": form}
#         )




# without forms
def emp_edit_education(request):
    if not request.user.is_authenticated:
        return redirect("emp_login")
    error = ""
    user = request.user
    try:
        education = EmployeeDetail.objects.get(user=user)
    except ObjectDoesNotExist:
        education = EmployeeDetail(user=user)

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





# using the forms
# def emp_edit_education(request):
#     if not request.user.is_authenticated:
#         return redirect("emp_login")

#     user = request.user
#     education = EmployeeDetail.objects.get(user=user)

#     if request.method == "POST":
#         form = EmployeeProfileEditForm(request.GET, instance=education)
#         if form.is_valid():
#             print("Sucess update")
#             messages.success(request, "Sucess")
#             form.save()
#             return redirect("emp_experiences")
#         else:
#             print("Failed update")
#             messages.error(request, "failed")
#             return render(
#                 request, "emp/emp_details/emp_education_update.html", {"form": form}
#             )
#     else:
#         form = EmployeeProfileEditForm(instance=education)

#         return render(
#             request, "emp/emp_details/emp_education_update.html", {"form": form}
#         )










# change password


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


# delete view
def emp_profile_delete(request, pk):
    if not request.user.is_superuser:
        return redirect("admin_login")
    try:
        post = EmployeeDetail.objects.get(pk=pk)
        post.delete()
        return HttpResponse("User deleted successfully", status=200)
    except Exception as e:
        # Handle exceptions or errors
        return HttpResponse("An error occurred", status=500)


def job_post_delete(request, pk):
    if not request.user.is_superuser:
        return redirect("admin_login")
    try:
        post = JobPosting.objects.get(pk=pk)
        post.delete()
        return HttpResponse("Post deleted successfully", status=200)
    except Exception as e:
        # Handle exceptions or errors
        return HttpResponse("An error occurred", status=500)
