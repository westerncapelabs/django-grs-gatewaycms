from tastypie.resources import ModelResource
from usersvumigo.models import VumiGoUser, QuizResponse
from tastypie import fields
from tastypie.authorization import Authorization



class VumiGoUserResource(ModelResource):
    class Meta:
        queryset = VumiGoUser.objects.all()
        resource_name = "users"
        list_allowed_methods = ['post', 'get'] 
        include_resource_uri = True
        always_return_data = True
        authorization = Authorization()

class QuizResponseResource(ModelResource):
    question = fields.ForeignKey("quiz.api.QuestionResource", 'question', full=True)
    class Meta:
        queryset = QuizResponse.objects.all()
        resource_name = "quizresponses"
        list_allowed_methods = ['post', 'get'] 
        include_resource_uri = True
        always_return_data = True
        authorization = Authorization()
