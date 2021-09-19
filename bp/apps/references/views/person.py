from django.views import generic
from rest_framework import viewsets

from apps.references.models.person import Person
from apps.references.serializers import PersonSerializer
from apps.references.utils import RefTableMixin


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonList(RefTableMixin, generic.ListView):
    model = Person
    # template_name = 'references/ref_list.html'
    # PermissionRequiredMixin, <== Добавить в класс первым
    # permission_required = 'references.view_region'
    url_list = 'person-list'
    field_list = [
        {'name': 'id', 'title': 'Код'},
        {'name': 'lastname', 'title': 'Фамилия'},
        {'name': 'firstname', 'title': 'Имя'},
        {'name': 'middlename', 'title': 'Отчество'},
        {'name': 'name_lfm', 'title': 'Фамилия И.О.'},
        {"name": None, "title": "Операции"},
    ]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_list'] = self.get_url(model=self.model)
        # context['field_list'] = self.get_columns(model=self.model)
        context['field_list'] = self.get_columns()
        return context
