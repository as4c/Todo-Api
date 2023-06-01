from django.contrib import admin
from .models import Task, Tag


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description','timestamp', 'due_date', 'status')

admin.site.register(Task)
admin.site.register(Tag)
