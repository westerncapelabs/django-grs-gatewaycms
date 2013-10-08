from tastypie.resources import ModelResource
from tastypie import fields
from services.models import Service, Category
from tastypie.authorization import Authorization


# class ServiceResource(ModelResource):
#     class Meta:
#         queryset = Category.objects.all()
#         resource_name = "services"
#         list_allowed_methods = ['get'] 
#         include_resource_uri = True
#         always_return_data = True
#         authorization = Authorization()



class CategoryResource(ModelResource):
    services = fields.ToManyField("services.api.ServiceResource",
                                   'services', full=True)


    class Meta:
        queryset = Category.objects.all()
        resource_name = "category"
        list_allowed_methods = ['get']
        include_resource_uri = True
        always_return_data = True

    def get_object_list(self, request):
        query = super(CategoryResource, self).get_object_list(request)
        return query

class ServiceResource(ModelResource):
    class Meta:
        queryset = Service.objects.all()
        include_resource_uri = False
