from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views import generic
from rest_framework import viewsets

from apps.references.models.building import Building
from apps.references.serializers import BuildingSerializer
from apps.references.utils import RefTableMixin


class BuildingViewSet(viewsets.ModelViewSet):
    """Список зданий"""

    queryset = Building.objects.all()
    serializer_class = BuildingSerializer


class BuildingList(PermissionRequiredMixin, RefTableMixin, generic.ListView):
    """Справочник зданий"""

    permission_required = 'references.view_building'

    model = Building

    def get_context_data(self, *, object_list=None, **kwargs):
        context = self.update_context_data(super().get_context_data(**kwargs))
        return context
