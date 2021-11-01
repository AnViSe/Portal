from django.urls import path, include
from rest_framework import routers

from apps.references.views.address import AddressViewSet
from apps.references.views.building import BuildingViewSet
from apps.references.views.country import CountryViewSet
from apps.references.views.district import DistrictViewSet
from apps.references.views.employee import EmployeeViewSet
from apps.references.views.location import LocationViewSet
from apps.references.views.person import PersonViewSet
from apps.references.views.phone import PhoneViewSet
from apps.references.views.postoffice import PostOfficeViewSet
from apps.references.views.region import RegionViewSet
from apps.references.views.street import StreetViewSet
from apps.references.views.subdivision import SubdivisionViewSet

router = routers.DefaultRouter()
# router = routers.SimpleRouter()
# routerTree = routers.DefaultRouter()

router.register(r'country', CountryViewSet)
router.register(r'region', RegionViewSet)
router.register(r'district', DistrictViewSet)
router.register(r'location', LocationViewSet)
router.register(r'street', StreetViewSet)
router.register(r'building', BuildingViewSet)
router.register(r'address', AddressViewSet)

router.register(r'subdivision', SubdivisionViewSet)
router.register(r'postoffice', PostOfficeViewSet)
router.register(r'employee', EmployeeViewSet)
router.register(r'person', PersonViewSet)
router.register(r'phone', PhoneViewSet)


# routerTree.register(r'subdivision', SubdivisionTreeViewSet)
# router.register(r'person/tree', PersonViewSet, basename='person-tree')
# router.register(r'subdivision', SubdivisionTreeViewSet)

urlpatterns = [
    # path('tree/', include(routerTree.urls)),
    path('', include(router.urls))
]
