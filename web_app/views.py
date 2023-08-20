from django.shortcuts import render,HttpResponse
from web_app.forms import CustomerForm
from django.views import View
from django.contrib.auth.models import *
from web_app.model import *


# Create your views here.
class AboutView(View):
    def get(self, request):
        return render(request, "jobs/about.html")
    
class JobView(View):
    def get(self, request):
        return render(request, "jobs/job.html")
    
class FreelancerView(View):
    def get(self, request):
        return render(request, "jobs/freelancer.html")



def customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            Name = form.cleaned_data['name']
            Address = form.cleaned_data['address']
            City = form.cleaned_data['city']
            Pincode = form.cleaned_data['pincode']
            Email = form.cleaned_data['email']
            Phone = form.cleaned_data['phone']
            print('Name:', Name)
            print('Full Address:', Address, City, Pincode)	
            print('Email:', Email)
            print('Phone:', Phone)
    form = CustomerForm()
    return render(request, "forms.html", {'form':form})





from .forms import ResumeForm

# Create your views here.

def jobapply(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Your Job Application is successfully submitted')
    else:
        form = ResumeForm()
        context = {
            'form':form,
        }
    return render(request, 'apply_form.html', context)