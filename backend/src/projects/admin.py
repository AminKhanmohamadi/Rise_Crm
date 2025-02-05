from django.contrib import admin
from projects.models import Tags , Task , Project
# Register your models here.

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display=['name']
    
 
@admin.register(Project)
class ProjectsAdmin(admin.ModelAdmin):
    list_display=['title' , 'customer__name']   
    

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title' , 'project']