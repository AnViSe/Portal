from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import *

urlpatterns = [
    path('', login_required(index), name='refs'),
    path('employees/', login_required(EmployeeList.as_view()), name='employees'),
    path('employees/create/', login_required(EmployeeCreate.as_view()), name='add_employees'),
    path('employees/<int:pk>/', login_required(EmployeeEdit .as_view()), name='edit_employee'),
    path('employees/<int:pk>/view/', login_required(EmployeeView .as_view()), name='view_employee'),
    path('countries/', login_required(CountryList.as_view()), name='countries'),
    path('regions/', login_required(RegionList.as_view()), name='regions'),
]
