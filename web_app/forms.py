from django import forms
from web_app.model import *



CITY_CHOICES =(
    ("1", "New York"),
    ("2", "Washington"),
    ("3", "Los Angeles"),
    ("4", "Houston"),
    ("5", "Las Vegas"),
)

class CustomerForm(forms.Form):
    name = forms.CharField(max_length=50)
    address = forms.CharField(max_length=150)
    city = forms.ChoiceField(choices=CITY_CHOICES)
    pincode = forms.IntegerField()
    email = forms.EmailField()
    phone = forms.IntegerField()

select_gender = (
    ("male", "Male"),
    ("female", "Female"),
    ("other", "Other"),
)

class DateInput(forms.DateInput):
    input_type = 'date'

select_city = (
    ("Kathmandu", "ktm"),
    ("Pokhara", "pokhara"),
    ("houston", "Houston"),
    ("chicago", "Chicago"),
    ("phoenix", "Phoenix"),
    ("austin", "Austin"),
    ("boston", "Boston"),
    ("las vegas", "Las Vegas"),
    ("columbia", "Columbia"),
    ("waco", "Waco"),
)

select_state = (
    ("new york", "New York"),
    ("california", "California"),
    ("iiiinois", "IIIinois"),
    ("texas", "Texas"),
    ("arizona", "Arizona"),
    ("massachusetts", "Massachusetts"),
    ("nevada", "Nevada"),
    ("south carolina", "South Carolina"),   
)


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = '__all__'
        widgets = {
            "gender": forms.RadioSelect(choices=select_gender),
            "date_of_birth": DateInput,
            "city": forms.Select(choices=select_city),
            "state": forms.Select(choices=select_state),
        }