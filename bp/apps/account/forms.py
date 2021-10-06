from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import Group

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        exclude = []


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        exclude = []


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
