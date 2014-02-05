from django.conf.urls import patterns, include, url

from django.contrib import admin

from django.views.generic import TemplateView
admin.autodiscover()

from backend.api import PersonResource

person_resource = PersonResource()
urlpatterns = patterns('',
    # Examples:
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^api/', include(person_resource.urls)),

    url(r'^admin/', include(admin.site.urls)),
)
