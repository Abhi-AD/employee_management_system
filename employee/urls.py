"""
URL configuration for employee project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from employee_app.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", IndexView.as_view(), name="index"),
    path("about/", AboutView.as_view(), name="about"),
    path("job/", JobView.as_view(), name="job"),
    path("freelancer/", FreelancerView.as_view(), name="freelancer"),
    path("registration/", RegistrationView.as_view(), name="registration"),
    path("emp_login/", emp_login, name="emp_login"),
    path("emp_home/", emp_home, name="emp_home"),
    path("emp_profile/", emp_profile, name="emp_profile"),
    path("emp_logout/", emp_logout, name="emp_logout"),
    path("admin_login/", admin_login, name="admin_login"),
    path("emp_experiences/", emp_experiences, name="emp_experiences"),
    path("emp_edit_experiences/", emp_edit_experiences, name="emp_edit_experiences"),
    path("emp_education/", emp_education, name="emp_education"),
    path("emp_edit_education/", emp_edit_education, name="emp_edit_education"),
    path("change_password/", change_password, name="change_password"),
    path("admin_home/", admin_home, name="admin_home"),
    path("admin_change_password/",admin_change_password, name="admin_change_password"),
    path("all_employee/",all_employee, name="all_employee"),
    path("emp_delete/<int:pk>/",emp_delete, name="emp_delete"),
    path("admin_emp_view_detail/<int:pk>/",admin_emp_view_detail, name="admin_emp_view_detail"),
    
    # template website
    path("about/", AboutView.as_view(), name="about")
    
    
    
    
]
