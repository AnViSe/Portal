from django.views.generic import ListView

from apps.modules.delivery.models import Mailing


class DeliveryMainView(ListView):
    model = Mailing
    template_name = 'modules/delivery/index.html'
    context_object_name = 'mails_list'
