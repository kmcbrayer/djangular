from django.conf.urls import patterns, include, url

from tastypie.api import Api 

from api import PersonResource

person_resource = PersonResource()

urlpatterns = patterns('',
	url(r'^api/', include(person_resource.urls)),
)