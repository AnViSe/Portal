from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import Menu


@admin.register(Menu)
class MenuAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title', 'route', 'icon', 'perm', 'status')
    list_display_links = ('indented_title',)
    search_fields = ['title']

    fields = ['title', 'parent', 'route', 'perm', 'icon', 'badge', 'header', 'status']
    autocomplete_fields = ['parent']
