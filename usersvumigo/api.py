from tastypie.resources import ModelResource, ALL
from usersvumigo.models import VumiGoUser, QuizResponse
from tastypie import fields
from tastypie.authorization import Authorization
from django.conf.urls import url



class VumiGoUserResource(ModelResource):
    class Meta:
        queryset = VumiGoUser.objects.all()
        resource_name = "users"
        list_allowed_methods = ['post', 'get'] 
        include_resource_uri = True
        always_return_data = True
        authorization = Authorization()
        filtering = {
            'msisdn': ALL}

    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/msisdn/(?P<msisdn>[\w\d_.-]+)/$" % self._meta.resource_name, self.wrap_view('dispatch_detail'), name="api_dispatch_detail"),
        ]

class QuizResponseResource(ModelResource):
    quiz = fields.ForeignKey("quiz.api.QuizResource", 'quiz', full=True)
    question = fields.ForeignKey("quiz.api.QuestionResource", 'question', full=True)
    created_by = fields.ForeignKey("usersvumigo.api.VumiGoUserResource", 'created_by', full=True)

    class Meta:
        queryset = QuizResponse.objects.all()
        resource_name = "quizresponses"
        list_allowed_methods = ['post', 'get'] 
        include_resource_uri = True
        always_return_data = True
        authorization = Authorization()
