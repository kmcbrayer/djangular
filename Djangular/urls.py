from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

from api.models import Person

from rest_framework import viewsets, routers

admin.autodiscover()

#ViewSets define the view behavior
class PersonViewSet(viewsets.ModelViewSet):
    model = Person

router = routers.DefaultRouter()
router.register(r'persons',PersonViewSet)

urlpatterns = patterns('',
    # Examples:
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
