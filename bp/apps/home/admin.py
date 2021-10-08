from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Menu


class MenuAdmin(ModelAdmin):
    list_display = ('name', 'route', 'icon', 'status')


admin.site.register(Menu, MenuAdmin)
