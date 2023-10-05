from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from web_app.forms import NewsletterForm,Job_apply_Form
from django.views import View
from django.contrib.auth.models import *
from web_app.model import *
from employee_app.models import *
from datetime import timedelta
from django.utils import timezone
from django.views.generic import ListView, TemplateView, View, DetailView


# Create your views here.
       
class HomeView(ListView):
    model = JobPosting,EmployeeDetail,JobLocation
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
        
        context["locations"] = JobLocation.objects.all()       
        context["department"] = JobPosting.objects.all()       
        return context
 
 

from django.core.paginator import PageNotAnInteger, Paginator
from django.db.models import Q
from django.http import JsonResponse

class PostSearchView(View):
    template_name = "home/search.html"

    def get(self, request, *args, **kwargs):
        query = request.GET["query"]
        post_list = JobPosting.objects.filter(
            (Q(title__icontains=query))
            & Q(status="active")
            & Q(posted_at__isnull=False)
        ).order_by("-posted_at")

        # paginator start
        page = request.GET.get("page", 1)
        paginator_by = 1
        paginator = Paginator(post_list, paginator_by)
        try:
            posts = paginator.page(page)

        except PageNotAnInteger:
            posts = paginator.page(1)

        # paginations end'
        return render(
            request,
            self.template_name,
            {"page_obj": posts, "query": query},
        )

 
class JobAllView(ListView):
    model = JobPosting
    template_name = "jobs/job_all.html"
    context_object_name = "posts"
    queryset = JobPosting.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)      
        context["featured_posts"] = JobPosting.objects.filter(
            posted_at__isnull=False, status="active"
        ).order_by("-posted_at")      
        return context   
    
class ExpertAllView(ListView):
    model = EmployeeDetail
    template_name = "jobs/expert_all.html"
    context_object_name = "posts"
    queryset = EmployeeDetail.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)      
        context["expert_all"] = EmployeeDetail.objects.filter().order_by("-join_date")      
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
        form = Job_apply_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Your Job Application is successfully submitted'})
        else:
            # Handle form validation errors here if needed.
            errors = form.errors
            return JsonResponse({'message': 'Form validation failed', 'errors': errors}, status=400)

    else:
        form = Job_apply_Form()

    context = {
        'form': form,
    }

    return render(request, 'apply_form.html', context)




# def customer(request):
#     if request.method == 'POST':
#         form = CustomerForm(request.POST)
#         if form.is_valid():
#             Name = form.cleaned_data['name']
#             Address = form.cleaned_data['address']
#             City = form.cleaned_data['city']
#             Pincode = form.cleaned_data['pincode']
#             Email = form.cleaned_data['email']
#             Phone = form.cleaned_data['phone']
#             print('Name:', Name)
#             print('Full Address:', Address, City, Pincode)	
#             print('Email:', Email)
#             print('Phone:', Phone)
#     form = CustomerForm()
#     return render(request, "forms.html", {'form':form})



class NewlettersView(View):
    def post(self, request):
        is_ajax = request.headers.get('x-requested-with')
        if is_ajax == 'XMLHttpRequest':
            form = NewsletterForm(request.POST)
            if form.is_valid():
                form.save()
                return JsonResponse({"sucess":True, "message":"Sucessfully subscribed to the news letters.",},status=200,)
            else:
                return JsonResponse({"sucess":False, "message":"cannot subscribed to the news letters.",},status=404,)
        else:
            return JsonResponse({"sucess":False, "message":"SUcessfully subscribed to the news letters.",},status=400,)



