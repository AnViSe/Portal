from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from rest_framework import viewsets

from apps.references.forms import RegionForm
from apps.references.models.region import Region
from apps.references.serializers import RegionSerializer
from apps.references.mixins import *


class RegionViewSet(RefModelViewMixin, viewsets.ModelViewSet):
    """Список областей"""

    queryset = Region.objects.select_related('country').all()
    serializer_class = RegionSerializer


class RegionList(PermissionRequiredMixin, RefListViewMixin, generic.ListView):
    """Справочник областей"""

    permission_required = 'references.view_region'

    model = Region

    def get_context_data(self, *, object_list=None, **kwargs):
        context = self.update_context_data(super().get_context_data(**kwargs))
        return context


class RegionCreate(PermissionRequiredMixin, RefCreateViewMixin, generic.CreateView):
    """Создание района"""

    permission_required = 'references.add_region'

    form_class = RegionForm

    success_url = reverse_lazy('districts')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj_name'] = Region._meta.verbose_name
        return context


class RegionEdit(PermissionRequiredMixin, RefUpdateViewMixin, generic.UpdateView):
    """Изменение района"""

    permission_required = 'references.change_region'

    model = Region
    form_class = RegionForm

    success_url = reverse_lazy(model.Params.route_list)


class RegionView(RefDetailViewMixin, generic.DetailView):
    """Просмотр района"""

    model = Region
    queryset = Region.objects.select_related('country')
