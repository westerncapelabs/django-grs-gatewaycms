from tastypie.resources import ModelResource, ALL
from gopher.models import RequestAirtimeSend, AirtimeApplication
from tastypie import fields
from tastypie.authorization import Authorization


class AirtimeApplicationResource(ModelResource):
    """
    To get the required app id
    GET:
    /api/v1/request/application/?name=test_application
    """
    class Meta:
        resource_name = "request/application"
        queryset = AirtimeApplication.objects.all()
        include_resource_uri = True
        always_return_data = True
        list_allowed_methods = ['get']
        filtering = {
            'name': ALL}


class RequestAirtimeSendResource(ModelResource):
    """
    POST:
        url:
            /api/v1/request/airtime/
        data:
        {
        "msisdn": "27721231234",
        "product_key": "VOD",
        "amount": 500,
        "request_application": "/api/v1/request/application/1/"
    }
    """

    request_application = fields.ForeignKey(AirtimeApplicationResource,
                                            'request_application',
                                            full=True)

    class Meta:
        queryset = RequestAirtimeSend.objects.all()
        resource_name = "request/airtime"
        list_allowed_methods = ['post', 'get']
        include_resource_uri = True
        always_return_data = True
        authorization = Authorization()