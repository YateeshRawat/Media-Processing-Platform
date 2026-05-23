from django.contrib import admin
from .models import ProcessingTask

@admin.register(ProcessingTask)
class ProcessingTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'task_type', 'status', 'created_at')
    list_filter = ('status', 'task_type')
    search_fields = ('user__username', 'id')
