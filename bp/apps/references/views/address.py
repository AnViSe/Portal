from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from rest_framework import viewsets

from apps.references.forms import AddressForm
from apps.references.models.address import Address
from apps.references.serializers import AddressSerializer
from apps.references.utils import RefTableMixin


class AddressViewSet(viewsets.ModelViewSet):
    """Список адресов"""

    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AddressList(PermissionRequiredMixin, RefTableMixin, generic.ListView):
    """Справочник адресов"""

    permission_required = 'references.view_address'

    model = Address

    def get_context_data(self, *, object_list=None, **kwargs):
        context = self.update_context_data(super().get_context_data(**kwargs))
        return context


class AddressCreate(PermissionRequiredMixin, generic.CreateView):
    """Создание адреса"""

    permission_required = 'references.add_address'

    form_class = AddressForm
    template_name = 'references/ref_add.html'
    success_url = reverse_lazy('addresses')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj_name'] = Address._meta.verbose_name
        return context


class AddressEdit(PermissionRequiredMixin, generic.UpdateView):
    """Изменение адреса"""

    permission_required = 'references.change_employee'

    model = Address
    form_class = AddressForm
    template_name = 'references/ref_edit.html'
    success_url = reverse_lazy(model.Params.route_list)
