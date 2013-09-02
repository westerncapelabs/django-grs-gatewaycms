from django.contrib import admin
from django.forms.models import BaseInlineFormSet
from quiz.models import (Quiz, Question, Answer, FinalResponse)
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

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

    def response_add(self, request, obj, post_url_continue=None):
        if request.POST.has_key('_addanother'):
            url = reverse("admin:quiz_question_add")
            quiz_id = request.POST['quiz_id']
            qs = '?quiz_id=%s' % quiz_id
            return HttpResponseRedirect(''.join((url, qs)))
        else:
            return super(QuestionAdmin, self).response_add(request, obj, post_url_continue=None)

    def response_change(self, request, obj, post_url_continue=None):
        if request.POST.has_key('_addanother'):
            url = reverse("admin:quiz_question_add")
            quiz_id = request.POST['quiz_id']
            qs = '?quiz_id=%s' % quiz_id
            return HttpResponseRedirect(''.join((url, qs)))
        else:
            return super(QuestionAdmin, self).response_add(request, obj, post_url_continue=None)



class FinalResponseAdmin(admin.ModelAdmin):
    list_display = ["quiz_id", "text", "sms", "for_total"]

    def response_add(self, request, obj, post_url_continue=None):
        if request.POST.has_key('_addanother'):
            url = reverse("admin:quiz_finalresponse_add")
            quiz_id = request.POST['quiz_id']
            qs = '?quiz_id=%s' % quiz_id
            return HttpResponseRedirect(''.join((url, qs)))
        else:
            return super(FinalResponseAdmin, self).response_add(request, obj, post_url_continue=None)

    def response_change(self, request, obj, post_url_continue=None):
        if request.POST.has_key('_addanother'):
            url = reverse("admin:quiz_finalresponse_add")
            quiz_id = request.POST['quiz_id']
            qs = '?quiz_id=%s' % quiz_id
            return HttpResponseRedirect(''.join((url, qs)))
        else:
            return super(FinalResponseAdmin, self).response_add(request, obj, post_url_continue=None)


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(FinalResponse, FinalResponseAdmin)
