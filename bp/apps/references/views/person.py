from django.urls import reverse_lazy
from django.views import generic
from rest_framework import viewsets

from apps.references.forms import PersonForm
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
        {'name': 'phone', 'title': 'Телефон'},
        {'name': 'fax', 'title': 'Факс'},
        {"name": None, "title": "Операции"},
    ]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_list'] = self.get_url(model=self.model)
        # context['field_list'] = self.get_columns(model=self.model)
        context['field_list'] = self.get_columns()
        return context


class PersonCreate(generic.CreateView):
    # permission_required = 'references.add_employee'
    form_class = PersonForm
    template_name = 'references/person/ref_add.html'
    success_url = reverse_lazy('persons')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj_name'] = Person._meta.verbose_name
        return context


class PersonEdit(generic.UpdateView):
    model = Person
    form_class = PersonForm
    template_name = 'references/person/ref_edit.html'
    success_url = reverse_lazy('persons')
