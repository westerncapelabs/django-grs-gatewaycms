from django.contrib import admin
from usersvumigo.models import (VumiGoUser, QuizResponse)
from usersvumigo.tasks import send_bulk_sms


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
    DEN = 5000
    PROD = "AIRTIME"
    NOTES = ""
    sms_array = [{"msisdn": obj.msisdn, "denomination": DEN, "product_code": PROD, "notes": NOTES} for obj in queryset]
    send_bulk_sms.delay(sms_array)


send_airtime_to_selected.short_descrption = "Send airtime to following users"

class VumiGoUserAdmin(admin.ModelAdmin):
    list_display = ["msisdn", "sex", "age", "community", "created_at"]
    actions = [send_airtime_to_selected]

class QuizResponseAdmin(admin.ModelAdmin):
    list_display = ["created_by", "quiz", "question", "question_text", "correct", "created_at"]



admin.site.register(VumiGoUser, VumiGoUserAdmin)
admin.site.register(QuizResponse, QuizResponseAdmin)
