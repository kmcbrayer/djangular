from models import Person

from rest_framework import viewsets, routers

#Init router
router = routers.DefaultRouter()

#ViewSets define the view behavior
class PersonViewSet(viewsets.ModelViewSet):
    model = Person
router.register(r'persons',PersonViewSet)