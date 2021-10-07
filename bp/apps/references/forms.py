from django import forms
from django.core.exceptions import ValidationError
from phonenumber_field import widgets

from apps.references.models.employee import Employee
from apps.references.models.person import Person
from extensions.widgets import DateInputWidget, PhoneNumberWidget
from extensions.validators import validate_ident_num_2012


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        # exclude = ['id']
        fields = ['tab_num', 'person', 'subdivision', 'status']
        # fields = '__all__'
        # readonly_fields = ('dt_cr', 'dt_up',)
        # widgets = {
        #     'lastname': forms.TextInput(attrs={'class': 'form-control'}),
        #     'firstname': forms.TextInput(attrs={'class': 'form-control'}),
        #     'middlename': forms.TextInput(attrs={'class': 'form-control'}),
        # }


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
