from django.urls import path
from employee_app.views import *



urlpatterns = [
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
    path('employee/<int:pk>/delete/', EmployeeProfileDeleteView.as_view(), name='employee_profile_delete'),
    path("admin_emp_view_detail/<int:pk>/",admin_emp_view_detail, name="admin_emp_view_detail"),
    
    
    
    
     
]