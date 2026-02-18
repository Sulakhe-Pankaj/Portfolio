from django.shortcuts import render,redirect
from admins import models
from django.http import HttpResponse
from django.contrib import messages

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
    return render (req,'user/about.html',obj)
    
def contact(req):
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
    return render (req,'user/contact.html',obj)
    
def portfolio(req):
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
    return render (req,'user/portfolio.html',obj)
    
def blog(req):
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
    return render (req,'user/blog.html',obj)
    
def service(req):
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
    return render (req,'user/service.html',obj)

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
    
    # =============================== delete section ===============================
    
def delete_service_user(req, id):
     services_data =  models.Service.objects.filter(id=id)
     if services_data.exists():
         services_data.delete()
         messages.success(req, "Service deleted successfully")
         return redirect('/service')
     else:
         messages.success(req, "data is not found")
     return redirect('/service')

def delete_profile_user(req, id):
     user_data =  models.profile.objects.filter(id=id)
     if user_data.exists():
         user_data.delete()
         return redirect('/home')
     else:
         return redirect('/home')
     
def delete_project_user(req, id):
     project_data =  models.project.objects.filter(id=id)
     if project_data.exists():
         project_data.delete()
     else:
         return HttpResponse('Data is not found')
     return redirect('/portfolio')
     
def delete_blog_user(req, id):
     blog_data =  models.blog.objects.filter(id=id)
     if blog_data.exists():
         blog_data.delete()
         return redirect('/blog')
     else:
         return redirect('/blog')
     
#  ================================= update section ============================
     
def update_service_user(req,id):
    services_data = models.Service.objects.get(id = id)
    if req.method == 'POST':
        services_data.service_title = req.POST.get('service_title')
        if req.FILES.get('service_image'):
            services_data.service_image = req.FILES.get('service_image')
        services_data.save()
        return redirect('/service')
    return render(req, 'admin_panel/update_service.html',{'services':services_data})

def update_profile_user(req,id):
    user_data = models.profile.objects.get(id = id)
    if req.method == 'POST':
        user_data.name = req.POST.get('name')
        user_data.password = req.POST.get('password')
        user_data.mail = req.POST.get('mail')
        user_data.mobile = req.POST.get('mobile')
        user_data.address = req.POST.get('address')
        user_data.bod = req.POST.get('bod')
        user_data.bod = req.POST.get('bod')
        user_data.facebook = req.POST.get('facebook')
        user_data.linkedin = req.POST.get('linkedin')

        if req.FILES.get('profile_image'):
            user_data.profile_image = req.FILES.get('profile_image')
            user_data.bg_image = req.FILES.get('bg_image')

        user_data.save()
        return redirect('/home')
    return render(req, 'admin_panel/update_profile.html',{'user':user_data})
     
def update_project_user(req,id):
    project_data = models.project.objects.get(id=id)
    if req.method == "POST":
        project_data.project_name = req.POST.get("project_name")
        project_data.project_desc = req.POST.get("project_desc")
        project_data.project_link = req.POST.get("project_link")
        project_data.project_duration = req.POST.get("project_duration")

        if req.FILES.get("project_image"):
            project_data.project_image = req.FILES.get("project_image")

        project_data.save()
        return redirect("/portfolio")

    return render(req, "admin_panel/update_project.html", {"project": project_data})

def update_blog_user(req,id):
    blog_data = models.blog.objects.get(id=id)
    if req.method == 'POST':
        blog_data.blog_date = req.POST.get('blog_date')
        blog_data.blog_title = req.POST.get('blog_title')
        blog_data.blog_description = req.POST.get('blog_description')
        
        if req.FILES.get('blog_image'):
            blog_data.blog_image = req.FILES.get('blog_image')

        blog_data.save()
        return redirect('/blog')
    return render(req,'admin_panel/update_blog.html',{'blog':blog_data})


def add(req):
    return render (req,'user/add.py')
    