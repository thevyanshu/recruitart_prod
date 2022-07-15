#import re
from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.category_name


class JobTitle(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    #def __str__(self):
    #    return self.category.category_name
    
class Location(models.Model):
    
    city = models.CharField(max_length=50)
    job_title = models.ManyToManyField(JobTitle)
    def __str__(self):
        return self.city
    
    
    
    
class JobPost(models.Model):
    
    job_title = models.ForeignKey(JobTitle, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    remuneration = models.CharField(max_length=255)
    job_description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.company_name)
    
    #def __str__(self):
    #    return self.company_name
    
    #def __str__(self):
    #    return self.remuneration
    
    #def __str__(self):
    #    return self.job_description


joining_choices = (
    ("Immediately","Immediately"),
    ("15 Days", "15 Days"),
    ("1 Month", "1 Month"),
    ("2 Month", "2 Months"),
    ("3 Month", "3 months"),
)
class Application(models.Model):
    
    current_designation = models.CharField(max_length=255)
    current_location = models.CharField(max_length=255)
    preferred_designation = models.CharField(max_length=255)
    preferred_location = models.CharField(max_length=255)
    current_salary = models.CharField(max_length=255)
    expected_salary = models.CharField(max_length=255)
    can_join = models.CharField(max_length=20, choices= joining_choices, default='1')
    name = models.CharField(max_length=255)
    mobile_no = models.IntegerField(max_length=10)
    alternate_mobile = models.IntegerField()
    total_experience = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    pg_name = models.CharField(max_length=255)
    ug_name = models.CharField(max_length=255)
    message = models.TextField(max_length=255)
    resume = models.FileField(upload_to='resume')
    agree = models.BooleanField(default=False)
    
    jobpost = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.current_designation
    
    def __str__(self):
        return self.current_location
    
    def __str__(self):
        return self.preferred_designation
    
    def __str__(self):
        return self.preferred_location
    
    def __str__(self):
        return self.current_salary
    
    def __str__(self):
        return self.expected_salary
    
    def __str__(self):
        return self.can_join
    
    def __str__(self):
        return self.name
    
    def __int__(self):
        return self.mobile_no
    
    def __int__(self):
        return self.alternate_mobile
    
    def __str__(self):
        return self.total_experience
    
    def __str__(self):
        return self.email
    
    def __str__(self):
        return self.pg_name
    
    def __str__(self):
        return self.ug_name
    
    def __str__(self):
        return self.message
    
    def __str__(self):
        return self.resume
    
    def __str__(self):
        return self.agree