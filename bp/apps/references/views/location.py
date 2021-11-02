from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from rest_framework import viewsets

from apps.references.forms import LocationAdminForm, LocationForm
from apps.references.models.location import Location
from apps.references.serializers import LocationSerializer
from apps.references.utils import *


class LocationViewSet(RefModelViewMixin, viewsets.ModelViewSet):
    """Список населенных пунктов"""

    queryset = Location.objects.select_related('district').all()
    serializer_class = LocationSerializer


class LocationList(PermissionRequiredMixin, RefListViewMixin, generic.ListView):
    """Справочник населенных пунктов"""

    permission_required = 'references.view_location'

    model = Location

    def get_context_data(self, *, object_list=None, **kwargs):
        context = self.update_context_data(super().get_context_data(**kwargs))
        return context


class LocationCreate(PermissionRequiredMixin, RefCreateViewMixin, generic.CreateView):
    """Создание населенного пункта"""

    permission_required = 'references.add_location'

    form_class = LocationForm

    success_url = reverse_lazy('locations')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj_name'] = Location._meta.verbose_name
        return context


class LocationEdit(PermissionRequiredMixin, RefUpdateViewMixin, generic.UpdateView):
    """Изменение населенного пункта"""

    permission_required = 'references.change_location'

    model = Location
    # form_class = LocationAdminForm
    form_class = LocationForm

    success_url = reverse_lazy(model.Params.route_list)


class LocationView(RefDetailViewMixin, generic.DetailView):
    """Просмотр населенного пункта"""

    model = Location
    queryset = Location.objects.select_related('district')
