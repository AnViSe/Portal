from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.references.models import Country, Employee, Region, Person


@admin.register(Person)
class PersonAdmin(ModelAdmin):
    pass


@admin.register(Employee)
class EmployeeAdmin(ModelAdmin):
    list_display = ('id', 'lastname', 'firstname', 'middlename', 'name_lfm', 'name_fml',)
    list_display_links = ('id', 'lastname',)
    search_fields = ('lastname', 'firstname', 'middlename')

    fields = (
    'lastname', 'firstname', 'middlename', 'name_lfm', 'name_fml', 'dt_cr', 'dt_up', 'status')
    readonly_fields = ('name_lfm', 'name_fml', 'dt_cr', 'dt_up')

    # save_on_top = True


@admin.register(Country)
class CountryAdmin(ModelAdmin):
    pass
    # list_display = ('id', 'lastname', 'firstname', 'middlename', 'name_lfm', 'name_fml',)
    # list_display_links = ('id', 'lastname',)
    # search_fields = ('lastname', 'firstname', 'middlename')

    # fields = ('lastname', 'firstname', 'middlename', 'name_lfm', 'name_fml', 'dt_cr', 'dt_up', 'status')
    # readonly_fields = ('name_lfm', 'name_fml', 'dt_cr', 'dt_up')


@admin.register(Region)
class RegionAdmin(ModelAdmin):
    pass
