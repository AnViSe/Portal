from django import forms
from django.conf import settings
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


class BaseSelect2Widget(s2forms.ModelSelect2Widget):

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.attrs = {"style": "width: 100%"}

    def build_attrs(self, base_attrs, extra_attrs=None):
        base_attrs = super().build_attrs(base_attrs, extra_attrs)
        base_attrs.update(
            {"data-minimum-input-length": 3,
             # "data-minimum-results-for-search": "Infinity",
             "data-placeholder": self.empty_label,
             "data-theme": "bootstrap4",
             "data-ajax--delay": 250,
             })
        return base_attrs

    @property
    def media(self):
        select2_js = settings.SELECT2_JS if settings.SELECT2_JS else ()
        select2_css = settings.SELECT2_CSS if settings.SELECT2_CSS else ()

        i18n_file = ()
        if self.i18n_name in settings.SELECT2_I18N_AVAILABLE_LANGUAGES:
            i18n_file = (
                ("%s/%s.js" % (settings.SELECT2_I18N_PATH, self.i18n_name),)
            )

        return forms.Media(
            js=select2_js + i18n_file + ("django_select2/django_select2.js",),
            css={"screen": select2_css + ("django_select2/django_select2.css",)},
        )
