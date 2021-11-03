from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from rest_framework import decorators, mixins, status, viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.references.forms import SubdivisionForm
from apps.references.models.employee import Employee
from apps.references.models.subdivision import Subdivision
from apps.references.serializers import SubdivisionTreeSerializer, SubdivisionSerializer
from apps.references.mixins import *


# class SubdivisionTreeViewSet(viewsets.ModelViewSet):
    # queryset = Subdivision.objects.all()
    # queryset = Subdivision.objects.filter(level=0).all()
    # queryset = Subdivision.objects.filter(level=0).all().prefetch_related('children')
    # queryset = Subdivision.objects.select_related('parent').filter(level=0).all()
    # serializer_class = SubdivisionTreeSerializer

    # @decorators.list_route(methods=['get'])
    # def tree(self, *args, **kwargs):
    #
    #     subdivisions = SB.objects.filter(level=0).all()
    #     serializer = SubdivisionTreeSerializer(subdivisions, many=True)
    #     return Response(status=status.HTTP_200_OK, data=serializer.data)


class SubdivisionViewSet(viewsets.ModelViewSet):
    """Список подразделений"""

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Subdivision.objects.select_related('parent').all()
    serializer_class = SubdivisionSerializer

    # @decorators.list_route(methods=['get'])
    # def tree(self, *args, **kwargs):
    #
    #     subdivisions = SB.objects.filter(level=0).all()
    #     serializer = SubdivisionTreeSerializer(subdivisions, many=True)
    #     return Response(status=status.HTTP_200_OK, data=serializer.data)


class SubdivisionList(PermissionRequiredMixin, RefTableMixin, generic.ListView):
    """Справочник подразделений"""

    permission_required = 'references.view_subdivision'

    model = Subdivision

    # todo Попробовать сделать через mixin
    def get_context_data(self, *, object_list=None, **kwargs):
        context = self.update_context_data(super().get_context_data(**kwargs))
        return context


class SubdivisionCreate(PermissionRequiredMixin, generic.CreateView):
    """Создание подразделения"""

    permission_required = 'references.add_subdivision'

    form_class = SubdivisionForm
    template_name = 'references/ref_add.html'
    success_url = reverse_lazy('subdivisions')

    extra_context = {'my_var': 'My Value'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj_name'] = Subdivision._meta.verbose_name
        return context

    def my_var(self):
        return get_object_or_404(Employee, id=self.kwargs.get('chief_id'))


class SubdivisionEdit(PermissionRequiredMixin, generic.UpdateView):
    """Изменение подразделения"""

    permission_required = 'references.change_subdivision'

    model = Subdivision
    form_class = SubdivisionForm
    template_name = 'references/ref_edit.html'
    success_url = reverse_lazy(model.Params.route_list)
