from django.urls import path, include
from rest_framework import routers

from apps.references.views.employee import EmployeeViewSet
from apps.references.views.person import PersonViewSet

router = routers.DefaultRouter()

router.register(r'employee', EmployeeViewSet)
# router.register(r'country', CountryViewSet)
# router.register(r'region', RegionViewSet)
router.register(r'person', PersonViewSet)
# router.register(r'subdivision', SubdivisionViewSet)


urlpatterns = [
    path('', include(router.urls))
]
