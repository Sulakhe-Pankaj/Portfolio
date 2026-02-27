"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from website import views as users
from admins import views as adminp


urlpatterns = [
    path('', users.home),
    path('add/',users.add),
    path('home/', users.home),
    path('portfolio/', users.portfolio),
    path('about/', users.about),
    path('service/', users.service),
    path('blog/', users.blog),
    path('contact/', users.contact),
    path('save_enq/', users.save_enq),

    path('save_user/', adminp.save_user),
    path('confirm_profile_action/<int:id>/', adminp.confirm_profile_action, name='confirm_profile_action'),
    path('admin/', adminp.home),
    path('register/', adminp.register, name='register'),
    path('login/',adminp.login, name='login'),
    path('logout/',adminp.logout, name='logout'),
    path('profile/', adminp.profile),  
    path('services/',adminp.services),
    path('save_services/',adminp.save_services) ,
    path('project/',adminp.project),
    path('save_project/',adminp.save_project),
    path('blogs/', adminp.blogs),
    path('save_blog/', adminp.save_blog),
    path('enquiry/', adminp.enquiry),
    path('delete_service/<int:id>/',adminp.delete_service, name="delete_service"),
    path('delete_profile/<int:id>/',adminp.delete_profile, name="delete_profile"),
    path('delete_blog/<int:id>/',adminp.delete_blog, name="delete_blog"),
    path('delete_project/<int:id>/',adminp.delete_project, name="delete_project"),
    path('update_service/<int:id>/',adminp.update_service, name="update_service"),
    path('update_profile/<int:id>/',adminp.update_profile, name="update_profile"),
    path('update_project/<int:id>/',adminp.update_project, name="update_project"),
    path('update_blog/<int:id>/',adminp.update_blog, name="update_blog"),

    path('delete_service_user/<int:id>/',users.delete_service_user, name="delete_service_user"),
    path('delete_profile_user/<int:id>/',users.delete_profile_user, name="delete_profile_user"),
    path('delete_blog_user/<int:id>/',users.delete_blog_user, name="delete_blog_user"),
    path('delete_project_user/<int:id>/',users.delete_project_user, name="delete_project_user"),
    path('update_service_user/<int:id>/',users.update_service_user, name="update_service_user"),
    path('update_profile_user/<int:id>/',users.update_profile_user, name="update_profile_user"),
    path('update_project_user/<int:id>/',users.update_project_user, name="update_project_user"),
    path('add_project_user/',users.add_project_user, name="add_project_user"),
    path('update_blog_user/<int:id>/',users.update_blog_user, name="update_blog_user"),
    path('switch_profile/<int:id>/',adminp.switch_profile, name="switch_profile")

]
