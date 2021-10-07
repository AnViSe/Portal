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
    list_display_links = ('username',)
    search_fields = ('username',)

    readonly_fields = ['date_joined', 'last_login']
    fieldsets = UserAdmin.fieldsets + (
        ('Профиль', {'fields': ('avatar', 'employee', 'subdivision',)}),
    )


admin.site.register(CustomUser, CustomUserAdmin)

admin.site.unregister(Group)


class CustomGroupAdmin(GroupAdmin):
    form = CustomGroupAdminForm
    filter_horizontal = ['permissions']


admin.site.register(Group, CustomGroupAdmin)
