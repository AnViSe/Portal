from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.safestring import mark_safe
from mptt.admin import DraggableMPTTAdmin

from apps.references.models.base import FlexType
from apps.references.models.country import Country
from apps.references.models.employee import Employee
from apps.references.models.person import Person
from apps.references.models.phone import Phone
from apps.references.models.subdivision import Subdivision


@admin.register(Country)
class CountryAdmin(ModelAdmin):
    list_display = ('code', 'name_cnt', 'alpha2', 'alpha3', 'status')


@admin.register(FlexType)
class FlexTypeAdmin(ModelAdmin):
    list_display = ('type_code', 'type_name', 'type_name_full', 'type_desc', 'status')
    search_fields = ['type_name']


# https://brainstorm.it/snippets/many-many-example-using-through-augment-m2m-relationships/
# class PersonForPhoneTabularInline(admin.TabularInline):
#     model = Phone.persons.through
#     extra = 0
#     autocomplete_fields = ['person', ]


@admin.register(Phone)
class PhoneAdmin(ModelAdmin):
    list_display = ('phone_number',
                    'model_type',
                    # 'list_persons',
                    'status')
    # list_prefetch_related = ['persons']
    list_display_links = ('phone_number',)
    search_fields = ['phone_number']
    # inlines = [PersonForPhoneTabularInline, ]

    fields = ['phone_number', 'model_type', 'status']

    # autocomplete_fields = ['person']

    def list_persons(self, obj):
        return mark_safe(', '.join([
            # f'<a href="{person.get_admin_url()}">{str(person)}</a>'
            f'<a href="#">{str(person)}</a>'
            # str(person)
            for person in obj.persons.all()
        ]))

    list_persons.short_description = 'персоны'


# class PhoneTabularInline(admin.TabularInline):
#     model = Phone.persons.through
#     extra = 0
#     autocomplete_fields = ['phone', ]


@admin.register(Person)
class PersonAdmin(ModelAdmin):
    list_display = ('name_lfm', 'last_name', 'first_name', 'middle_name',
                    'pers_num',
                    # 'list_phones',
                    'status')
    # list_prefetch_related = ['phones']
    list_display_links = ('name_lfm',)
    search_fields = ['name_lfm']
    # list_filter = ('status',)
    # inlines = [PhoneTabularInline, ]

    fields = ['last_name', 'first_name', 'middle_name',
              'pers_num', 'birth_date', 'gender', 'status']

    # autocomplete_fields = ['phones']

    def list_phones(self, obj):
        return mark_safe(', '.join([
            # f'<a href="{phone.get_admin_url()}">{str(phone)}</a>'
            str(phone)
            for phone in obj.phones.all()
        ]))

    list_phones.short_description = 'телефоны'


@admin.register(Employee)
class EmployeeAdmin(ModelAdmin):
    # Настройка списка
    list_display = ('tab_num', 'person', 'subdivision', 'dt_up', 'status')
    list_select_related = ['person', 'subdivision']
    list_display_links = ('tab_num',)
    search_fields = ('tab_num', 'person__name_lfm',)
    # list_filter = ('subdivision', 'status',)
    # Настройка формы
    fields = ['tab_num', 'person', 'subdivision', 'status']
    autocomplete_fields = ['person', 'subdivision']


@admin.register(Subdivision)
class SubdivisionAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title', 'name_sd',)
    list_display_links = ('indented_title', 'name_sd',)
    search_fields = ['name_sd']

    fields = ['name_sd', 'name_sd_full', 'parent', 'status']
    autocomplete_fields = ['parent']

# admin.site.register(Subdivision, DraggableMPTTAdmin,
#                     list_display=('tree_actions', 'indented_title', 'name',),
#                     list_display_links=('indented_title', 'name',),
#                     search_fields=['name'],
#                     fields=['name', 'name_full', 'parent', 'status'],
#                     autocomplete_fields=['parent'],
#                     )
