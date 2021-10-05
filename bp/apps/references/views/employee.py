from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from rest_framework import viewsets

from apps.references.forms import EmployeeForm
from apps.references.models.employee import Employee
from apps.references.serializers import EmployeeSerializer
from apps.references.utils import RefTableMixin


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.select_related('person', 'subdivision').all()
    serializer_class = EmployeeSerializer


class EmployeeList(RefTableMixin, generic.ListView):
    model = Employee

    # PermissionRequiredMixin, <== Добавить в класс первым
    # permission_required = 'references.view_employee'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['route_list_api'] = self.model.Params.route_list_api
        context['fields_list'] = self.model.Params.fields_list
        if self.action_field not in context['fields_list']:
            context['fields_list'].append(self.action_field)
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
