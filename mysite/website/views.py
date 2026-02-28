from django.shortcuts import render,redirect
from admins import models
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def get_public_context(req):
    active_profile = models.profile.objects.filter(is_active=True).first()
    if not active_profile:
        active_profile = models.profile.objects.first()
    
    admin_id = req.session.get('admin_id')
    
    if active_profile:
        user_data = models.profile.objects.filter(id=active_profile.id)
        service_data = models.Service.objects.filter(profile_id=active_profile.id) 
        project_data = models.project.objects.filter(profile_id=active_profile.id) 
        blog_data = models.blog.objects.filter(profile_id=active_profile.id) 
    else:
        user_data = service_data = project_data = blog_data = []

    all_profiles = models.profile.objects.all()
    
    return {
        'user_data': user_data,
        'all_profiles': all_profiles,
        'service_data': service_data,
        'project_data': project_data,
        'blog_data': blog_data,
        'admin_id': admin_id,
        'active_profile_id': active_profile.id if active_profile else None
    }

def home(req):
    obj = get_public_context(req)
    return render(req, 'user/index.html', obj)
    
def about(req):
    obj = get_public_context(req)
    return render(req, 'user/about.html', obj)
    
def contact(req):
    obj = get_public_context(req)
    return render(req, 'user/contact.html', obj)
    
def portfolio(req):
    obj = get_public_context(req)
    return render(req, 'user/portfolio.html', obj)
    
def blog(req):
    obj = get_public_context(req)
    return render(req, 'user/blog.html', obj)
    
def service(req):
    obj = get_public_context(req)
    return render(req, 'user/service.html', obj)

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
     admin_id = req.session.get('admin_id')
     if not admin_id:
         return redirect('/login/')
     services_data =  models.Service.objects.filter(id=id, profile_id=admin_id)
     if services_data.exists():
         services_data.delete()
         messages.success(req, "Service deleted successfully")
     else:
         messages.error(req, "Data is not found or you don't have permission")
     return redirect('/service')

def delete_profile_user(req, id):
     admin_id = req.session.get('admin_id')
     if not admin_id or str(admin_id) != str(id):
         return redirect('/login/')
     user_data =  models.profile.objects.filter(id=id)
     if user_data.exists():
         user_data.delete()
         req.session.flush()
     return redirect('/home')
     
def delete_project_user(req, id):
     admin_id = req.session.get('admin_id')
     if not admin_id:
         return redirect('/login/')
     project_data =  models.project.objects.filter(id=id, profile_id=admin_id)
     if project_data.exists():
         project_data.delete()
     else:
         return HttpResponse('Data is not found or no permission')
     return redirect('/portfolio')
     
def delete_blog_user(req, id):
     admin_id = req.session.get('admin_id')
     if not admin_id:
         return redirect('/login/')
     blog_data =  models.blog.objects.filter(id=id, profile_id=admin_id)
     if blog_data.exists():
         blog_data.delete()
     return redirect('/blog')
     
#  ================================= update section ============================
     
def update_service_user(req,id):
    admin_id = req.session.get('admin_id')
    if not admin_id:
        return redirect('/login/')
    services_data = models.Service.objects.get(id = id)
    if services_data.profile_id != admin_id:
        return redirect('/service')
    if req.method == 'POST':
        services_data.service_title = req.POST.get('service_title')
        if req.FILES.get('service_image'):
            services_data.service_image = req.FILES.get('service_image')
        services_data.save()
        return redirect('/service')
    return render(req, 'admin_panel/update_service.html',{'services':services_data})

def update_profile_user(req,id):
    admin_id = req.session.get('admin_id')
    if not admin_id or str(admin_id) != str(id):
        return redirect('/login/')
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
        return redirect('/home')
    return render(req, 'admin_panel/update_profile.html',{'user':user_data})
     
def update_project_user(req,id):
    admin_id = req.session.get('admin_id')
    if not admin_id:
        return redirect('/login/')
    project_data = models.project.objects.get(id=id)
    if project_data.profile_id != admin_id:
        return redirect('/portfolio')
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
    admin_id = req.session.get('admin_id')
    if not admin_id:
        return redirect('/login/')
    blog_data = models.blog.objects.get(id=id)
    if blog_data.profile_id != admin_id:
        return redirect('/blog')
    if req.method == 'POST':
        blog_data.blog_date = req.POST.get('blog_date')
        blog_data.blog_title = req.POST.get('blog_title')
        blog_data.blog_description = req.POST.get('blog_description')
        
        if req.FILES.get('blog_image'):
            blog_data.blog_image = req.FILES.get('blog_image')

        blog_data.save()
        return redirect('/blog')
    return render(req,'admin_panel/update_blog.html',{'blog':blog_data})


def add_project_user(req):
    admin_id = req.session.get('admin_id')
    if not admin_id:
        return redirect('/login/')
    user_data = models.profile.objects.filter(id=admin_id)
    
    if req.method == 'POST':
        project_data = models.project(
            profile_id=admin_id,
            project_name = req.POST.get('project_name'),
            project_image = req.FILES.get('project_image'),
            project_desc = req.POST.get('project_desc'),
            project_link = req.POST.get('project_link'),
            project_duration = req.POST.get('project_duration')
        )
        project_data.save()
        messages.success(req, "Project added successfully")
        return redirect('/portfolio')
    
    obj = {'user_data': user_data}
    return render(req, 'user/add_project.html', obj)

def add(req):
    return render (req,'user/add.py')
    