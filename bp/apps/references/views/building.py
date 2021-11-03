from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from rest_framework import viewsets

from apps.references.forms import BuildingForm
from apps.references.models.building import Building
from apps.references.serializers import BuildingSerializer
from apps.references.mixins import *


class BuildingViewSet(RefModelViewMixin, viewsets.ModelViewSet):
    """Список зданий"""

    queryset = Building.objects.all()
    serializer_class = BuildingSerializer


class BuildingList(PermissionRequiredMixin, RefListViewMixin, generic.ListView):
    """Справочник зданий"""

    permission_required = 'references.view_building'

    model = Building

    def get_context_data(self, *, object_list=None, **kwargs):
        context = self.update_context_data(super().get_context_data(**kwargs))
        return context


class BuildingCreate(PermissionRequiredMixin, RefCreateViewMixin, generic.CreateView):
    """Создание здания"""

    permission_required = 'references.add_building'

    form_class = BuildingForm

    success_url = reverse_lazy('buildings')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj_name'] = Building._meta.verbose_name
        return context


class BuildingEdit(PermissionRequiredMixin, RefUpdateViewMixin, generic.UpdateView):
    """Изменение здания"""

    permission_required = 'references.change_building'

    model = Building
    form_class = BuildingForm

    success_url = reverse_lazy(model.Params.route_list)


class BuildingView(RefDetailViewMixin, generic.DetailView):
    """Просмотр здания"""

    model = Building
    queryset = Building.objects.select_related('region')
