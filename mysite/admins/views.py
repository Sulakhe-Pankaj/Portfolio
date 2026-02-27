from django.shortcuts import render, redirect 
from admins import models
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def confirm_profile_action(req, id):
    try:
        profile = models.profile.objects.get(id=id)
    except models.profile.DoesNotExist:
        messages.error(req, "Profile not found.")
        return redirect('/admin/')

    next_url = req.GET.get('next', '/admin/')

    if req.method == 'POST':
        password = req.POST.get('password')
        if password == profile.password:
            # Set auth session flag
            req.session[f'auth_{id}'] = True
            return redirect(next_url)
        else:
            messages.error(req, "Incorrect password. Please try again.")

    return render(req, 'admin_panel/confirm_password.html', {'profile_name': profile.name})
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

def register(req):
    return render(req, 'admin_panel/register.html')

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
        'blog_data':blog_data,
        'current_admin_id': req.session.get('admin_id')
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
        # Check if this is the first profile ever created
        is_first = not models.profile.objects.exists()
        
        user_profile = models.profile()
        user_profile.name = req.POST.get('name')
        user_profile.password = req.POST.get('password')
        user_profile.email = req.POST.get('email')
        user_profile.mobile = req.POST.get('mobile')
        user_profile.address = req.POST.get('address', '')
        dob_val = req.POST.get('dob')
        if dob_val:
            user_profile.dob = dob_val
        else:
            from django.utils import timezone
            user_profile.dob = timezone.now()
            
        user_profile.facebook = req.POST.get('facebook', '')
        user_profile.linkedin = req.POST.get('linkedin', '')
        
        # If it's the first profile, make it active by default
        if is_first:
            user_profile.is_active = True
        else:
            user_profile.is_active = False
            
        if req.FILES.get('profile_image'):
            user_profile.profile_image = req.FILES.get('profile_image')
            
        if req.FILES.get('bg_image'):
            user_profile.bg_image = req.FILES.get('bg_image')
            
        user_profile.save()
        messages.success(req, "New profile created successfully!")
        
        # If created by an existing admin, stay in admin panel. 
        # If created by a new public user, go to login.
        if req.session.get('admin_id'):
            return redirect("/admin")
        else:
            return redirect("/login")
    return redirect("/login")

def switch_profile(req, id):
    # Check for authentication
    if not req.session.get(f'auth_{id}'):
        return redirect(f'/confirm_profile_action/{id}/?next=/switch_profile/{id}/')

    # Set all profiles to inactive
    models.profile.objects.all().update(is_active=False)
    # Set the selected profile to active
    selected_profile = models.profile.objects.get(id=id)
    selected_profile.is_active = True
    selected_profile.save()

    # Clear auth flag
    if f'auth_{id}' in req.session:
        del req.session[f'auth_{id}']

    messages.success(req, f"Profile '{selected_profile.name}' is now active.")
    
    # Redirect back to previous page
    next_url = req.META.get('HTTP_REFERER', '/admin/')
    return redirect(next_url)

def services(req):
    service_data = models.Service.objects.all()
    obj = {
        "service_data":service_data
    }
    return render(req, "admin_panel/services.html",obj)
def save_services(req):
    if req.method == 'POST':
        save_services =models.Service(
            profile_id=req.session.get('admin_id'),
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
            profile_id=req.session.get('admin_id'),
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
           profile_id=req.session.get('admin_id'),
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

# ======================== delete section =========================

def delete_service(req, id):
     services_data =  models.Service.objects.filter(id=id)
     if services_data.exists():
         service = services_data.first()
         if service.profile_id != req.session.get('admin_id'):
             messages.error(req, 'You do not have permission to delete this service.')
             return redirect('/admin')
         services_data.delete()
     else:
         return HttpResponse('data is not found')
     return redirect('/admin')

def delete_profile(req, id):
     # Check for authentication
     if not req.session.get(f'auth_{id}'):
         return redirect(f'/confirm_profile_action/{id}/?next=/delete_profile/{id}/')

     user_data =  models.profile.objects.filter(id=id)
     if user_data.exists():
         user_data.delete()
         
         # Clear auth flag if exists
         if f'auth_{id}' in req.session:
             del req.session[f'auth_{id}']
     else:
         return HttpResponse('data is not found')
     return redirect('/admin')
     
def delete_project(req, id):
     project_data =  models.project.objects.filter(id=id)
     if project_data.exists():
         project = project_data.first()
         if project.profile_id != req.session.get('admin_id'):
             messages.error(req, 'You do not have permission to delete this project.')
             return redirect('/admin')
         project_data.delete()
     else:
         return HttpResponse('data is not found')
     return redirect('/admin')
     
def delete_blog(req, id):
     blog_data =  models.blog.objects.filter(id=id)
     if blog_data.exists():
         blog = blog_data.first()
         if blog.profile_id != req.session.get('admin_id'):
             messages.error(req, 'You do not have permission to delete this blog post.')
             return redirect('/admin')
         blog_data.delete()
     else:
         return HttpResponse('data is not found')
     return redirect('/admin')
     
#  ================================= update section ============================
     
def update_service(req,id):
    services_data = models.Service.objects.get(id = id)
    if services_data.profile_id and services_data.profile_id != req.session.get('admin_id'):
        messages.error(req, 'You do not have permission to update this service.')
        return redirect('/admin')
    if req.method == 'POST':
        services_data.service_title = req.POST.get('service_title')
        if req.FILES.get('service_image'):
            services_data.service_image = req.FILES.get('service_image')
        services_data.save()
        return redirect('/admin')
    return render(req, 'admin_panel/update_service.html',{'services':services_data})

def update_profile(req,id):
    # Check for authentication
    if not req.session.get(f'auth_{id}'):
        return redirect(f'/confirm_profile_action/{id}/?next=/update_profile/{id}/')

    user_data = models.profile.objects.get(id = id)
    if req.method == 'POST':
        user_data.name = req.POST.get('name')
        user_data.password = req.POST.get('password')
        user_data.email = req.POST.get('email')
        user_data.mobile = req.POST.get('mobile')
        user_data.address = req.POST.get('address')
        user_data.dob = req.POST.get('dob')
        user_data.facebook = req.POST.get('facebook')
        user_data.linkedin = req.POST.get('linkedin')

        if req.FILES.get('profile_image'):
            user_data.profile_image = req.FILES.get('profile_image')
            
        if req.FILES.get('bg_image'):
            user_data.bg_image = req.FILES.get('bg_image')

        user_data.save()

        # Clear auth flag
        if f'auth_{id}' in req.session:
            del req.session[f'auth_{id}']

        messages.success(req, "Profile updated successfully")
        return redirect('/admin')
    return render(req, 'admin_panel/update_profile.html',{'user':user_data})
     
def update_project(req,id):
    project_data = models.project.objects.get(id=id)
    if project_data.profile_id and project_data.profile_id != req.session.get('admin_id'):
        messages.error(req, 'You do not have permission to update this project.')
        return redirect('/admin')
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
    if blog_data.profile_id and blog_data.profile_id != req.session.get('admin_id'):
        messages.error(req, 'You do not have permission to update this blog post.')
        return redirect('/admin')
    if req.method == 'POST':
        blog_data.blog_date = req.POST.get('blog_date')
        blog_data.blog_title = req.POST.get('blog_title')
        blog_data.blog_description = req.POST.get('blog_description')
        
        if req.FILES.get('blog_image'):
            blog_data.blog_image = req.FILES.get('blog_image')

        blog_data.save()
        return redirect('/admin')
    return render(req,'admin_panel/update_blog.html',{'blog':blog_data})
    

