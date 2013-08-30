from tastypie.resources import ModelResource
from services.models import Service
from tastypie.authorization import Authorization


class ServiceResource(ModelResource):
    class Meta:
        queryset = Service.objects.all()
        resource_name = "services"
        list_allowed_methods = ['get'] 
        include_resource_uri = True
        always_return_data = True
        authorization = Authorization()
