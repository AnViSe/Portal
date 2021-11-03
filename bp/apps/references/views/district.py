from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from rest_framework import viewsets

from apps.references.forms import DistrictForm
from apps.references.models.district import District
from apps.references.serializers import DistrictSerializer
from apps.references.mixins import *


class DistrictViewSet(RefModelViewMixin, viewsets.ModelViewSet):
    """Список районов"""

    queryset = District.objects.select_related('region').all()
    serializer_class = DistrictSerializer


class DistrictList(PermissionRequiredMixin, RefListViewMixin, generic.ListView):
    """Справочник районов"""

    permission_required = 'references.view_district'

    model = District

    def get_context_data(self, *, object_list=None, **kwargs):
        context = self.update_context_data(super().get_context_data(**kwargs))
        return context


class DistrictCreate(PermissionRequiredMixin, RefCreateViewMixin, generic.CreateView):
    """Создание района"""

    permission_required = 'references.add_district'

    form_class = DistrictForm

    success_url = reverse_lazy('districts')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj_name'] = District._meta.verbose_name
        return context


class DistrictEdit(PermissionRequiredMixin, RefUpdateViewMixin, generic.UpdateView):
    """Изменение района"""

    permission_required = 'references.change_district'

    model = District
    form_class = DistrictForm

    success_url = reverse_lazy(model.Params.route_list)


class DistrictView(RefDetailViewMixin, generic.DetailView):
    """Просмотр района"""

    model = District
    queryset = District.objects.select_related('region')
