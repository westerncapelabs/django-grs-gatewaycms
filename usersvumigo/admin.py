from django.contrib import admin
from usersvumigo.models import (VumiGoUser, QuizResponse)
from gopher.models import SendAirtime, AirtimeApplication


def send_airtime_to_selected(modeladmin, request, queryset):
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


send_airtime_to_selected.short_descrption = "Send R 5 airtime to following users"

class VumiGoUserAdmin(admin.ModelAdmin):
    list_display = ["msisdn", "sex", "age", "community", "created_at"]
    actions = [send_airtime_to_selected]

class QuizResponseAdmin(admin.ModelAdmin):
    list_display = ["created_by", "quiz", "question", "question_text", "correct", "created_at"]



admin.site.register(VumiGoUser, VumiGoUserAdmin)
admin.site.register(QuizResponse, QuizResponseAdmin)
