from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from rest_framework import viewsets

from apps.references.forms import EmployeeForm
from apps.references.models.employee import Employee
from apps.references.serializers import EmployeeSerializer
from apps.references.utils import *


class EmployeeViewSet(RefModelViewMixin, viewsets.ModelViewSet):
    """Список сотрудников"""

    queryset = Employee.objects.select_related('person', 'subdivision').all()
    serializer_class = EmployeeSerializer


class EmployeeList(PermissionRequiredMixin, RefListViewMixin, generic.ListView):
    """Справочник сотрудников"""

    permission_required = 'references.view_employee'

    model = Employee

    def get_context_data(self, *, object_list=None, **kwargs):
        context = self.update_context_data(super().get_context_data(**kwargs))
        return context


class EmployeeView(RefDetailViewMixin, generic.DetailView):
    """Просмотр сотрудника"""

    model = Employee
    queryset = Employee.objects.select_related('subdivision')


class EmployeeCreate(PermissionRequiredMixin, RefCreateViewMixin, generic.CreateView):
    """Создание сотрудника"""

    permission_required = 'references.add_employee'

    form_class = EmployeeForm

    success_url = reverse_lazy('employees')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj_name'] = Employee._meta.verbose_name
        return context


class EmployeeEdit(PermissionRequiredMixin, RefUpdateViewMixin, generic.UpdateView):
    """Изменение сотрудника"""

    permission_required = 'references.change_employee'

    model = Employee
    form_class = EmployeeForm

    success_url = reverse_lazy(model.Params.route_list)


class EmployeeDelete(PermissionRequiredMixin, generic.DeleteView):
    """Удаление сотрудника"""

    permission_required = 'references.delete_employee'

    model = Employee
