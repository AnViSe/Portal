from django.urls import path, include
from rest_framework import routers

from apps.references.views.employee import EmployeeViewSet
from apps.references.views.person import PersonViewSet

router = routers.DefaultRouter()
# routerTree = routers.DefaultRouter()


router.register(r'employee', EmployeeViewSet)
# router.register(r'country', CountryViewSet)
# router.register(r'region', RegionViewSet)
# router.register(r'person/tree', PersonViewSet, basename='person-tree')
router.register(r'person', PersonViewSet)
# router.register(r'subdivision', SubdivisionViewSet)

# routerTree.register(r'person', PersonViewSet)
# routerTree.register(r'subdivision', SubdivisionTreeViewSet)


urlpatterns = [
    # path('tree/', include(routerTree.urls)),
    path('', include(router.urls))
]
