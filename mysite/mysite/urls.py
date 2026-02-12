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
    path('home/', users.home),
    path('portfolio/', users.portfolio),
    path('about/', users.about),
    path('service/', users.service),
    path('blog/', users.blog),
    path('contact/', users.contact),

    path('save_user/', adminp.save_user),
    path('admin/', adminp.home),
    path('profile/', adminp.profile),  
    path('services/',adminp.services),
    path('save_services/',adminp.save_services) 
]
