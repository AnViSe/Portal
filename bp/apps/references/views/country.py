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
    # template_name = 'references/ref_list.html'
    # PermissionRequiredMixin, <== Добавить в класс первым
    # permission_required = 'references.view_country'
    url_list = 'country-list'
    field_list = [
        {'name': 'id', 'title': 'Код'},
        {'name': 'code', 'title': 'Код1'},
        {'name': 'name', 'title': 'Наименование'},
        {'name': 'alpha2', 'title': 'ISO2'},
        {'name': 'alpha3', 'title': 'ISO3'},
        {"name": None, "title": "Операции"},
    ]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_list'] = self.get_url(model=self.model)
        # context['field_list'] = self.get_columns(model=self.model)
        context['field_list'] = self.get_columns()
        return context

