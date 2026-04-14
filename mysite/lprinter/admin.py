from django.contrib import admin
from .forms import TaskAdminForm
from .models import Task, Filamentai, Sandelis


class TaskAdmin(admin.ModelAdmin):
    form = TaskAdminForm
    list_display = ("title", "user", "creat_at", "status" )
    search_fields = ("title", "content", "user__username")



class FilamentaiAdmin(admin.ModelAdmin):
    list_display = ("pavadinimas", "medziaga", "spalva", "atvaziavo_kg", "sunaudota_kg", "kaina")


class SandelisAdmin(admin.ModelAdmin):
    list_display = ("pavadinimas", "vieta", "aprasymas")


admin.site.register(Task, TaskAdmin)
admin.site.register(Filamentai,FilamentaiAdmin )
admin.site.register(Sandelis,SandelisAdmin)
