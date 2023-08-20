from django.db import models




class TimesStampModel(models.Model):
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
     
     class Meta:
          abstract = True #Don't create table in DB
     
class JobCategory(models.Model):
     name = models.CharField(max_length=100)
     def __str__(self):
          return self.name
     
class JobLocation(models.Model):
     name = models.CharField(max_length=100)   
     def __str__(self):
          return self.name
     


class JobPosting(models.Model):
     STATUS_CHOICES = [
          ("active", "Active"),
          ("in_active", "Inactive"),
     ]
     title = models.CharField(max_length=200)
     company = models.CharField(max_length=100)
     feature_image = models.ImageField(upload_to="Job_post_images/%Y/%m/%d", blank=False)
     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="active")
     description = models.TextField()
     salary = models.DecimalField(max_digits=10, decimal_places=2)
     posted_at = models.DateTimeField(auto_now_add=True)
     views_count = models.PositiveBigIntegerField(default=0)
     category = models.ForeignKey(JobCategory, on_delete=models.CASCADE)
     location = models.ManyToManyField(JobLocation)
     
     
     def __str__(self):
        return self.title
   


class Resume(models.Model):
    full_name = models.CharField(max_length=150)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    email = models.EmailField()
    current_address = models.CharField(max_length=300)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    resume = models.FileField(upload_to='Job_apply/resumes/%Y/%m/%d', blank=False)
    letter = models.FileField(upload_to='Job_apply/letter/%Y/%m/%d', blank=False)
    apply_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name




