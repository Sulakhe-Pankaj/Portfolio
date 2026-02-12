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

     

