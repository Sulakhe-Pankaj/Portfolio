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
    return redirect("/profile"),
def services(req):
    return render(req, "admin_panel/services.html")
def save_services(req):
    if req.method == 'POST':
        save_services =models.Service(
            service_image = req.FILES.get('service_image'), 
            service_title = req.POST.get('service_title')
        )
        save_services.save()
        messages.success(req, "Service saved")
        return redirect("/services/")

