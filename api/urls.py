from django.conf.urls import patterns, include, url

from models import Person

from rest_framework import viewsets, routers

#ViewSets define the view behavior
class PersonViewSet(viewsets.ModelViewSet):
    model = Person

router = routers.DefaultRouter()
router.register(r'persons',PersonViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    )