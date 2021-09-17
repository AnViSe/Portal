from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from rest_framework import viewsets

from references.forms import EmployeeForm
from references.models import Employee
from references.serializers import EmployeeSerializer
from references.utils import RefTableMixin


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeList(RefTableMixin, generic.ListView):
    model = Employee
    # template_name = 'references/ref_list.html'
    # PermissionRequiredMixin, <== Добавить в класс первым
    # permission_required = 'references.view_employee'
    # url_list = 'employee-list'
    field_list = [
        {'name': 'id', 'title': 'Код'},
        {'name': 'lastname', 'title': 'Фамилия'},
        {'name': 'firstname', 'title': 'Имя'},
        {'name': 'middlename', 'title': 'Отчество'},
        {'name': 'name_lfm', 'title': 'Фамилия И.О.'},
        {"name": None, "title": "Операции"},
    ]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_list'] = self.get_url(model=self.model)
        # context['field_list'] = self.get_columns(model=self.model)
        context['field_list'] = self.get_columns()
        return context


class EmployeeView(generic.DetailView):
    model = Employee
    # form_class = EmployeeForm
    template_name = 'references/ref_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # fields = get_columns(self.model)
        # for field in fields:
        #     field['value'] = self.model.serializable_value(self, field['name'])
        # context['fields'] = fields
        return context


class EmployeeCreate(PermissionRequiredMixin, generic.CreateView):
    permission_required = 'references.add_employee'
    form_class = EmployeeForm
    template_name = 'references/ref_add.html'
    success_url = reverse_lazy('employees')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj_name'] = Employee._meta.verbose_name
        return context


class EmployeeEdit(generic.UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'references/ref_edit.html'
    success_url = reverse_lazy('employees')


class EmployeeDelete(generic.DeleteView):
    model = Employee
