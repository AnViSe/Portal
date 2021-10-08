from django.views import generic
from rest_framework import viewsets

from apps.references.models.country import Country
from apps.references.serializers import CountrySerializer
from apps.references.utils import RefTableMixin


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryList(RefTableMixin, generic.ListView):
    model = Country

    # PermissionRequiredMixin, <== Добавить в класс первым
    # permission_required = 'references.view_country'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = self.update_context_data(super().get_context_data(**kwargs))
        return context
