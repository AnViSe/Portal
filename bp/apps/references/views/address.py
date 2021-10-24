from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views import generic
from rest_framework import viewsets

from apps.references.models.address import Address
from apps.references.serializers import AddressSerializer
from apps.references.utils import RefTableMixin


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AddressList(PermissionRequiredMixin, RefTableMixin, generic.ListView):
    permission_required = 'references.view_address'
    model = Address

    def get_context_data(self, *, object_list=None, **kwargs):
        context = self.update_context_data(super().get_context_data(**kwargs))
        return context