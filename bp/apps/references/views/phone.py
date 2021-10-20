from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views import generic
from rest_framework import viewsets

from apps.references.models.phone import Phone
from apps.references.serializers import PhoneSerializer
from apps.references.utils import RefTableMixin


class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer


class PhoneList(PermissionRequiredMixin, RefTableMixin, generic.ListView):
    permission_required = 'references.view_phone'
    model = Phone

    # todo Попробовать сделать через mixin
    def get_context_data(self, *, object_list=None, **kwargs):
        context = self.update_context_data(super().get_context_data(**kwargs))
        return context
