from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from rest_framework import viewsets

from apps.references.forms import PhoneForm
from apps.references.models.phone import Phone
from apps.references.serializers import PhoneSerializer
from apps.references.mixins import *


class PhoneViewSet(RefModelViewMixin, viewsets.ModelViewSet):
    """Список телефонов"""

    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer


class PhoneList(PermissionRequiredMixin, RefListViewMixin, generic.ListView):
    """Справочник телефонов"""

    permission_required = 'references.view_phone'

    model = Phone

    # todo Попробовать сделать через mixin
    def get_context_data(self, *, object_list=None, **kwargs):
        context = self.update_context_data(super().get_context_data(**kwargs))
        return context


class PhoneCreate(PermissionRequiredMixin, RefCreateViewMixin, generic.CreateView):
    """Создание телефона"""

    permission_required = 'references.add_phone'

    form_class = PhoneForm

    success_url = reverse_lazy('phones')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj_name'] = Phone._meta.verbose_name
        return context


class PhoneEdit(PermissionRequiredMixin, RefUpdateViewMixin, generic.UpdateView):
    """Изменение телефона"""

    permission_required = 'references.change_phone'

    model = Phone
    form_class = PhoneForm

    success_url = reverse_lazy(model.Params.route_list)


class PhoneView(RefDetailViewMixin, generic.DetailView):
    """Просмотр телефона"""

    model = Phone
