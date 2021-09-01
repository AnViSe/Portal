from django.contrib import admin
from django.contrib.admin import ModelAdmin

from references.models import Employee


@admin.register(Employee)
class EmployeeAdmin(ModelAdmin):
    list_display = ('id', 'lastname', 'firstname', 'middlename', 'name_lfm', 'name_fml',)
    list_display_links = ('id', 'lastname',)
    search_fields = ('lastname', 'firstname', 'middlename')

    fields = ('lastname', 'firstname', 'middlename', 'name_lfm', 'name_fml', 'dt_cr', 'dt_up', 'status')
    readonly_fields = ('name_lfm', 'name_fml', 'dt_cr', 'dt_up')

    # save_on_top = True
