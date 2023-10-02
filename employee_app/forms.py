from django import forms
from .models import EmployeeDetail

class YourModelForm(forms.ModelForm):
    class Meta:
        model = EmployeeDetail
        fields = ['feature_image']
