from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from rest_framework import viewsets

from apps.references.forms import AddressForm
from apps.references.models.address import Address
from apps.references.serializers import AddressSerializer
from apps.references.mixins import *


class AddressViewSet(RefModelViewMixin, viewsets.ModelViewSet):
    """Список адресов"""

    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AddressList(PermissionRequiredMixin, RefListViewMixin, generic.ListView):
    """Справочник адресов"""

    permission_required = 'references.view_address'

    model = Address

    def get_context_data(self, *, object_list=None, **kwargs):
        context = self.update_context_data(super().get_context_data(**kwargs))
        return context


class AddressCreate(PermissionRequiredMixin, RefCreateViewMixin, generic.CreateView):
    """Создание адреса"""

    permission_required = 'references.add_address'

    form_class = AddressForm

    success_url = reverse_lazy('addresses')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj_name'] = Address._meta.verbose_name
        return context


class AddressEdit(PermissionRequiredMixin, RefUpdateViewMixin, generic.UpdateView):
    """Изменение адреса"""

    permission_required = 'references.change_employee'

    model = Address
    form_class = AddressForm

    success_url = reverse_lazy(model.Params.route_list)


class AddressView(RefDetailViewMixin, generic.DetailView):
    """Просмотр адреса"""

    model = Address
    queryset = Address.objects.select_related('building')
