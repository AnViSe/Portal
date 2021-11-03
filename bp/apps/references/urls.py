from django.contrib.auth.decorators import login_required
from django.urls import include, path

from apps.references.views import index
from apps.references.views.address import AddressList, AddressCreate, AddressEdit, AddressView
from apps.references.views.building import BuildingCreate, BuildingEdit, BuildingList, BuildingView
from apps.references.views.country import CountryCreate, CountryEdit, CountryList, CountryView
from apps.references.views.district import DistrictCreate, DistrictEdit, DistrictList, DistrictView
from apps.references.views.employee import EmployeeList, EmployeeCreate, EmployeeEdit, EmployeeView
from apps.references.views.location import LocationCreate, LocationEdit, LocationList, LocationView
from apps.references.views.person import PersonList, PersonCreate, PersonEdit, PersonView
from apps.references.views.phone import PhoneCreate, PhoneEdit, PhoneList, PhoneView
from apps.references.views.postoffice import PostOfficeCreate, PostOfficeEdit, PostOfficeList, \
    PostOfficeView
from apps.references.views.region import RegionCreate, RegionEdit, RegionList, RegionView
from apps.references.views.street import StreetCreate, StreetEdit, StreetList, StreetView
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

    path('countries/', include([
        path('', login_required(CountryList.as_view()), name='countries'),
        path('create/', login_required(CountryCreate.as_view()), name='add_country'),
        path('<int:pk>/', login_required(CountryEdit.as_view()), name='edit_country'),
        path('<int:pk>/view/', login_required(CountryView.as_view()), name='view_country'),
    ])),

    path('districts/', include([
        path('', login_required(DistrictList.as_view()), name='districts'),
        path('create/', login_required(DistrictCreate.as_view()), name='add_district'),
        path('<int:pk>/', login_required(DistrictEdit.as_view()), name='edit_district'),
        path('<int:pk>/view/', login_required(DistrictView.as_view()), name='view_district'),
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
        path('<int:pk>/view/', login_required(PersonView.as_view()), name='view_person'),
    ])),

    path('phones/', include([
        path('', login_required(PhoneList.as_view()), name='phones'),
        path('create/', login_required(PhoneCreate.as_view()), name='add_phone'),
        path('<int:pk>/', login_required(PhoneEdit.as_view()), name='edit_phone'),
        path('<int:pk>/view/', login_required(PhoneView.as_view()), name='view_phone'),
    ])),

    path('postoffices/', include([
        path('', login_required(PostOfficeList.as_view()), name='postoffices'),
        path('create/', login_required(PostOfficeCreate.as_view()), name='add_postoffice'),
        path('<int:pk>/', login_required(PostOfficeEdit.as_view()), name='edit_postoffice'),
        path('<int:pk>/view/', login_required(PostOfficeView.as_view()), name='view_postoffice'),
    ])),

    path('regions/', include([
        path('', login_required(RegionList.as_view()), name='regions'),
        path('create/', login_required(RegionCreate.as_view()), name='add_region'),
        path('<int:pk>/', login_required(RegionEdit.as_view()), name='edit_region'),
        path('<int:pk>/view/', login_required(RegionView.as_view()), name='view_region'),
    ])),

    path('streets/', include([
        path('', login_required(StreetList.as_view()), name='streets'),
        path('create/', login_required(StreetCreate.as_view()), name='add_street'),
        path('<int:pk>/', login_required(StreetEdit.as_view()), name='edit_street'),
        path('<int:pk>/view/', login_required(StreetView.as_view()), name='view_street'),
    ])),

    path('subdivisions/', include([
        path('', login_required(SubdivisionList.as_view()), name='subdivisions'),
        path('create/', login_required(SubdivisionCreate.as_view()), name='add_subdivision'),
        path('<int:pk>/', login_required(SubdivisionEdit.as_view()), name='edit_subdivision'),
        path('<int:pk>/view/', login_required(EmployeeView.as_view()), name='view_subdivision'),
    ])),

]
