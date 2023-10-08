# from django.contrib.auth.models import User
# from django import forms
# from django.contrib.auth.forms import UserCreationForm


# class SignUpForm(UserCreationForm):
#     password2 = forms.CharField(
#         label="Confirm Password (again)", widget=forms.PasswordInput
#     )

#     class Meta:
#         model = User
#         fields = ["username", "first_name", "last_name", "email"]
#         labels = {"email": "Email"}






from django import forms
from employee_app.models import *



class EmployeeExperienceForm(forms.ModelForm):
    class Meta:
        model = EmployeeExperience
        fields = '__all__'
        
class EmployeeEducationForm(forms.ModelForm):
    class Meta:
        model = EmployeeEducation
        fields = '__all__'
        
        
class EmployeeProfileEditForm(forms.ModelForm):
    class Meta:
        model = EmployeeDetail
        fields = ['empcode', 'empdept', 'designation', 'contact', 'gender', 'join_date']
        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
    
    
class EmployeeProfileForm(forms.ModelForm):
    class Meta:
        model = EmployeeDetail
        fields = '__all__'
  