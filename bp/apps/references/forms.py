from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Row, Submit
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms import CheckboxSelectMultiple, SelectMultiple
from django_select2.forms import Select2MultipleWidget

from apps.references.models.address import Address
from apps.references.models.building import Building
from apps.references.models.district import District
from apps.references.models.employee import Employee
from apps.references.models.location import Location, LocationStreets
from apps.references.models.person import Person
from apps.references.models.street import Street
from apps.references.models.subdivision import Subdivision
from extensions.widgets import BaseSelect2MultipleWidget, BaseSelect2Widget


class BuildingWidget(BaseSelect2Widget):
    empty_label = '-- Выберите здание --'
    search_fields = ('name_bld_full__icontains',)
    queryset = Building.objects.all().order_by('name_bld_full')


class DistrictWidget(BaseSelect2Widget):
    empty_label = '-- Выберите район --'
    search_fields = ('name_dst__icontains',)
    queryset = District.objects.all().order_by('name_dst')


class LocationWidget(BaseSelect2Widget):
    empty_label = '-- Выберите населенный пункт --'
    search_fields = ('name_lct_full__icontains',)
    queryset = Location.objects.all().order_by('name_lct_full')


class PersonWidget(BaseSelect2Widget):
    empty_label = '-- Выберите персону --'
    search_fields = ('name_lfm__icontains',)
    queryset = Person.objects.all().order_by('name_lfm')


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


class SubdivisionWidget(BaseSelect2Widget):
    empty_label = '-- Выберите подразделение --'
    search_fields = ('name_sd__icontains',)
    queryset = Subdivision.objects.all().order_by('name_sd')


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['code', 'building', 'name_adds', 'status']
        widgets = {
            'code': forms.TextInput(attrs={'autofocus': True}),
            'building': BuildingWidget,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('code', css_class='form-group col-md-2 mb-0'),
                Column('building', css_class='form-group col-md-8 mb-0'),
                Column('name_adds', css_class='form-group col-md-2 mb-0'),
            ),
            'status',
            Submit('submit', 'Сохранить')
        )


class BuildingForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = ['code', 'location', 'street', 'name_bld', 'latitude', 'longitude', 'status']
        widgets = {
            'code': forms.TextInput(attrs={'autofocus': True}),
            'location': LocationWidget,
            'street': StreetWidget,  # (dependent_fields={'location': 'location'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'code',
            Row(
                Column('location', css_class='form-group col-md-5 mb-0'),
                Column('street', css_class='form-group col-md-5 mb-0'),
                Column('name_bld', css_class='form-group col-md-2 mb-0'),
            ),
            Row(
                Column('latitude', css_class='form-group col-md-6 mb-0'),
                Column('longitude', css_class='form-group col-md-6 mb-0'),
            ),
            'status',
            Submit('submit', 'Сохранить')
        )


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['tab_num', 'person', 'subdivision', 'status']
        widgets = {
            'tab_num': forms.NumberInput(attrs={'autofocus': True}),
            'person': PersonWidget,
            'subdivision': SubdivisionWidget,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('tab_num', css_class='form-group col-md-4 mb-0'),
                Column('person', css_class='form-group col-md-8 mb-0'),
            ),
            'subdivision',
            'status',
            Submit('submit', 'Сохранить')
        )


class LocationForm(forms.ModelForm):
    # streets = forms.ModelMultipleChoiceField(
    #     queryset=LocationStreets.objects.filter(location__id=6),
    #     required=False,
    # limit_choices_to={'location': Location},
    #     label='Улицы',
    # Use the pretty 'filter_horizontal widget'.
    # widget=FilteredSelectMultiple('пользователи', False)
    # widget=CheckboxSelectMultiple(),
    # )

    class Meta:
        model = Location
        fields = ['code', 'soato', 'name_lct', 'district', 'model_type', 'streets', 'status']
        widgets = {
            'code': forms.TextInput(attrs={'autofocus': True}),
            'district': DistrictWidget,
            'streets': StreetMultipleWidget,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('code', css_class='form-group col-md-2 mb-0'),
                Column('soato', css_class='form-group col-md-3 mb-0'),
                Column('district', css_class='form-group col-md-7 mb-0'),
            ),
            Row(
                Column('model_type', css_class='form-group col-md-2 mb-0'),
                Column('name_lct', css_class='form-group col-md-10 mb-0'),
            ),
            'streets',
            'status',
            Submit('submit', 'Сохранить')
        )


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['last_name', 'first_name', 'middle_name',
                  'pers_num', 'birth_date', 'gender', 'status']
        widgets = {
            'birth_date': forms.TextInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('last_name', css_class='form-group col-md-4 mb-0'),
                Column('first_name', css_class='form-group col-md-4 mb-0'),
                Column('middle_name', css_class='form-group col-md-4 mb-0'),
            ),
            Row(
                Column('pers_num', css_class='form-group col-md-4 mb-0'),
                Column('birth_date', css_class='form-group col-md-4 mb-0'),
                Column('gender', css_class='form-group col-md-4 mb-0'),
            ),
            'status',
            Submit('submit', 'Сохранить')
        )

    # def clean(self):
    #     super().clean()
    #     value = str(self.cleaned_data.get('ident_num'))
    #     result = validate_ident_num_2012(value)
    #     if result is not None:
    #         self.add_error('ident_num', result)


class SubdivisionForm(forms.ModelForm):
    class Meta:
        model = Subdivision
        fields = ['code', 'name_sd', 'parent', 'status']
        widgets = {
            'code': forms.TextInput(attrs={'autofocus': True}),
            'parent': SubdivisionWidget,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('code', css_class='form-group col-md-2 mb-0'),
                Column('name_sd', css_class='form-group col-md-10 mb-0'),
            ),
            'parent',
            'status',
            Submit('submit', 'Сохранить')
        )


class LocationAdminForm(forms.ModelForm):
    streets = forms.ModelMultipleChoiceField(
        queryset=Street.objects.all(),
        required=False,
        label='Улицы',
        # Use the pretty 'filter_horizontal widget'.
        widget=FilteredSelectMultiple('улицы', False)
    )

    class Meta:
        model = Location
        exclude = []

    def __init__(self, *args, **kwargs):
        # Do the normal form initialisation.
        super(LocationAdminForm, self).__init__(*args, **kwargs)
        # If it is an existing group (saved objects have a pk).
        if self.instance.pk:
            # Populate the users field with the current Group users.
            self.fields['streets'].initial = self.instance.streets.all()
