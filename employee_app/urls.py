from django.urls import path
from employee_app.views import *



urlpatterns = [
    # add new  view
    path("registration/", RegistrationView.as_view(), name="registration"),
    path("employee-add/", NewEmployeeRegistrationView.as_view(), name="employee-add"),
    path("job-add/", add_job_posting, name="job-add"),
    # path('signup/', CustomUserCreateView.as_view(), name='signup'),    
    
    
    # login/logout view
    path("emp_login/", emp_login, name="emp_login"),
    path("emp_logout/", emp_logout, name="emp_logout"),
    path("admin_login/", admin_login, name="admin_login"),
    
    
    
    # show view emp
    path("emp_home/", emp_home, name="emp_home"),    
    path("emp_profile/", emp_profile, name="emp_profile"),    
    path("emp_experiences/", emp_experiences, name="emp_experiences"),
    path("emp_education/", emp_education, name="emp_education"),
    
    # show view admin
    path("admin_home/", admin_home, name="admin_home"),
    path("all_employee/",all_employee, name="all_employee"),
    path("admin_emp_view_detail/<int:pk>/",admin_emp_view_detail, name="admin_emp_view_detail"),
    path("all_job/",all_job, name="all_job"),
    path("admin_job_view_detail/<int:pk>/",admin_job_view_detail, name="admin_job_view_detail"),
    
    
    # edit emp
    path("emp_profile_edit/", emp_profile_edit, name="emp_profile_edit"),
    path("emp_edit_experiences/", emp_edit_experiences, name="emp_edit_experiences"),
    path("emp_edit_education/", emp_edit_education, name="emp_edit_education"),
    
    
    # edit admin
    # path("edit_admin_education/", edit_admin_education, name="edit_admin_education"),
    
    # change password
    path("change_password/", change_password, name="change_password"),
    path("admin_change_password/",admin_change_password, name="admin_change_password"),

    
    # delete view
    path('employee/<int:pk>/delete/', emp_profile_delete, name='employee_profile_delete'),
    path("job_posting_delete/<int:pk>/",job_post_delete, name="job_posting_delete"),
    
    
    
    
     
]