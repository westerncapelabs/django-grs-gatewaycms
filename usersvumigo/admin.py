from django.contrib import admin
from usersvumigo.models import (VumiGoUser)


class VumiGoUserAdmin(admin.ModelAdmin):
    list_display = ["msisdn", "sex", "age", "community", "created_at"]


admin.site.register(VumiGoUser, VumiGoUserAdmin)
