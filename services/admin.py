from django.contrib import admin
from services.models import Service


class ServiceAdmin(admin.ModelAdmin):
    list_display = ["name", "content_1", "content_2", "content_3"]


admin.site.register(Service, ServiceAdmin)
