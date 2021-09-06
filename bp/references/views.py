from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.views import generic
from rest_framework import viewsets

from references.models import Employee, Country, Region
from references.serializers import EmployeeSerializer, CountrySerializer, RegionSerializer

from references.utils import RefTableMixin


def index(request):
    return render(request, template_name='references/index.html')


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeList(RefTableMixin, generic.ListView):
    model = Employee
    # template_name = 'references/ref_list.html'
    # PermissionRequiredMixin, <== Добавить в класс первым
    # permission_required = 'references.view_employee'
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


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryList(RefTableMixin, generic.ListView):
    model = Country
    # template_name = 'references/ref_list.html'
    # PermissionRequiredMixin, <== Добавить в класс первым
    # permission_required = 'references.view_country'
    url_list = 'country-list'
    field_list = [
        {'name': 'id', 'title': 'Код'},
        {'name': 'code', 'title': 'Код1'},
        {'name': 'name', 'title': 'Наименование'},
        {'name': 'alpha2', 'title': 'ISO2'},
        {'name': 'alpha3', 'title': 'ISO3'},
        {"name": None, "title": "Actions"},
    ]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_list'] = self.get_url(model=self.model)
        # context['field_list'] = self.get_columns(model=self.model)
        context['field_list'] = self.get_columns()
        return context


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.select_related('country').all()
    serializer_class = RegionSerializer


class RegionList(RefTableMixin, generic.ListView):
    model = Region
    # template_name = 'references/ref_list.html'
    # PermissionRequiredMixin, <== Добавить в класс первым
    # permission_required = 'references.view_region'
    url_list = 'region-list'
    field_list = [
        {'name': 'id', 'title': 'Код'},
        {'name': 'code', 'title': 'Код1'},
        {'name': 'name', 'title': 'Наименование'},
        {'name': 'country', 'title': 'Страна'},
        {"name": None, "title": "Actions"},
    ]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_list'] = self.get_url(model=self.model)
        # context['field_list'] = self.get_columns(model=self.model)
        context['field_list'] = self.get_columns()
        return context
