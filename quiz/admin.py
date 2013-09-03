from django.contrib import admin
from django.forms.models import BaseInlineFormSet
from quiz.models import (Quiz, Question, Answer, FinalResponse)
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django import forms


# Formsets
class AnswerFormset(BaseInlineFormSet):
    """
    Checks if Q + n * (A + 3) <= 163
    """
    def clean(self):
        super(AnswerFormset, self).clean()
        char_limit = len(self.instance.question)
        for form in self.forms:
            if not hasattr(form, 'cleaned_data'):
                continue

            if "answer" in form.cleaned_data:
                char_limit = char_limit + len(form.cleaned_data['answer']) + 3

                if char_limit > 163:
                    raise forms.ValidationError("You have gone beyond the"
                                                " character limit"
                                                " please shorten questions"
                                                " and/or answers")


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

    def response_add(self, request, obj, post_url_continue=None):
        if '_addanother' in request.POST:
            url = reverse("admin:quiz_question_add")
            quiz_id = request.POST['quiz_id']
            qs = '?quiz_id=%s' % quiz_id
            return HttpResponseRedirect(''.join((url, qs)))
        else:
            return super(QuestionAdmin, self).response_add(request,
                                                           obj,
                                                           post_url_continue=None)

    def response_change(self, request, obj, post_url_continue=None):
        if '_addanother' in request.POST:
            url = reverse("admin:quiz_question_add")
            quiz_id = request.POST['quiz_id']
            qs = '?quiz_id=%s' % quiz_id
            return HttpResponseRedirect(''.join((url, qs)))
        else:
            return super(QuestionAdmin, self).response_add(request,
                                                           obj,
                                                           post_url_continue=None)


class FinalResponseAdmin(admin.ModelAdmin):
    list_display = ["quiz_id", "text", "sms", "for_total"]

    def response_add(self, request, obj, post_url_continue=None):
        if '_addanother' in request.POST:
            url = reverse("admin:quiz_finalresponse_add")
            quiz_id = request.POST['quiz_id']
            qs = '?quiz_id=%s' % quiz_id
            return HttpResponseRedirect(''.join((url, qs)))
        else:
            return super(FinalResponseAdmin, self).response_add(request,
                                                                obj,
                                                                post_url_continue=None)

    def response_change(self, request, obj, post_url_continue=None):
        if '_addanother' in request.POST:
            url = reverse("admin:quiz_finalresponse_add")
            quiz_id = request.POST['quiz_id']
            qs = '?quiz_id=%s' % quiz_id
            return HttpResponseRedirect(''.join((url, qs)))
        else:
            return super(FinalResponseAdmin, self).response_add(request,
                                                                obj,
                                                                post_url_continue=None)


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(FinalResponse, FinalResponseAdmin)
