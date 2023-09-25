from django.urls import path
from web_app.views import *
from . import views



urlpatterns = [
    path("", HomeView.as_view(), name="index"),         
    path("about/", AboutView.as_view(), name="about"),
    path("job/", JobView.as_view(), name="job"),
    path("freelancer/", FreelancerView.as_view(), name="freelancer"),
    path("apply/", jobapply, name="apply"),
    path("newsletter/", views.NewlettersView.as_view(), name = "newsletter"),
    path("job_all/", JobAllView.as_view(), name = "job_all"),
    path("expert_all/", ExpertAllView.as_view(), name = "expert_all"),
    path("job-post-search", PostSearchView.as_view(), name="job-post-search")
]