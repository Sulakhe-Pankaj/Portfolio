from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'is_active')
    search_fields = ('name', 'email')

@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_title', 'profile')
    list_filter = ('profile',)

@admin.register(models.project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'profile', 'project_duration')
    list_filter = ('profile',)

@admin.register(models.blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_title', 'profile', 'blog_date')
    list_filter = ('profile', 'blog_date')

@admin.register(models.enq)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'profile')
    list_filter = ('profile',)
