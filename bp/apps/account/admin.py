from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group

from .forms import CustomGroupAdminForm, CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ('username', 'employee', 'subdivision', 'last_login', 'is_active')
    list_select_related = [
        'employee__person',
        'subdivision'
    ]
    list_display_links = ('username',)
    # search_fields = ['username',]

    readonly_fields = ['date_joined', 'last_login']

    fieldsets = UserAdmin.fieldsets + (
        ('Профиль', {'fields': (
            'avatar',
            'employee',
            'subdivision'
        )}),
    )

    autocomplete_fields = ['employee', 'subdivision']

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        disabled_fields = set()

        if not is_superuser:
            disabled_fields |= {
                'username',
                'is_superuser',
                # 'user_permissions',
            }

        # Запретить пользователям, не являющимся суперпользователями,
        # редактировать свои собственные разрешения
        if (
                not is_superuser
                and obj is not None
                and obj == request.user
        ):
            disabled_fields |= {
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            }

        for f in disabled_fields:
            if f in form.base_fields:
                form.base_fields[f].disabled = True

        return form


admin.site.register(CustomUser, CustomUserAdmin)

admin.site.unregister(Group)


class CustomGroupAdmin(GroupAdmin):
    form = CustomGroupAdminForm
    filter_horizontal = ['permissions']


admin.site.register(Group, CustomGroupAdmin)
