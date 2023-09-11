from django.shortcuts import render,HttpResponse
from web_app.forms import CustomerForm,ResumeForm
from django.views import View
from django.contrib.auth.models import *
from web_app.model import *
from employee_app.models import *
from datetime import timedelta
from django.utils import timezone
from django.views.generic import ListView, TemplateView, View, DetailView



# Create your views here.
class HomeView(ListView):
    model = JobPosting,EmployeeDetail
    template_name = "index.html"
    context_object_name = "posts"
    queryset = JobPosting.objects.filter(
        posted_at__isnull=False, status="active"
    ).order_by("-posted_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recent_posts"] = JobPosting.objects.filter(
            posted_at__isnull=False, status="active"
        ).order_by("-posted_at")[:4]
        context["featured_posts"] = JobPosting.objects.filter(
            posted_at__isnull=False, status="active"
        ).order_by("-posted_at")[:2]
        context["freelancer_posts"] = EmployeeDetail.objects.filter(
        ).order_by("-join_date")[:3]
        return context
    
class AboutView(TemplateView):
     template_name = "jobs/about.html"
    
class JobView(TemplateView):
    model = JobPosting
    template_name =  "jobs/job.html"
    queryset = JobPosting.objects.filter(
        posted_at__isnull=False, status="active"
    ).order_by("-posted_at")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recent_posts"] = JobPosting.objects.filter(
            posted_at__isnull=False, status="active"
        ).order_by("-posted_at")[:4]
        context["featured_posts"] = JobPosting.objects.filter(
            posted_at__isnull=False, status="active"
        ).order_by("-posted_at")[:2]
        return context
    
class FreelancerView(ListView):
    model = EmployeeDetail
    template_name = "jobs/freelancer.html"
    queryset = EmployeeDetail.objects.filter(
    ).order_by("-join_date")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["freelancer_posts"] = EmployeeDetail.objects.filter(
        ).order_by("-join_date")[:3]
        return context



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





