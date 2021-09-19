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
    # template_name = 'references/ref_list.html'
    # PermissionRequiredMixin, <== Добавить в класс первым
    # permission_required = 'references.view_region'
    url_list = 'region-list'
    field_list = [
        {'name': 'id', 'title': 'Код'},
        {'name': 'code', 'title': 'Код1'},
        {'name': 'name', 'title': 'Наименование'},
        {'name': 'country', 'title': 'Страна'},
        {"name": None, "title": "Операции"},
    ]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_list'] = self.get_url(model=self.model)
        # context['field_list'] = self.get_columns(model=self.model)
        context['field_list'] = self.get_columns()
        return context
