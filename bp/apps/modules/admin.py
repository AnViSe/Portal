from django.contrib import admin

from apps.modules.models import Module


@admin.register(Module)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'perm', 'icon', 'status')
    list_display_links = ('name',)
    search_fields = ['name']
