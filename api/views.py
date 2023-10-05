from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import *
from employee_app.models import *
from web_app.model import *

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class JobLocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows JobLocations to be viewed or edited.
    """
    queryset = JobLocation.objects.all()
    serializer_class = JobLocationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [permissions.AllowAny()]
        return super().get_permissions()

    


class JobCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows JobCategorys to be viewed or edited.
    """
    queryset = JobCategory.objects.all()
    serializer_class = JobCategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [permissions.AllowAny()]
        return super().get_permissions()



class JobPostingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows JobPostings to be viewed or edited.
    """
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer
    permission_classes = [permissions.IsAuthenticated] 
    
    def get_queryset(self):
        querset = super().get_queryset()
        if self.action in ["list", "retrieve"]:
            querset = querset.filter(status="active", posted_at__isnull=False)
        return querset

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [permissions.AllowAny()]
        return super().get_permissions()



class ResumeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows resumes to be viewed or edited.
    """
    queryset = Job_apply_Application.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [permissions.AllowAny()]
        return super().get_permissions()


class NewsletterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows newsletters to be viewed or edited.
    """
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [permissions.AllowAny()]
        return super().get_permissions()

class EmployeeDetailViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows EmployeeDetails to be viewed or edited.
    """
    queryset = EmployeeDetail.objects.all()
    serializer_class = EmployeeDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

class EmployeeEducationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows EmployeeEducations to be viewed or edited.
    """
    queryset = EmployeeEducation.objects.all()
    serializer_class = EmployeeEducationSerializer
    permission_classes = [permissions.IsAuthenticated]

class EmployeeExperienceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows EmployeeExperiences to be viewed or edited.
    """
    queryset = EmployeeExperience.objects.all()
    serializer_class = EmployeeExperienceSerializer
    permission_classes = [permissions.IsAuthenticated]

