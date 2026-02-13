from django.shortcuts import render, redirect 
from admins import models
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def home(req):
    return render(req, "admin_panel/home.html")
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