from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from apps.references.forms import PostOfficeForm
from apps.references.models.postoffice import PostOffice
from apps.references.serializers import PostOfficeSerializer
from apps.references.mixins import *


class PostOfficeViewSet(RefModelViewMixin, viewsets.ModelViewSet):
    """Список почтовых кодов"""

    queryset = PostOffice.objects.select_related('parent', 'address', 'model_type').all()
    serializer_class = PostOfficeSerializer


class PostOfficeList(PermissionRequiredMixin, RefListViewMixin, generic.ListView):
    """Справочник почтовых кодов"""

    permission_required = 'references.view_postoffice'

    model = PostOffice

    def get_context_data(self, *, object_list=None, **kwargs):
        context = self.update_context_data(super().get_context_data(**kwargs))
        return context


class PostOfficeCreate(PermissionRequiredMixin, RefCreateViewMixin, generic.CreateView):
    """Создание почтового кода"""

    permission_required = 'references.add_postoffice'

    form_class = PostOfficeForm

    success_url = reverse_lazy('postoffices')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj_name'] = PostOffice._meta.verbose_name
        return context


class PostOfficeEdit(PermissionRequiredMixin, RefUpdateViewMixin, generic.UpdateView):
    """Изменение почтового кода"""

    permission_required = 'references.change_postoffice'

    model = PostOffice
    form_class = PostOfficeForm

    success_url = reverse_lazy(model.Params.route_list)


class PostOfficeView(RefDetailViewMixin, generic.DetailView):
    """Просмотр почтового кода"""

    model = PostOffice

    queryset = PostOffice.objects.select_related('parent', 'address', 'model_type')
