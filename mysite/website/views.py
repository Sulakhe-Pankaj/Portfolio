from django.shortcuts import render
from admins import models 

# Create your views here.
def home(req):
    user_data = models.profile.objects.all() 
    service_data = models.Service.objects.all() 
    obj =  {
        'user_data':user_data,
        'service_data':service_data
    }
    return render (req,'user/index.html',obj)
    
def about(req):
    return render (req,'user/about.html')
    
def contact(req):
    return render (req,'user/contact.html')
    
def portfolio(req): 
    return render (req,'user/portfolio.html')
    
def blog(req):
    return render (req,'user/blog.html')
    
def service(req):
    return render (req,'user/service.html')
    