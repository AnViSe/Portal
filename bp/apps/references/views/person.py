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

    # PermissionRequiredMixin, <== Добавить в класс первым
    # permission_required = 'references.view_person'

    # todo Попробовать сделать через mixin
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['route_list_api'] = self.model.Params.route_list_api
        context['fields_list'] = self.model.Params.fields_list
        if self.action_field not in context['fields_list']:
            context['fields_list'].append(self.action_field)
        return context


class PersonCreate(generic.CreateView):
    # permission_required = 'references.add_employee'
    form_class = PersonForm
    template_name = 'references/person/ref_add.html'
    success_url = reverse_lazy(Person.Params.route_list)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj_name'] = Person.Meta.verbose_name
        return context


class PersonEdit(generic.UpdateView):
    model = Person
    form_class = PersonForm
    template_name = 'references/person/ref_edit.html'
    success_url = reverse_lazy(model.Params.route_list)