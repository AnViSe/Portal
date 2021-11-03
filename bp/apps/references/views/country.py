from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from rest_framework import viewsets

from apps.references.forms import CountryForm
from apps.references.models.country import Country
from apps.references.serializers import CountrySerializer
from apps.references.mixins import *


class CountryViewSet(RefModelViewMixin, viewsets.ModelViewSet):
    """Список стран"""

    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryList(PermissionRequiredMixin, RefListViewMixin, generic.ListView):
    """Справочник стран"""

    permission_required = 'references.view_country'

    model = Country

    def get_context_data(self, *, object_list=None, **kwargs):
        context = self.update_context_data(super().get_context_data(**kwargs))
        return context


class CountryCreate(PermissionRequiredMixin, RefCreateViewMixin, generic.CreateView):
    """Создание страны"""

    permission_required = 'references.add_country'

    form_class = CountryForm

    success_url = reverse_lazy('countries')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj_name'] = Country._meta.verbose_name
        return context


class CountryEdit(PermissionRequiredMixin, RefUpdateViewMixin, generic.UpdateView):
    """Изменение страны"""

    permission_required = 'references.change_country'

    model = Country
    form_class = CountryForm

    success_url = reverse_lazy(model.Params.route_list)


class CountryView(RefDetailViewMixin, generic.DetailView):
    """Просмотр страны"""

    model = Country
