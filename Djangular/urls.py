from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from rest_framework import viewsets, routers

'''
#django rest framework example

from django.contrib.auth.models import User, Group

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    model = User

class GroupViewSet(viewsets.ModelViewSet):
    model = Group

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
'''

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Djangular.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #rest framework example
    #url(r'^', include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

    url(r'^admin/', include(admin.site.urls)),
)
