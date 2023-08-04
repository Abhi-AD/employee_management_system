from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class EmployeeDetail(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     empcode = models.IntegerField(max_length=10, null=True)
     empdept = models.CharField(max_length=50, null=True)
     designation = models.CharField(max_length=100, null=True)
     contact = models.IntegerField(max_length=10, null=True)
     gender = models.CharField(max_length=50, null=True)
     join_date = models.DateField(null=True)
     
     def __str__(self):
          return self.user.username
     
     