from django.shortcuts import render, redirect 
from admins import models
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def login(req):
    if req.method == 'POST':
        email = req.POST.get('email')
        password =req.POST.get('password')

        try:
            user = models.profile.objects.get(email = email, password = password)
            req.session['admin_id'] = user.id
            req.session['admin_name'] = user.name
            return redirect('/admin/')
        except:
            return HttpResponse('invalid password or id please try again','/login/')
    return render(req,'admin_panel/login.html')

def logout(req):
    req.session.flush()
    return redirect('/login')

def home(req):
    if not req.session.get('admin_id'):
        return redirect('/login/')
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
    return render (req,'admin_panel/home.html',obj)
def profile(req):
    user_data = models.profile.objects. all()
    obj = {
        'user_data':user_data
        }
    return render(req, "admin_panel/profile.html",obj)
def save_user(req):
    if req.method == 'POST':
        save_user = models.profile(
            name = req.POST.get('name'),
            password = req.POST.get('password'),
            email = req.POST.get('email'),
            mobile = req.POST.get('mobile'), 
            address = req.POST.get('address'),
            dob = req.POST.get('dob'),
            profile_image = req.FILES.get('profile_image'),
            bg_image = req.FILES.get('bg_image'),
            facebook = req.POST.get('facebook'),
            linkedin = req.POST.get('linkedin')
        )
        save_user.save()
    return redirect("/profile")

def services(req):
    service_data = models.Service.objects.all()
    obj = {
        "service_data":service_data
    }
    return render(req, "admin_panel/services.html",obj)
def save_services(req):
    if req.method == 'POST':
        save_services =models.Service(
            service_image = req.FILES.get('service_image'), 
            service_title = req.POST.get('service_title')
        )
        save_services.save()
        messages.success(req, "Service saved")
        return redirect("/services")

def project(req):
    project_data = models.project.objects.all()
    obj = {
        "project_data":project_data
    }
    return render(req, "admin_panel/project.html",obj)

def save_project(req):
    if req.method == 'POST':
        project_data = models.project(
            project_name = req.POST.get('project_name'),
            project_image = req.FILES.get('project_image'),
            project_desc = req.POST.get('project_desc'),
            project_link = req.POST.get('project_link'),
            project_duration = req.POST.get('project_duration')
        )
        project_data.save()
        return redirect('/project')
    
def blogs(req):
    blog_data = models.blog.objects.all()
    obj = {
        "blog_data":blog_data
    }
    return render(req,"admin_panel/blog.html",obj)

def save_blog(req):
    if req.method == "POST":
        blog_data = models.blog(
           blog_date = req.POST.get('blog_date'),
           blog_image = req.FILES.get('blog_image'),
           blog_title = req.POST.get('blog_title'),
           blog_description = req.POST.get('blog_description')
        )
        blog_data.save()
        return redirect('/blogs')
    
def enquiry(req):
    enq_data = models.enq.objects.all()
    obj = {
        'enq_data':enq_data
    }
    return render(req, "admin_panel/enq.html",obj)

def delete_service(req, id):
     services_data =  models.Service.objects.filter(id=id)
     if services_data.exists():
         services_data.delete()
         return HttpResponse('data delete successfully')
     else:
         return redirect('/admin')

def update_service(req,id):
    services_data = models.Service.objects.get(id = id)
    if req.method == 'POST':
        services_data.service_title = req.POST.get('service_title')
        if req.FILES.get('service_image'):
            services_data.service_image = req.FILES.get('service_image')
        services_data.save()
        return redirect('/admin')
    return render(req, 'admin_panel/update_service.html',{'services':services_data})

def update_profile(req,id):
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
        return redirect('/admin')
    return render(req, 'admin_panel/update_profile.html',{'user':user_data})

def delete_profile(req, id):
     user_data =  models.profile.objects.filter(id=id)
     if user_data.exists():
         user_data.delete()
         return HttpResponse('data delete successfully')
     else:
         return redirect('/admin')
     
def delete_project(req, id):
     project_data =  models.project.objects.filter(id=id)
     if project_data.exists():
         project_data.delete()
         return HttpResponse('data delete successfully')
     else:
         return redirect('/admin')
     
def update_project(req,id):
    project_data = models.project.objects.get(id=id)
    if req.method == "POST":
        project_data.project_name = req.POST.get("project_name")
        project_data.project_desc = req.POST.get("project_desc")
        project_data.project_link = req.POST.get("project_link")
        project_data.project_duration = req.POST.get("project_duration")

        if req.FILES.get("project_image"):
            project_data.project_image = req.FILES.get("project_image")

        project_data.save()
        return redirect("/admin")

    return render(req, "admin_panel/update_project.html", {"project": project_data})

def update_blog(req,id):
    blog_data = models.blog.objects.get(id=id)
    if req.method == 'POST':
        blog_data.blog_date = req.POST.get('blog_date')
        blog_data.blog_title = req.POST.get('blog_title')
        blog_data.blog_description = req.POST.get('blog_description')
        
        if req.FILES.get('blog_image'):
            blog_data.blog_image = req.FILES.get('blog_image')

        blog_data.save()
        return redirect('/admin')
    return render(req,'admin_panel/update_blog.html',{'blog':blog_data})

def delete_blog(req, id):
     blog_data =  models.blog.objects.filter(id=id)
     if blog_data.exists():
         blog_data.delete()
         return HttpResponse('data delete successfully')
     else:
         return redirect('/admin')
    

