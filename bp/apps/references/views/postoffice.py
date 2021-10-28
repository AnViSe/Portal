from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views import generic
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from apps.references.models.postoffice import PostOffice
from apps.references.serializers import PostOfficeSerializer
from apps.references.utils import RefTableMixin


class PostOfficeViewSet(viewsets.ModelViewSet):
    """Список почтовых кодов"""

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = PostOffice.objects.select_related('parent', 'model_type').all()
    serializer_class = PostOfficeSerializer


class PostOfficeList(PermissionRequiredMixin, RefTableMixin, generic.ListView):
    """Справочник почтовых кодов"""

    permission_required = 'references.view_region'

    model = PostOffice

    def get_context_data(self, *, object_list=None, **kwargs):
        context = self.update_context_data(super().get_context_data(**kwargs))
        return context
