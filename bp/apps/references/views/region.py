from django.views import generic
from rest_framework import viewsets

from apps.references.models import Region
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
        context = super().get_context_data(**kwargs)
        context['route_list_api'] = self.model.Params.route_list_api
        context['fields_list'] = self.model.Params.fields_list
        return context
