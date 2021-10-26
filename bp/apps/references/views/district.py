from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views import generic
from rest_framework import viewsets

from apps.references.models.district import District
from apps.references.serializers import DistrictSerializer
from apps.references.utils import RefTableMixin


class DistrictViewSet(viewsets.ModelViewSet):
    """Список районов"""

    queryset = District.objects.select_related('region').all()
    serializer_class = DistrictSerializer


class DistrictList(PermissionRequiredMixin, RefTableMixin, generic.ListView):
    """Справочник районов"""

    permission_required = 'references.view_region'

    model = District

    def get_context_data(self, *, object_list=None, **kwargs):
        context = self.update_context_data(super().get_context_data(**kwargs))
        return context
