from tastypie.resources import ModelResource, ALL
from gopher.models import RequestAirtimeSend
from tastypie import fields
from tastypie.authorization import Authorization


class RequestAirtimeSendResource(ModelResource):
    class Meta:
        queryset = RequestAirtimeSend.objects.all()
        resource_name = "request/airtime"
        list_allowed_methods = ['post', 'get']
        include_resource_uri = True
        always_return_data = True
        authorization = Authorization()