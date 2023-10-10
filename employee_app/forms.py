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
        


      
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
    
    
class EmployeeProfileForm(forms.ModelForm):
    class Meta:
        model = EmployeeDetail
        fields = '__all__'
  
  
  
from django import forms

class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    empcode = forms.IntegerField()
    username = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    image = forms.FileField() 
    

class EmployeeProfileEditForm(forms.Form):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    empcode = forms.IntegerField()
    image = forms.FileField()
    empdept = forms.CharField(max_length=255)
    designation = forms.CharField(max_length=255)
    contact = forms.IntegerField()
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    join_date = forms.DateField()
  
  
class EmployeeExperienceEditForm(forms.ModelForm):
    class Meta:
        model =  EmployeeExperience
        fields = '__all__'       