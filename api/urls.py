from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'joblocation', views.JobLocationViewSet)
router.register(r'jobcategory', views.JobCategoryViewSet)
router.register(r'jobposting', views.JobPostingViewSet)
router.register(r'resume', views.ResumeViewSet)
router.register(r'newsletter', views.NewsletterViewSet)
router.register(r'emp-detail', views.EmployeeDetailViewSet)
router.register(r'emp-education', views.EmployeeEducationViewSet)
router.register(r'emp-experience', views.EmployeeExperienceViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]