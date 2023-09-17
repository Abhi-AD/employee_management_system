from django.urls import path
from web_app.views import *
from . import views



urlpatterns = [
    path("", HomeView.as_view(), name="index"),         
    path("about/", AboutView.as_view(), name="about"),
    path("job/", JobView.as_view(), name="job"),
    path("freelancer/", FreelancerView.as_view(), name="freelancer"),
    path("apply/", jobapply, name="apply"),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('success/', views.success, name='success'),
]