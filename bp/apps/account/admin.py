from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group
from django.db.models import Q

from .forms import CustomGroupAdminForm, CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


@admin.register(CustomUser)
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
    search_fields = ['username',]

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
                'is_superuser',
            }
            if obj is not None:
                disabled_fields |= {
                    'username',
                }
                if obj.is_superuser:
                    disabled_fields |= {
                        'is_active',
                        'is_staff',
                        'groups',
                        'user_permissions',
                        'employee',
                        'subdivision',
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

    def get_queryset(self, request):
        qs = super(CustomUserAdmin, self).get_queryset(request)
        # Обычные пользователи не могут видеть суперпользователей
        if not request.user.is_superuser:
            qs = qs.filter(is_superuser=0)
            if request.user.subdivision:
                qs = qs.filter(Q(subdivision=request.user.subdivision) | Q(subdivision=None))
        return qs


admin.site.unregister(Group)


class CustomGroupAdmin(GroupAdmin):
    form = CustomGroupAdminForm
    filter_horizontal = ['permissions']


admin.site.register(Group, CustomGroupAdmin)
