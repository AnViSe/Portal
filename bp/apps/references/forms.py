from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Row, Submit
from django import forms

from apps.references.models.address import Address
from apps.references.models.building import Building
from apps.references.models.employee import Employee
from apps.references.models.person import Person
from apps.references.models.subdivision import Subdivision
from extensions.widgets import BaseSelect2Widget


class BuildingWidget(BaseSelect2Widget):
    empty_label = '-- Выберите здание --'
    search_fields = ('name_bld_full__icontains',)
    queryset = Building.objects.all().order_by('name_bld_full')


class PersonWidget(BaseSelect2Widget):
    empty_label = '-- Выберите персону --'
    search_fields = ('name_lfm__icontains',)
    queryset = Person.objects.all().order_by('name_lfm')


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
