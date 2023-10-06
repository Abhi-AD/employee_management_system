from django import forms
from web_app.model import *
from django import forms


CITY_CHOICES =(
)



class NewsletterForm(forms.ModelForm):
     class Meta:
          model = Newsletter
          fields= "__all__"


class JobPostingForm(forms.ModelForm):
    class Meta:
        model = JobPosting
        fields = '__all__' 





class DateInput(forms.DateInput):
    input_type = 'date'




class Job_apply_Form(forms.ModelForm):
    class Meta:
        model = Job_apply_Application
        fields = '__all__'
        widgets = {
            "date_of_birth": DateInput,
            "city": forms.Select(choices=CITY_CHOICES),
         }
        
        
from employee_app.models import *

class EmployeeProfileForm(forms.ModelForm):
    class Meta:
        model = EmployeeDetail
        fields = '__all__'
  

class EmployeeExperienceForm(forms.ModelForm):
    class Meta:
        model = EmployeeExperience
        fields = '__all__'
        
class EmployeeEducationForm(forms.ModelForm):
    class Meta:
        model = EmployeeEducation
        fields = '__all__'
        

  
  
        
        
# class CustomerForm(forms.Form):
#     name = forms.CharField(max_length=50)
#     address = forms.CharField(max_length=150)
#     city = forms.ChoiceField(choices=CITY_CHOICES)
#     pincode = forms.IntegerField()
#     email = forms.EmailField()
#     phone = forms.IntegerField()
