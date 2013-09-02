from django.contrib import admin
from django import forms
from django.forms.models import BaseInlineFormSet
from quiz.models import (Quiz, Question, Answer, FinalResponse)

# Formsets 
class AnswerFormset(BaseInlineFormSet):
    pass


class FinalResponseFormset(BaseInlineFormSet):
    pass


# Inlines
class AnswerInline(admin.StackedInline):
    model = Answer
    formset = AnswerFormset


# Admin
class QuizAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "active",
                    "updated_by", "updated_at"]

    def save_model(self, request, obj, form, change):
        obj.updated_by = request.user
        obj.save()


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_display = ["quiz_id", "question"]


class FinalResponseAdmin(admin.ModelAdmin):
    list_display = ["quiz_id", "text", "sms", "for_total"]


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(FinalResponse, FinalResponseAdmin)
