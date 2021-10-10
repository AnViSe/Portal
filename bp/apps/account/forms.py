from django import forms
from django.urls import reverse_lazy
from django_select2 import forms as s2forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import Group

from extensions.widgets import BaseAutocompleteSelect
from apps.account.models import CustomUser
from apps.references.models.employee import Employee
from apps.references.models.subdivision import Subdivision


class EmployeeWidget(BaseAutocompleteSelect):
    empty_label = '-- Выберите сотрудника --'
    # model = Employee
    search_fields = [
        'tab_num__icontains',
        'person__name_lfm__icontains',
    ]

    def label_from_instance(self, obj):
        return str(obj.person)


class SubdivisionWidget(s2forms.HeavySelect2Widget):
    empty_label = '-- Выберите подразделение --'
    # model = Subdivision
    # queryset = Subdivision.objects.filter().order_by('name')
    search_fields = [
        'name__icontains',
    ]

    def label_from_instance(self, obj):
        return str(obj.name)


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        exclude = []


class CustomUserChangeForm(UserChangeForm):
# https://django-select2.readthedocs.io/en/latest/django_select2.html#module-django_select2.views

    class Meta:
        model = CustomUser
        exclude = []
        widgets = {
            'employee': EmployeeWidget,
            'subdivision': s2forms.HeavySelect2Widget(data_view='subdivision-list',
            # 'subdivision': s2forms.HeavySelect2Widget(data_url='/api/v1/refs/subdivision/?format=json',
                                                      search_fields=['name__icontains', ]
                                                      ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['employee'].queryset = Employee.objects.none()
        # self.fields['subdivision'].queryset = Subdivision.objects.none()


class CustomGroupAdminForm(forms.ModelForm):
    # Добавляем список пользователей
    users = forms.ModelMultipleChoiceField(
        queryset=CustomUser.objects.all(),
        required=False,
        label='Пользователи',
        # Use the pretty 'filter_horizontal widget'.
        widget=FilteredSelectMultiple('пользователи', False)
    )

    class Meta:
        model = Group
        exclude = []

    def __init__(self, *args, **kwargs):
        # Do the normal form initialisation.
        super(CustomGroupAdminForm, self).__init__(*args, **kwargs)
        # If it is an existing group (saved objects have a pk).
        if self.instance.pk:
            # Populate the users field with the current Group users.
            self.fields['users'].initial = self.instance.user_set.all()

    def save_m2m(self):
        # Add the users to the Group.
        self.instance.user_set.set(self.cleaned_data['users'])

    def save(self, *args, **kwargs):
        # Default save
        instance = super(CustomGroupAdminForm, self).save()
        # Save many-to-many data
        self.save_m2m()
        return instance
