from django.views import generic
from rest_framework import viewsets

from apps.references.models.district import District
from apps.references.serializers import DistrictSerializer
from apps.references.utils import RefTableMixin


class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.select_related('region').all()
    serializer_class = DistrictSerializer


class DistrictList(RefTableMixin, generic.ListView):
    model = District

    # PermissionRequiredMixin, <== Добавить в класс первым
    # permission_required = 'references.view_region'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = self.update_context_data(super().get_context_data(**kwargs))
        return context
