from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views import generic
from rest_framework import viewsets

from apps.references.models.street import Street
from apps.references.serializers import StreetSerializer
from apps.references.utils import RefTableMixin


class StreetViewSet(viewsets.ModelViewSet):
    """Список улиц"""

    queryset = Street.objects.all()
    serializer_class = StreetSerializer


class StreetList(PermissionRequiredMixin, RefTableMixin, generic.ListView):
    """Справочник улиц"""

    permission_required = 'references.view_street'

    model = Street

    def get_context_data(self, *, object_list=None, **kwargs):
        context = self.update_context_data(super().get_context_data(**kwargs))
        return context
