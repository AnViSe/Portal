from django.views import generic
from rest_framework import decorators, mixins, status, viewsets
from rest_framework.response import Response

from apps.references.models import SB
from apps.references.serializers import SubdivisionSerializer, SubdivisionTreeSerializer
from apps.references.utils import RefTableMixin


class SubdivisionViewSet(viewsets.ModelViewSet):
    # queryset = SB.objects.all()
    queryset = SB.objects.filter(level=0).all()
    # queryset = SB.objects.select_related('parent').all()
    serializer_class = SubdivisionTreeSerializer

    # @decorators.list_route(methods=['get'])
    # def tree(self, *args, **kwargs):
    #
    #     subdivisions = SB.objects.filter(level=0).all()
    #     serializer = SubdivisionTreeSerializer(subdivisions, many=True)
    #     return Response(status=status.HTTP_200_OK, data=serializer.data)


class SubdivisionList(RefTableMixin, generic.ListView):
    model = SB
    # template_name = 'references/subdivision/ref_list.html'
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
