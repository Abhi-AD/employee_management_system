from django import forms
from web_app.model import *
from django import forms
from web_app.model import Subscriber

class NewsletterForm(forms.ModelForm):
     class Meta:
          model = Subscriber
          fields= "__all__"


CITY_CHOICES =(
    ("0","Select Provinces"),
    ("1", "Koshi"),
    ("2", "Madhesh"),
    ("3", "Bagmati"),
    ("4", "Gandaki"),
    ("5", "Lumbini"),
    ("6", "Karnali"),
    ("7", "Sudurpashchim"),
)

class CustomerForm(forms.Form):
    name = forms.CharField(max_length=50)
    address = forms.CharField(max_length=150)
    city = forms.ChoiceField(choices=CITY_CHOICES)
    pincode = forms.IntegerField()
    email = forms.EmailField()
    phone = forms.IntegerField()

select_gender = (
    ("select gender","Select gender"),
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


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = '__all__'
        widgets = {
            "gender": forms.Select(choices=select_gender),
            "date_of_birth": DateInput,
            "city": forms.Select(choices=CITY_CHOICES),
            "state": forms.Select(choices=select_state),
        }