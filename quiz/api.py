from tastypie.resources import ModelResource
from tastypie import fields
from quiz.models import (Quiz, Question, Answer, FinalResponse)



class QuizResource(ModelResource):
    q_quiz_id = fields.ToManyField("quiz.api.QuestionResource",
                                   'q_quiz_id',
                                    full=True)

    fr_quiz_id = fields.ToManyField("quiz.api.FinalResponseResource",
                                   'fr_quiz_id',
                                    full=True)
    class Meta:
        queryset = Quiz.objects.all()
        resource_name = "quiz"
        list_allowed_methods = ['post', 'get'] 
        include_resource_uri = True
        always_return_data = True

    def get_object_list(self, request):
        query = super(QuizResource, self).get_object_list(request)
        query = query.filter(active=True)
        return query


class QuestionResource(ModelResource):
    question_id = fields.ToManyField("quiz.api.AnswerResource",
                                  'question_id',
                                  full=True)

    class Meta:
        queryset = Question.objects.all()
        include_resource_uri = False


class AnswerResource(ModelResource):
    class Meta:
        queryset = Answer.objects.all()
        include_resource_uri = False


class FinalResponseResource(ModelResource):
    class Meta:
        queryset = FinalResponse.objects.all()
        include_resource_uri = False
