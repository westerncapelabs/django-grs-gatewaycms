from tastypie.resources import ModelResource
from usersvumigo.models import VumiGoUser



class VumiGoUserResource(ModelResource):
    class Meta:
        queryset = VumiGoUser.objects.all()
        resource_name = "users"
        list_allowed_methods = ['post', 'get'] 
        include_resource_uri = True
        always_return_data = True