from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Row, Submit
from django import forms

from apps.references.models.employee import Employee
from apps.references.models.person import Person
from apps.references.models.subdivision import Subdivision
from extensions.widgets import BaseSelect2Widget


class PersonWidget(BaseSelect2Widget):
    empty_label = '-- Выберите персону --'
    search_fields = ('name_lfm__icontains',)
    queryset = Person.objects.all().order_by('name_lfm')


class SubdivisionWidget(BaseSelect2Widget):
    empty_label = '-- Выберите подразделение --'
    search_fields = ('name_sd__icontains',)
    queryset = Subdivision.objects.all().order_by('name_sd')


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ['tab_num', 'person', 'subdivision', 'status']
        widgets = {
            'tab_num': forms.NumberInput,
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
        fields = ['name_sd', 'parent', 'status']
        widgets = {
            'parent': SubdivisionWidget,
        }
