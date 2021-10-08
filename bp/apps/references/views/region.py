from django.views import generic
from rest_framework import viewsets

from apps.references.models.region import Region
from apps.references.serializers import RegionSerializer
from apps.references.utils import RefTableMixin


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.select_related('country').all()
    serializer_class = RegionSerializer


class RegionList(RefTableMixin, generic.ListView):
    model = Region

    # PermissionRequiredMixin, <== Добавить в класс первым
    # permission_required = 'references.view_region'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = self.update_context_data(super().get_context_data(**kwargs))
        return context
