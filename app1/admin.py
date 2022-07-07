from django.contrib import admin
from app1.models import Category, JobPost, Application, Location, JobTitle
# Register your models here.

admin.site.register(Category)
admin.site.register(Location)
admin.site.register(JobTitle)
admin.site.register(JobPost)
admin.site.register(Application)