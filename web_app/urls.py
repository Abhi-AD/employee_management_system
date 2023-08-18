from django.urls import path
from web_app.views import *



urlpatterns = [     
    path("about/", AboutView.as_view(), name="about"),
    path("job/", JobView.as_view(), name="job"),
    path("freelancer/", FreelancerView.as_view(), name="freelancer"),
]