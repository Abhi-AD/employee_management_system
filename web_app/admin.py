from django.contrib import admin
from web_app.model import JobPosting,JobCategory,JobLocation,Newsletter,Job_apply_Application

admin.site.register(JobCategory)
admin.site.register(JobLocation)
admin.site.register(JobPosting)
admin.site.register(Newsletter)


@admin.register(Job_apply_Application)
class PostAdmin(admin.ModelAdmin):
     list_display = ['category_id','apply_date','gender']
     list_filter = ['category_id','location', 'gender']
     search_fields = ['category_id', 'location']
     prepopulated_fields = {'state': ('category_id',)}
     date_hierarchy = 'apply_date'
     ordering = ['location', 'apply_date']
     