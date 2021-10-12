from django.contrib import admin
from django.contrib.admin import ModelAdmin
from mptt.admin import DraggableMPTTAdmin

from apps.references.models.employee import Employee
from apps.references.models.person import Person
from apps.references.models.subdivision import Subdivision


@admin.register(Person)
class PersonAdmin(ModelAdmin):
    list_display = ('name_lfm', 'last_name', 'first_name', 'middle_name', 'pers_num', 'status')
    list_display_links = ('name_lfm',)
    search_fields = ['name_lfm']
    list_filter = ('status',)

    fields = ['last_name', 'first_name', 'middle_name',
              'pers_num', 'birth_date', 'gender', 'status']


@admin.register(Employee)
class EmployeeAdmin(ModelAdmin):
    # Настройка списка
    list_display = ('tab_num', 'person', 'subdivision', 'dt_up', 'status')
    list_select_related = ['person', 'subdivision']
    list_display_links = ('tab_num',)
    search_fields = ('tab_num', 'person__name_lfm',)
    list_filter = ('subdivision', 'status',)
    # Настройка формы
    fields = ['tab_num', 'person', 'subdivision', 'status']
    autocomplete_fields = ['person', 'subdivision']


@admin.register(Subdivision)
class SubdivisionAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title', 'name',)
    list_display_links = ('indented_title', 'name',)
    search_fields = ['name']

    fields = ['name', 'name_full', 'parent', 'status']
    autocomplete_fields = ['parent']

# admin.site.register(Subdivision, DraggableMPTTAdmin,
#                     list_display=('tree_actions', 'indented_title', 'name',),
#                     list_display_links=('indented_title', 'name',),
#                     search_fields=['name'],
#                     fields=['name', 'name_full', 'parent', 'status'],
#                     autocomplete_fields=['parent'],
#                     )
