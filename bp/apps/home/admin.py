from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import Menu


@admin.register(Menu)
class MenuAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title', 'route', 'icon', 'status')
    list_display_links = ('indented_title',)
    search_fields = ['name']

    fields = ['name', 'parent', 'route', 'perm', 'icon', 'badge', 'header', 'sort', 'status']
    autocomplete_fields = ['parent']
