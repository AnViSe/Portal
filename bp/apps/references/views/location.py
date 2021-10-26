from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views import generic
from rest_framework import viewsets

from apps.references.models.location import Location
from apps.references.serializers import LocationSerializer
from apps.references.utils import RefTableMixin


class LocationViewSet(viewsets.ModelViewSet):
    """Список населенных пунктов"""

    queryset = Location.objects.select_related('district').all()
    serializer_class = LocationSerializer


class LocationList(PermissionRequiredMixin, RefTableMixin, generic.ListView):
    """Справочник населенных пунктов"""

    permission_required = 'references.view_location'

    model = Location

    def get_context_data(self, *, object_list=None, **kwargs):
        context = self.update_context_data(super().get_context_data(**kwargs))
        return context
