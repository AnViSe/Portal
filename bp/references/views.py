from django.shortcuts import render
from django.views import generic
from rest_framework import viewsets

from references.models import Employee
from references.serializers import EmployeeSerializer

from references.utils import RefTableMixin


def index(request):
    return render(request, template_name='references/index.html')


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeList(RefTableMixin, generic.ListView):
    model = Employee
    # Employee._meta.get_fields(False, False)
    template_name = 'references/ref_list.html'
    url_list = 'employee-list'
    field_list = [
        {'name': 'id', 'title': 'Код'},
        {'name': 'lastname', 'title': 'Фамилия'},
        {'name': 'firstname', 'title': 'Имя'},
        {'name': 'middlename', 'title': 'Отчество'},
        {'name': 'name_lfm', 'title': 'Фамилия И.О.'},
        # {"name": 'actions', "title": "Actions"},
        {"name": None, "title": "Actions"},
    ]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_list'] = self.get_url(model=self.model)
        # context['field_list'] = self.get_columns(model=self.model)
        context['field_list'] = self.get_columns()
        return context
