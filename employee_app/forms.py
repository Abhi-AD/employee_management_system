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

class RegistrationForm(forms.Form):
    class Meta:
        model = EmployeeDetail
        fields = '__all__  '