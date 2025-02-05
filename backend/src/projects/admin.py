from django.contrib import admin
from projects.models import Tags , Task , Project
# Register your models here.

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    fields=['name']
    