from django.contrib import admin
from gopher.models import AirtimeApplication, SendAirtime


class AirtimeApplicationAdmin(admin.ModelAdmin):
    list_display = ["name", "ratio", "max_per_day", "amount", "active", "product_key"]


class SendAirtimeAdmin(admin.ModelAdmin):
    list_display = ["app_id", "msisdn", "product_key", "amount", "sent", "created_at"]


admin.site.register(AirtimeApplication, AirtimeApplicationAdmin)
admin.site.register(SendAirtime, SendAirtimeAdmin)
