from django.views import generic
from rest_framework import decorators, mixins, status, viewsets
from rest_framework.response import Response

from apps.references.models.subdivision import Subdivision
from apps.references.serializers import SubdivisionTreeSerializer, SubdivisionSerializer
from apps.references.utils import RefTableMixin


class SubdivisionTreeViewSet(viewsets.ModelViewSet):
    # queryset = Subdivision.objects.all()
    queryset = Subdivision.objects.filter(level=0).all()
    # queryset = Subdivision.objects.filter(level=0).all().prefetch_related('children')
    # queryset = Subdivision.objects.select_related('parent').filter(level=0).all()
    serializer_class = SubdivisionTreeSerializer

    # @decorators.list_route(methods=['get'])
    # def tree(self, *args, **kwargs):
    #
    #     subdivisions = SB.objects.filter(level=0).all()
    #     serializer = SubdivisionTreeSerializer(subdivisions, many=True)
    #     return Response(status=status.HTTP_200_OK, data=serializer.data)


class SubdivisionViewSet(viewsets.ModelViewSet):
    # queryset = Subdivision.objects.all()
    queryset = Subdivision.objects.select_related('parent').all()
    serializer_class = SubdivisionSerializer

    # @decorators.list_route(methods=['get'])
    # def tree(self, *args, **kwargs):
    #
    #     subdivisions = SB.objects.filter(level=0).all()
    #     serializer = SubdivisionTreeSerializer(subdivisions, many=True)
    #     return Response(status=status.HTTP_200_OK, data=serializer.data)


class SubdivisionList(RefTableMixin, generic.ListView):
    model = Subdivision

    # PermissionRequiredMixin, <== Добавить в класс первым
    # permission_required = 'references.view_subdivision'

    # todo Попробовать сделать через mixin
    def get_context_data(self, *, object_list=None, **kwargs):
        context = self.update_context_data(super().get_context_data(**kwargs))
        return context
