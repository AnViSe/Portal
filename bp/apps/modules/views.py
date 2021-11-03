from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView

from apps.modules.models import Module


class ModulesMainView(PermissionRequiredMixin, ListView):
    """Просмотр списка модулей"""

    permission_required = 'modules.view_module'

    model = Module
    template_name = 'modules/index.html'
    context_object_name = 'mods_list'
