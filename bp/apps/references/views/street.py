from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from rest_framework import viewsets

from apps.references.forms import StreetForm
from apps.references.models.street import Street
from apps.references.serializers import StreetSerializer
from apps.references.mixins import *


class StreetViewSet(RefModelViewMixin, viewsets.ModelViewSet):
    """Список улиц"""

    queryset = Street.objects.all()
    serializer_class = StreetSerializer


class StreetList(PermissionRequiredMixin, RefListViewMixin, generic.ListView):
    """Справочник улиц"""

    permission_required = 'references.view_street'

    model = Street

    def get_context_data(self, *, object_list=None, **kwargs):
        context = self.update_context_data(super().get_context_data(**kwargs))
        return context


class StreetCreate(PermissionRequiredMixin, RefCreateViewMixin, generic.CreateView):
    """Создание улицы"""

    permission_required = 'references.add_street'

    form_class = StreetForm

    success_url = reverse_lazy('streets')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj_name'] = Street._meta.verbose_name
        return context


class StreetEdit(PermissionRequiredMixin, RefUpdateViewMixin, generic.UpdateView):
    """Изменение улицы"""

    permission_required = 'references.change_street'

    model = Street
    form_class = StreetForm

    success_url = reverse_lazy(model.Params.route_list)


class StreetView(RefDetailViewMixin, generic.DetailView):
    """Просмотр улицы"""

    model = Street
