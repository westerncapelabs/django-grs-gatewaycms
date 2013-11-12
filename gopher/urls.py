from django.conf.urls import patterns, url, include
from tastypie.api import Api
from gopher.api import RequestAirtimeSendResource, AirtimeApplicationResource


api_resources = Api(api_name='v1')
api_resources.register(RequestAirtimeSendResource())
api_resources.register(AirtimeApplicationResource())
api_resources.prepend_urls()

# Setting the urlpatterns to hook into the api urls
urlpatterns = patterns('',
    url(r'^api/', include(api_resources.urls))
)
