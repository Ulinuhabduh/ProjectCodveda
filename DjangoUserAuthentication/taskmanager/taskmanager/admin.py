# admin.py
from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'description', 'status', 'deadline')

    search_fields = ('title', 'description')

    list_filter = ('status',)

    list_per_page = 20

admin.site.register(Task, TaskAdmin)
