from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('quiz.urls')),
    url(r'^', include('services.urls')),
    url(r'^', include('usersvumigo.urls')),
    url(r'^', include('gopher.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

)
