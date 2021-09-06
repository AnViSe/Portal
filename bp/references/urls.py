from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import index, EmployeeList, CountryList, RegionList

urlpatterns = [
    path('', login_required(index), name='refs'),
    path('employees/', login_required(EmployeeList.as_view()), name='employees'),
    path('countries/', login_required(CountryList.as_view()), name='countries'),
    path('regions/', login_required(RegionList.as_view()), name='regions'),
]
