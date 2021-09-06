from django.urls import path, include
from rest_framework import routers

from references.views import EmployeeViewSet, CountryViewSet, RegionViewSet

router = routers.DefaultRouter()

router.register(r'employee', EmployeeViewSet)
router.register(r'country', CountryViewSet)
router.register(r'region', RegionViewSet)

urlpatterns = [
    path('', include(router.urls))
]
