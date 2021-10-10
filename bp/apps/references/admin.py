from django.contrib import admin
from django.contrib.admin import ModelAdmin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

from apps.references.forms import EmployeeForm, PersonForm

from apps.references.models.employee import Employee
from apps.references.models.person import Person
from apps.references.models.subdivision import Subdivision


class PersonAdmin(ModelAdmin):
    list_display = ('name_lfm', 'last_name', 'first_name', 'middle_name',
                    'pers_num', 'status')
    # list_filter = ('status',)

    form = PersonForm


class SubdivisionAdmin(ModelAdmin):
    list_filter = ('status',)


# @admin.register(Employee)
class EmployeeAdmin(ModelAdmin):
    list_display = ('tab_num',
                    'person',
                    'subdivision',
                    'dt_up', 'status')
    list_select_related = ['person', 'subdivision']
    list_display_links = ('tab_num',)
    search_fields = ('tab_num', 'person__name_lfm',)
    # list_filter = ('status',)

    form = EmployeeForm
    # model = Employee

    # fields = ['pers_num', 'dt_cr', 'dt_up', 'status']
    # readonly_fields = ('dt_cr', 'dt_up')

    # save_on_top = True


# @admin.register(Country)
# class CountryAdmin(ModelAdmin):
#     pass
# list_display = ('id', 'lastname', 'firstname', 'middlename', 'name_lfm', 'name_fml',)
# list_display_links = ('id', 'lastname',)
# search_fields = ('lastname', 'firstname', 'middlename')

# fields = ('lastname', 'firstname', 'middlename', 'name_lfm', 'name_fml', 'dt_cr', 'dt_up', 'status')
# readonly_fields = ('name_lfm', 'name_fml', 'dt_cr', 'dt_up')


# @admin.register(Region)
# class RegionAdmin(ModelAdmin):
#     pass

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Person, PersonAdmin)

admin.site.register(
    Subdivision,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
        'name',
    ),
    list_display_links=(
        'indented_title',
        'name',
    ),
)
