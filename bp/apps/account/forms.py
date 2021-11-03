from django import forms
from django.urls import reverse_lazy
from django_select2 import forms as s2forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import Group

from apps.references.models.subdivision import Subdivision
from extensions.widgets import BaseSelect2Widget, SubdivisionWidget
from apps.account.models import CustomUser
# from apps.references.models.employee import Employee
# from apps.references.models.subdivision import Subdivision


# class EmployeeWidget(BaseSelect2Widget):
#     empty_label = '-- Выберите сотрудника --'
#     search_fields = [
#         'tab_num__icontains',
#         'person__name_lfm__icontains',
#     ]
#     queryset = Employee.objects.select_related('person').all().order_by('person__name_lfm')


# class SubdivisionWidget(BaseSelect2Widget):
#     empty_label = '-- Выберите подразделение --'
#     search_fields = ['name__icontains',]
#     queryset = Subdivision.objects.all().order_by('name')


class CustomUserCreationForm(UserCreationForm):

    # subdivision = forms.ModelChoiceField(
    #     widget=SubdivisionWidget(
    #         queryset=Subdivision.objects.all().order_by('name_sd'))
    # )

    class Meta:
        model = CustomUser
        # fields = ('subdivision',)
        exclude = []


class CustomUserChangeForm(UserChangeForm):
    # https://django-select2.readthedocs.io/en/latest/django_select2.html#module-django_select2.views

    class Meta:
        model = CustomUser
        exclude = []
        # widgets = {
        #     'employee': EmployeeWidget,
        #     'subdivision': SubdivisionWidget,
        # }

    # class Media:
    #     js = ('','')

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
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
