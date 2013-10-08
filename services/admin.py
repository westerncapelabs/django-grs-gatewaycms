# from django.contrib import admin
# from services.models import Service


# class ServiceAdmin(admin.ModelAdmin):
#     list_display = ["name", "content_1", "content_2", "content_3", "sms"]


# admin.site.register(Service, ServiceAdmin)

# -----

from django.contrib import admin
from models import (Category, Service)
from django import forms
from django.forms.models import BaseInlineFormSet


class ServiceFormset(BaseInlineFormSet):
    def clean(self):
        super(ServiceFormset, self).clean()

        for form in self.forms:
            if not hasattr(form, 'cleaned_data'):
                continue

            service_index = 0
            if ("name" not in form.cleaned_data and service_index >= 1):
                raise forms.ValidationError("You need to name the service")

            if ("name" in form.cleaned_data):
                if not (form.cleaned_data["content_1"] or
                        form.cleaned_data["content_2"] or
                        form.cleaned_data["content_3"]):
                    raise forms.ValidationError("You need to enter at least one "
                                                "screen of content to display")

            if ("sms" not in form.cleaned_data and service_index >= 1):
                raise forms.ValidationError("You need to provice an SMS")

            service_index = service_index + 1


class ServiceInline(admin.StackedInline):
    model = Service
    extra = 0  # Number of initial answers fields
    formset = ServiceFormset


class CategoryAdmin(admin.ModelAdmin):
    inlines = [ServiceInline]

admin.site.register(Category, CategoryAdmin)
