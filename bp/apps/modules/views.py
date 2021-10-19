from django.views.generic import ListView

from apps.modules.models import Module


class ModulesMainView(ListView):
    model = Module
    template_name = 'modules/index.html'
    context_object_name = 'mods_list'
