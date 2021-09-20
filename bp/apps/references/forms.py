from django import forms
from django.core.exceptions import ValidationError
from phonenumber_field import widgets

from apps.references.models import Employee, Person
from extensions.widgets import DateInputWidget, PhoneNumberWidget


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
        fields = ['lastname', 'firstname', 'middlename', 'ident_num', 'birth_date', 'sex',
                  # 'phone',
                  'fax'
                  ]
        widgets = {
            'birth_date': DateInputWidget(),
            # 'phone': PhoneNumberWidget(),
            'fax': PhoneNumberWidget(),
        }

    # def clean(self):
    #     super().clean()
    #     data = str(self.cleaned_data.get('fax'))
    #     if not data.startswith('375'):
    #         raise ValidationError('Номер должен начинаться на 375')
