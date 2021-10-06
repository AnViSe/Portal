from django.urls import path, include
from rest_framework import routers

from apps.references.views import *

router = routers.DefaultRouter()

router.register(r'employee', EmployeeViewSet)
# router.register(r'country', CountryViewSet)
# router.register(r'region', RegionViewSet)
router.register(r'person', PersonViewSet)
# router.register(r'subdivision', SubdivisionViewSet)
router.register(r'subdivision', SubdivisionTreeViewSet)

urlpatterns = [
    path('', include(router.urls))
]
