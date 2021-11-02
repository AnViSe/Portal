from django.contrib.auth.decorators import login_required
from django.urls import include, path

from apps.references.views import index
from apps.references.views.address import AddressList, AddressCreate, AddressEdit, AddressView
from apps.references.views.building import BuildingCreate, BuildingEdit, BuildingList, BuildingView
from apps.references.views.country import CountryList
from apps.references.views.district import DistrictList
from apps.references.views.employee import EmployeeList, EmployeeCreate, EmployeeEdit, EmployeeView
from apps.references.views.location import LocationCreate, LocationEdit, LocationList, LocationView
from apps.references.views.person import PersonList, PersonCreate, PersonEdit
from apps.references.views.phone import PhoneList
from apps.references.views.postoffice import PostOfficeList
from apps.references.views.region import RegionList
from apps.references.views.street import StreetList
from apps.references.views.subdivision import SubdivisionList, SubdivisionCreate, SubdivisionEdit

urlpatterns = [
    path('', login_required(index), name='refs'),

    path('addresses/', include([
        path('', login_required(AddressList.as_view()), name='addresses'),
        path('create/', login_required(AddressCreate.as_view()), name='add_address'),
        path('<int:pk>/', login_required(AddressEdit.as_view()), name='edit_address'),
        path('<int:pk>/view/', login_required(AddressView.as_view()), name='view_address'),
    ])),

    path('buildings/', include([
        path('', login_required(BuildingList.as_view()), name='buildings'),
        path('create/', login_required(BuildingCreate.as_view()), name='add_building'),
        path('<int:pk>/', login_required(BuildingEdit.as_view()), name='edit_building'),
        path('<int:pk>/view/', login_required(BuildingView.as_view()), name='view_building'),
    ])),

    path('employees/', include([
        path('', login_required(EmployeeList.as_view()), name='employees'),
        path('create/', login_required(EmployeeCreate.as_view()), name='add_employee'),
        path('<int:pk>/', login_required(EmployeeEdit.as_view()), name='edit_employee'),
        path('<int:pk>/view/', login_required(EmployeeView.as_view()), name='view_employee'),
    ])),

    path('locations/', include([
        path('', login_required(LocationList.as_view()), name='locations'),
        path('create/', login_required(LocationCreate.as_view()), name='add_location'),
        path('<int:pk>/', login_required(LocationEdit.as_view()), name='edit_location'),
        path('<int:pk>/view/', login_required(LocationView.as_view()), name='view_location'),
    ])),

    path('persons/', include([
        path('', login_required(PersonList.as_view()), name='persons'),
        path('create/', login_required(PersonCreate.as_view()), name='add_person'),
        path('<int:pk>/', login_required(PersonEdit.as_view()), name='edit_person'),
    ])),

    path('phones/', login_required(PhoneList.as_view()), name='phones'),
    path('postoffices/', login_required(PostOfficeList.as_view()), name='postoffices'),

    path('subdivisions/', include([
        path('', login_required(SubdivisionList.as_view()), name='subdivisions'),
        path('create/', login_required(SubdivisionCreate.as_view()), name='add_subdivision'),
        path('<int:pk>/', login_required(SubdivisionEdit.as_view()), name='edit_subdivision'),
        path('<int:pk>/view/', login_required(EmployeeView.as_view()), name='view_subdivision'),
    ])),

    path('countries/', include([
        path('', login_required(CountryList.as_view()), name='countries'),
    ])),

    path('regions/', include([
        path('', login_required(RegionList.as_view()), name='regions'),
    ])),

    path('districts/', include([
        path('', login_required(DistrictList.as_view()), name='districts'),
    ])),

    path('streets/', include([
        path('', login_required(StreetList.as_view()), name='streets'),
    ])),

]
