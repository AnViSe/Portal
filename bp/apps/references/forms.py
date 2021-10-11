from django import forms
from django_select2 import forms as s2forms
from django.core.exceptions import ValidationError
from phonenumber_field import widgets

from apps.references.models.employee import Employee
from apps.references.models.person import Person
from extensions.widgets import BaseAutocompleteSelect, DateInputWidget, PhoneNumberWidget
from extensions.validators import validate_ident_num_2012


class PersonWidget(s2forms.ModelSelect2Widget):
    empty_label = '-- Выберите персону --'
    search_fields = ('name_lfm__icontains',)
    queryset = Person.objects.all().order_by('name_lfm')

    # def __init__(self, **kwargs):
    #     super().__init__(kwargs)
    #     self.attrs = {"style": "width: 100%"}

    def build_attrs(self, base_attrs, extra_attrs=None):
        base_attrs = super().build_attrs(base_attrs, extra_attrs)
        base_attrs.update(
            {"data-minimum-input-length": 3,
             "data-placeholder": self.empty_label,
             "data-theme": "bootstrap4",
             }
        )
        return base_attrs


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        # exclude = ['id']
        fields = ['tab_num', 'person', 'subdivision', 'status']
        # fields = '__all__'
        # readonly_fields = ('dt_cr', 'dt_up',)
        widgets = {
            'person': PersonWidget,
        }


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['last_name', 'first_name', 'middle_name',
                  'pers_num', 'birth_date', 'gender', 'status']
        widgets = {
            'birth_date': forms.TextInput(attrs={'type': 'date'}),
        }

    # def clean(self):
    #     super().clean()
    #     value = str(self.cleaned_data.get('ident_num'))
    #     result = validate_ident_num_2012(value)
    #     if result is not None:
    #         self.add_error('ident_num', result)
