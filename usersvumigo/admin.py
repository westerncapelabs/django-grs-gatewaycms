from django.contrib import admin
from usersvumigo.models import (VumiGoUser)
from gopher.models import SendAirtime, AirtimeApplication


def send_five_rand_airtime_to_selected(modeladmin, request, queryset):
    """
    Post Structure:
    {
        "denomination": 10,
        "product_code": "AIRTIME",
        "notes": "Grassroots Random Winner",
        "msisdn": 27821231231,
        "project_id": ""
    }
    """
    app = AirtimeApplication.objects.get(name="Registered User Airtime")
    amount = 500  # cents
    product_key = "AIRTIME"
    create_list = [SendAirtime(app_id_id=app.id, msisdn=obj.msisdn, amount=amount, product_key=product_key) for obj in queryset]
    SendAirtime.objects.bulk_create(create_list)


def send_ten_rand_airtime_to_selected(modeladmin, request, queryset):
    """
    Post Structure:
    {
        "denomination": 1000,
        "product_code": "AIRTIME",
        "notes": "Grassroots Random Winner",
        "msisdn": 27821231231,
        "project_id": ""
    }
    """
    app = AirtimeApplication.objects.get(name="Registered User Airtime")
    amount = 1000  # cents
    product_key = "AIRTIME"
    create_list = [SendAirtime(app_id_id=app.id, msisdn=obj.msisdn, amount=amount, product_key=product_key) for obj in queryset]
    SendAirtime.objects.bulk_create(create_list)


def send_fifteen_rand_airtime_to_selected(modeladmin, request, queryset):
    """
    Post Structure:
    {
        "denomination": 10,
        "product_code": "AIRTIME",
        "notes": "Grassroots Random Winner",
        "msisdn": 27821231231,
        "project_id": ""
    }
    """
    app = AirtimeApplication.objects.get(name="Registered User Airtime")
    amount = 1500  # cents
    product_key = "AIRTIME"
    create_list = [SendAirtime(app_id_id=app.id, msisdn=obj.msisdn, amount=amount, product_key=product_key) for obj in queryset]
    SendAirtime.objects.bulk_create(create_list)


send_five_rand_airtime_to_selected.short_description = "Send R 5 airtime to following users"
send_ten_rand_airtime_to_selected.short_description = "Send R 10 airtime to following users"
send_fifteen_rand_airtime_to_selected.short_description = "Send R 15 airtime to following users"

class VumiGoUserAdmin(admin.ModelAdmin):
    list_display = ["msisdn", "sex", "age", "community", "created_at"]
    actions = [send_five_rand_airtime_to_selected, send_ten_rand_airtime_to_selected,
               send_fifteen_rand_airtime_to_selected]


admin.site.register(VumiGoUser, VumiGoUserAdmin)
