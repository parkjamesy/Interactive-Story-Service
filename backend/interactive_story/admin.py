from django.contrib import admin
from .models import Story

# Register your models here.
class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'text')

admin.site.register(Story, StoryAdmin)

