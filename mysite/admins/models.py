from django.db import models

# Create your models here.
class profile(models.Model):
     name = models.CharField(max_length=300)
     password = models.CharField(max_length=500)
     email = models.EmailField()
     mobile = models.IntegerField()
     address = models.CharField(max_length=500)
     dob = models.DateTimeField()
     profile_image = models.ImageField(upload_to='static/asset')
     bg_image = models.ImageField(upload_to="static/asset/", null=True, blank=True)
     facebook = models.URLField(max_length=300)
     linkedin = models.URLField(max_length=300)

class Service(models.Model):
    service_image = models.ImageField(upload_to='static/asset')
    service_title = models.CharField(max_length=300)

class project(models.Model):
     project_name = models.CharField(max_length=300)
     project_image = models.ImageField(upload_to="static/asset/")
     project_desc = models.CharField(max_length=300)
     project_link = models.URLField(max_length=300)
     project_duration = models.CharField(max_length=100)

class blog(models.Model):
    blog_date = models.DateField()
    blog_image = models.ImageField(upload_to="static/asset/")
    blog_title = models.CharField(max_length=200)
    blog_description = models.TextField()

class enq(models.Model):
     name = models.TextField(max_length=300)
     email = models.TextField(max_length=300)
     mobile = models.IntegerField(max_length=20)
     massage = models.TextField(max_length=300)



     

