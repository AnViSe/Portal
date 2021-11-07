from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView
from rest_framework import viewsets

from apps.modules.delivery.forms import MailingForm
from apps.modules.delivery.models import Mailing
from apps.modules.delivery.serializers import MailingSerializer


class MailingViewSet(viewsets.ModelViewSet):
    """Список почтовых отправлений"""

    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer


class MailingView(PermissionRequiredMixin, ListView):

    permission_required = 'references.view_mailing'

    model = Mailing
    template_name = 'modules/delivery/index.html'

    # context_object_name = 'mails_list'

    def update_context_data(self, context):
        result = context
        result['route_list_api'] = self.model.Params.route_list_api
        result['fields_list'] = self.model.Params.fields_list
        return result

    def get_context_data(self, *, object_list=None, **kwargs):
        context = self.update_context_data(super().get_context_data(**kwargs))
        return context


class MailingCreate(PermissionRequiredMixin, generic.CreateView):
    """Создание почтового отправления"""

    permission_required = 'references.add_mailing'

    template_name = 'modules/delivery/add.html'

    form_class = MailingForm

    success_url = reverse_lazy('mailings')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj_name'] = Mailing._meta.verbose_name
        return context

    def form_valid(self, form):
        form.instance.subdivision = self.request.user.subdivision
        return super().form_valid(form)
