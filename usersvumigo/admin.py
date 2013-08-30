from django.contrib import admin
from usersvumigo.models import (VumiGoUser)


class VumiGoUserAdmin(admin.ModelAdmin):
    list_display = ["msisdn", "sex", "age", "community"]


admin.site.register(VumiGoUser, VumiGoUserAdmin)
