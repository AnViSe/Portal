from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ('username', 'employee', 'subdivision', 'is_active')
    list_display_links = ('username',)
    search_fields = ('username',)

    readonly_fields = ['date_joined', 'last_login']
    fieldsets = UserAdmin.fieldsets + (
        ('Профиль', {'fields': ('avatar', 'employee', 'subdivision',)}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
