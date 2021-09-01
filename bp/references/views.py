from django.shortcuts import render
from django.views import generic
from rest_framework import viewsets

from references.models import Employee
from references.serializers import EmployeeSerializer


def index(request):
    return render(request, template_name='references/index.html')


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeList(generic.ListView):
    model = Employee
    template_name = 'references/ref_list.html'
