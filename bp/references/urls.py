from django.urls import path

from .views import index, EmployeeList

urlpatterns = [
    path('', index, name='refs'),
    path('employees/', EmployeeList.as_view(), name='employees'),
]
