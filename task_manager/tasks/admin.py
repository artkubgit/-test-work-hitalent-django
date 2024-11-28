from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'due_date', 'priority', 'status')
    list_filter = ('category', 'priority', 'status')
    search_fields = ('title', 'description')
