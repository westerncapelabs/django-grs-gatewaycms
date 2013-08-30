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
    pass


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]


class FinalResponseAdmin(admin.ModelAdmin):
    pass


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(FinalResponse, FinalResponseAdmin)