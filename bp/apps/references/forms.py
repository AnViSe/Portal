from django import forms
from django.core.exceptions import ValidationError
from phonenumber_field import widgets

from apps.references.models import Employee, Person
from extensions.widgets import DateInputWidget, PhoneNumberWidget
from extensions.validators import validate_ident_num_2012


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['lastname', 'firstname', 'middlename']
        widgets = {
            'lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'firstname': forms.TextInput(attrs={'class': 'form-control'}),
            'middlename': forms.TextInput(attrs={'class': 'form-control'}),
        }


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['lastname', 'firstname', 'middlename', 'ident_num', 'birth_date', 'sex']
        widgets = {
            'birth_date': forms.TextInput(attrs={'type': 'date'}),
            # 'phone': PhoneNumberWidget(),
            # 'fax': PhoneNumberWidget(),
        }

    def clean(self):
        super().clean()
        value = str(self.cleaned_data.get('ident_num'))
        result = validate_ident_num_2012(value)
        if result is not None:
            self.add_error('ident_num', result)
