from django.shortcuts import render,redirect
from admins import models 

# Create your views here.
def home(req):
    user_data = models.profile.objects.all() 
    service_data = models.Service.objects.all() 
    project_data = models.project.objects.all() 
    blog_data = models.blog.objects.all() 
    obj =  {
        'user_data':user_data,
        'service_data':service_data,
        'project_data':project_data,
        'blog_data':blog_data
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

def save_enq(req):
    if req.method == "POST":
        enq_data = models.enq(
            name =req.POST.get("name"),
            email =req.POST.get("email"),
            mobile =req.POST.get("mobile"),
            massage =req.POST.get("massage")
        )
        enq_data.save()
        return redirect('/home')
    