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
     
class EmployeeEducation(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     
     coursepg = models.CharField(max_length=255,null=True)
     schoolpg = models.CharField(max_length=255,null=True)
     yearofpassingpg = models.DateTimeField(null=True)
     percentagepg = models.FloatField(null=True)
     
     coursegra = models.CharField(max_length=255,null=True)
     schoolgra = models.CharField(max_length=255,null=True)
     yearofpassinggra = models.DateTimeField(null=True)
     percentagegra = models.FloatField(null=True)
     
     coursessc = models.CharField(max_length=255,null=True)
     schoolssc = models.CharField(max_length=255,null=True)
     yearofpassinssc = models.DateTimeField(null=True)
     percentagessc = models.FloatField(null=True)
     
     coursehsc = models.CharField(max_length=255,null=True)
     schoolhsc = models.CharField(max_length=255,null=True)
     yearofpassinhsc = models.DateTimeField(null=True)
     percentagehsc = models.FloatField(null=True)
     def __str__(self):
          return self.user.username
     
class EmployeeExperience(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     
     first_comany_name = models.CharField(max_length=255,null=True)
     first_comany_designation = models.CharField(max_length=255,null=True)
     first_comany_duration = models.CharField(max_length=255,null=True)
     first_comany_salary = models.IntegerField(null=True)
     
     second_comany_name = models.CharField(max_length=255,null=True)
     second_comany_designation = models.CharField(max_length=255,null=True)
     second_comany_duration = models.CharField(max_length=255,null=True)
     second_comany_salary = models.IntegerField(null=True)
     
     third_comany_name = models.CharField(max_length=255,null=True)
     third_comany_designation = models.CharField(max_length=255,null=True)
     third_comany_duration = models.CharField(max_length=255,null=True)
     third_comany_salary = models.IntegerField(null=True)
     
     def __str__(self):
          return self.user.username

     