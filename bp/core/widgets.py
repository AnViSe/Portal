from django import forms
from django.conf import settings
from django_select2 import forms as s2forms
from django.forms import widgets
from django.template import loader
from django.utils.safestring import mark_safe

from apps.references.models.address import Address
from apps.references.models.building import Building
from apps.references.models.country import Country
from apps.references.models.district import District
from apps.references.models.employee import Employee
from apps.references.models.location import Location
from apps.references.models.person import Person
from apps.references.models.phone import Phone
from apps.references.models.postoffice import PostOffice
from apps.references.models.region import Region
from apps.references.models.street import Street
from apps.references.models.subdivision import Subdivision


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
            {
                "data-minimum-input-length": 0,
                "data-minimum-results-for-search": 25,
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
            # js=select2_js + i18n_file + ("django_select2/django_select2.js",),
            # css={"screen": select2_css + ("django_select2/django_select2.css",)},
        )


class BaseSelect2AppendWidget(s2forms.ModelSelect2Widget):

    template_name = 'widgets/select2-append.html'

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.attrs = {"style": "width: 70%"}

    def build_attrs(self, base_attrs, extra_attrs=None):
        base_attrs = super().build_attrs(base_attrs, extra_attrs)
        base_attrs.update(
            {
                "append": {'link': '#', 'label': 'Label', 'img': 'far fa-square-plus'},
                "data-minimum-input-length": 0,
                "data-minimum-results-for-search": 25,
                "data-placeholder": self.empty_label,
                "data-theme": "bootstrap4",
                "data-ajax--delay": 250,
             })
        return base_attrs

    @property
    def media(self):
        return forms.Media(
        )


class BaseSelect2MultipleWidget(s2forms.HeavySelect2MultipleWidget):

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.attrs = {"style": "width: 100%"}

    def build_attrs(self, base_attrs, extra_attrs=None):
        base_attrs = super().build_attrs(base_attrs, extra_attrs)
        base_attrs.update(
            {
                # "data-minimum-input-length": 0,
                # "data-minimum-results-for-search": 25,
                # "data-placeholder": self.empty_label,
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
            # js=select2_js + i18n_file + ("django_select2/django_select2.js",),
            # css={"screen": select2_css + ("django_select2/django_select2.css",)},
        )


class AddressWidget(BaseSelect2Widget):
    empty_label = '-- Выберите адрес --'
    search_fields = ('name_adds_full__icontains',)
    queryset = Address.objects.all().order_by('name_adds_full')


class BuildingWidget(BaseSelect2Widget):
    empty_label = '-- Выберите здание --'
    search_fields = ('name_bld_full__icontains',)
    queryset = Building.objects.all().order_by('name_bld_full')


class BuildingAppendWidget(BaseSelect2AppendWidget):
    empty_label = '-- Выберите здание --'
    search_fields = ('name_bld_full__icontains',)
    queryset = Building.objects.all().order_by('name_bld_full')


class CountryWidget(BaseSelect2Widget):
    empty_label = '-- Выберите страну --'
    search_fields = ('name_cnt__icontains',)
    queryset = Country.objects.all().order_by('name_cnt')


class DistrictWidget(BaseSelect2Widget):
    empty_label = '-- Выберите район --'
    search_fields = ('name_dst__icontains',)
    queryset = District.objects.all().order_by('name_dst')


class EmployeeWidget(BaseSelect2Widget):
    empty_label = '-- Выберите сотрудника --'
    search_fields = ('tab_num__icontains', 'person__name_lfm__icontains')
    queryset = Employee.objects.select_related('person').all().order_by('person__name_lfm')


class LocationWidget(BaseSelect2Widget):
    empty_label = '-- Выберите населенный пункт --'
    search_fields = ('name_lct_full__icontains',)
    queryset = Location.objects.all().order_by('name_lct_full')


class PersonWidget(BaseSelect2Widget):
    empty_label = '-- Выберите персону --'
    search_fields = ('name_lfm__icontains',)
    queryset = Person.objects.all().order_by('name_lfm')


class PhoneWidget(BaseSelect2Widget):
    empty_label = '-- Выберите номер телефона --'
    search_fields = ('phone_number__icontains',)
    # queryset = Phone.objects.all().order_by('phone_number')
    queryset = Phone.mobiles.all().order_by('phone_number')


class PostOfficeWidget(BaseSelect2Widget):
    empty_label = '-- Выберите почтовый код --'
    search_fields = ('name_post__icontains',)
    queryset = PostOffice.objects.all().order_by('name_post')


class RegionWidget(BaseSelect2Widget):
    empty_label = '-- Выберите область --'
    search_fields = ('name_rgn__icontains',)
    queryset = Region.objects.all().order_by('name_rgn')


class StreetWidget(BaseSelect2Widget):
    empty_label = '-- Выберите улицу --'
    search_fields = ('name_str_full__icontains',)
    # queryset = LocationStreets.objects.select_related('street').all().order_by('street__name_str_full')
    queryset = Street.objects.all().order_by('name_str_full')


class StreetMultipleWidget(BaseSelect2MultipleWidget):
    # empty_label = '-- Выберите улицу --'
    search_fields = ('name_str_full__icontains',)
    # queryset = LocationStreets.objects.select_related('street').all().order_by('street__name_str_full')
    queryset = Street.objects.all().order_by('name_str_full')


class StreetModelMultipleWidget(s2forms.ModelSelect2MultipleWidget):
    # empty_label = '-- Выберите улицу --'
    search_fields = ('name_str_full__icontains',)
    # queryset = LocationStreets.objects.select_related('street').all().order_by('street__name_str_full')
    # queryset = Street.objects.all().order_by('name_str_full')

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.attrs = {"style": "width: 100%"}

    def build_attrs(self, base_attrs, extra_attrs=None):
        base_attrs = super().build_attrs(base_attrs, extra_attrs)
        base_attrs.update(
            {
                # "data-minimum-input-length": 0,
                # "data-minimum-results-for-search": 25,
                # "data-placeholder": self.empty_label,
                "data-theme": "bootstrap4",
                "data-ajax--delay": 250,
             })
        return base_attrs

    @property
    def media(self):
        return forms.Media(
        )


class SubdivisionWidget(BaseSelect2Widget):
    empty_label = '-- Выберите подразделение --'
    search_fields = ('name_sd__icontains',)
    queryset = Subdivision.objects.all().order_by('level', 'name_sd')
