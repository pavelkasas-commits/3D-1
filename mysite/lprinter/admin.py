from django.contrib import admin

from .forms import TaskAdminForm
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    form = TaskAdminForm
    list_display = ("title", "user", "creat_at")
    search_fields = ("title", "content", "user__username")
