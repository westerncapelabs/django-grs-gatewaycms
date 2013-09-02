from django.conf.urls import patterns, url, include
from tastypie.api import Api
from quiz.api import QuizResource

api_resources = Api(api_name='v1')
api_resources.register(QuizResource())


# Setting the urlpatterns to hook into the api urls
urlpatterns = patterns('',
    url(r'^api/', include(api_resources.urls))
)
