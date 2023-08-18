from django.shortcuts import render
from django.views import View


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