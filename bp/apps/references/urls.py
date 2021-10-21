from django.contrib.auth.decorators import login_required
from django.urls import include, path

from apps.references.views import index
from apps.references.views.country import CountryList
from apps.references.views.district import DistrictList
from apps.references.views.employee import EmployeeList, EmployeeCreate, EmployeeEdit, EmployeeView
from apps.references.views.location import LocationList
from apps.references.views.person import PersonList, PersonCreate, PersonEdit
from apps.references.views.phone import PhoneList
from apps.references.views.region import RegionList
from apps.references.views.subdivision import SubdivisionList, SubdivisionCreate, SubdivisionEdit

urlpatterns = [
    path('', login_required(index), name='refs'),



    path('employees/', login_required(EmployeeList.as_view()), name='employees'),
    # path('employees/', include([
    #     path('create/', login_required(EmployeeCreate.as_view()), name='add_employee'),
    #     path('<int:pk>/', login_required(EmployeeEdit.as_view()), name='edit_employee'),
    #     path('<int:pk>/view/', login_required(EmployeeView.as_view()), name='view_employee'),
    # ])),


    path('persons/', PersonList.as_view(), name='persons'),
    # path('persons/', include([
    #     path('create/', PersonCreate.as_view(), name='add_person'),
    #     path('<int:pk>/', PersonEdit.as_view(), name='edit_person'),
    # ])),

    path('phones/', PhoneList.as_view(), name='phones'),

    path('subdivisions/', SubdivisionList.as_view(), name='subdivisions'),
    # path('subdivisions/', include([
    #     path('create/', login_required(SubdivisionCreate.as_view()), name='add_subdivision'),
    #     path('<int:pk>/', login_required(SubdivisionEdit.as_view()), name='edit_subdivision'),
        # path('<int:pk>/view/', login_required(EmployeeView.as_view()), name='view_subdivision'),
    # ])),
    path('countries/', login_required(CountryList.as_view()), name='countries'),
    path('regions/', login_required(RegionList.as_view()), name='regions'),
    path('districts/', login_required(DistrictList.as_view()), name='districts'),
    path('locations/', login_required(LocationList.as_view()), name='locations'),

]
