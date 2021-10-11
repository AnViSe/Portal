from django import forms
from django_select2 import forms as s2forms
from django.forms import widgets
from django.template import loader
from django.utils.safestring import mark_safe


class DateInputWidget(forms.DateInput):
    input_type = 'date'
    # template_name = ''


class PhoneNumberWidget(widgets.Input):
    template_name = 'widgets/phone.html'
    input_type = 'tel'

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        # print(context['widget']['value'])
    #     context['widget']['name'] = name
    #     context['widget']['value'] = value
        return context

    def render(self, name, value, attrs=None, renderer=None):
        context = self.get_context(name, value, attrs)
        template = loader.get_template(self.template_name).render(context)
        return mark_safe(template)


class BaseAutocompleteSelect(s2forms.ModelSelect2Widget):
    # class Media:
    #     js = ("/static/js/jquery/jquery-3.6.0.min.js",)

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.attrs = {"style": "width: 100%"}

    def build_attrs(self, base_attrs, extra_attrs=None):
        base_attrs = super().build_attrs(base_attrs, extra_attrs)
        base_attrs.update(
            {"data-minimum-input-length": 3, "data-placeholder": self.empty_label}
        )
        return base_attrs
