from django.contrib import admin
from web_app.model import JobPosting,JobCategory,JobLocation,Resume,Newsletter

admin.site.register(JobCategory)
admin.site.register(JobLocation)
admin.site.register(JobPosting)
admin.site.register(Resume)
admin.site.register(Newsletter)

