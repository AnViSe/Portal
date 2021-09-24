from django.views import generic
from rest_framework import viewsets

from apps.references.models import Country
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
        context = super().get_context_data(**kwargs)
        context['route_list_api'] = self.model.Params.route_list_api
        context['fields_list'] = self.model.Params.fields_list
        if self.action_field not in context['fields_list']:
            context['fields_list'].append(self.action_field)
        return context
