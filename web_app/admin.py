from django.contrib import admin
from web_app.model import JobPosting,JobCategory,JobLocation,Resume,Subscriber

admin.site.register(JobCategory)
admin.site.register(JobLocation)
admin.site.register(JobPosting)
admin.site.register(Resume)
admin.site.register(Subscriber)

