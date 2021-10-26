from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from apps.references.forms import PersonForm
from apps.references.models.person import Person
from apps.references.serializers import PersonSerializer
from apps.references.utils import RefTableMixin


class PersonViewSet(viewsets.ModelViewSet):
    """Список персон"""

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonList(PermissionRequiredMixin, RefTableMixin, generic.ListView):
    """Справочник персон"""

    permission_required = 'references.view_person'
    model = Person

    # todo Попробовать сделать через mixin
    def get_context_data(self, *, object_list=None, **kwargs):
        context = self.update_context_data(super().get_context_data(**kwargs))
        return context


class PersonCreate(PermissionRequiredMixin, generic.CreateView):
    """Создание персоны"""

    permission_required = 'references.add_person'

    form_class = PersonForm
    template_name = 'references/ref_add.html'
    success_url = reverse_lazy('persons')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj_name'] = Person._meta.verbose_name
        return context


class PersonEdit(PermissionRequiredMixin, generic.UpdateView):
    """Изменение персоны"""

    permission_required = 'references.change_person'

    model = Person
    form_class = PersonForm
    template_name = 'references/ref_edit.html'
    success_url = reverse_lazy(model.Params.route_list)
