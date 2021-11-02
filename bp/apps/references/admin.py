from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.safestring import mark_safe
from mptt.admin import DraggableMPTTAdmin

from apps.references.forms import LocationAdminForm
from apps.references.models.address import Address
from apps.references.models.base import FlexType
from apps.references.models.building import Building
from apps.references.models.country import Country
from apps.references.models.district import District
from apps.references.models.employee import Employee
from apps.references.models.location import Location
from apps.references.models.person import Person
from apps.references.models.phone import Phone
from apps.references.models.postoffice import PostOffice
from apps.references.models.region import Region
from apps.references.models.street import Street
from apps.references.models.subdivision import Subdivision


@admin.register(Address)
class AddressAdmin(ModelAdmin):
    list_display = ['code', 'name_adds_full', 'status']
    search_fields = ['name_adds_full']


@admin.register(Building)
class BuildingAdmin(ModelAdmin):
    list_display = ['code', 'name_bld_full', 'status']
    search_fields = ['name_bld_full']


@admin.register(Country)
class CountryAdmin(ModelAdmin):
    list_display = ['code', 'name_cnt', 'alpha2', 'alpha3', 'status']
    search_fields = ['name_cnt']

    fields = ['code', 'name_cnt', 'alpha2', 'alpha3', 'status']


@admin.register(District)
class DistrictAdmin(ModelAdmin):
    list_display = ['code', 'name_dst', 'region', 'status']
    list_display_links = ['code']
    list_select_related = ['region']
    search_fields = ['name_dst']

    fields = ['code', 'name_dst', 'region', 'status']
    autocomplete_fields = ['region']


@admin.register(Employee)
class EmployeeAdmin(ModelAdmin):
    # Настройка списка
    list_display = ['tab_num', 'person', 'subdivision', 'dt_up', 'status']
    list_display_links = ['tab_num']
    list_select_related = ['person', 'subdivision']
    search_fields = ['tab_num', 'person__name_lfm']
    # list_filter = ('subdivision', 'status',)
    # Настройка формы
    fields = ['tab_num', 'person', 'subdivision', 'status']
    autocomplete_fields = ['person', 'subdivision']


@admin.register(FlexType)
class FlexTypeAdmin(ModelAdmin):
    list_display = ['type_code', 'type_name', 'type_name_full', 'type_object', 'status']
    list_display_links = ['type_code']
    list_select_related = ['type_object']
    search_fields = ['type_name']

    fields = ['type_code', 'type_name', 'type_object', 'status']
    # autocomplete_fields = ['content_type']


@admin.register(Location)
class LocationAdmin(ModelAdmin):
    list_display = ['code', 'soato', 'name_lct_full', 'district', 'status']
    list_display_links = ['code']
    list_select_related = ['district']
    search_fields = ['name_lct_full']

    form = LocationAdminForm
    # fields = ['code',
    #           'soato',
    #           'model_type',
    #           'name_lct',
    #           'district',
    #           'status']
    # autocomplete_fields = [
    #     'district',
        # 'model_type'
    # ]


@admin.register(Person)
class PersonAdmin(ModelAdmin):
    list_display = ['name_lfm', 'last_name', 'first_name', 'middle_name',
                    'pers_num',
                    # 'list_phones',
                    'status']
    # list_prefetch_related = ['phones']
    list_display_links = ['name_lfm']
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


# https://brainstorm.it/snippets/many-many-example-using-through-augment-m2m-relationships/
# class PersonForPhoneTabularInline(admin.TabularInline):
#     model = Phone.persons.through
#     extra = 0
#     autocomplete_fields = ['person', ]


@admin.register(Phone)
class PhoneAdmin(ModelAdmin):
    list_display = ['phone_number',
                    'model_type',
                    # 'list_persons',
                    'status']
    list_select_related = ['model_type']
    # list_prefetch_related = ['persons']
    list_display_links = ['phone_number']
    search_fields = ['phone_number']
    # inlines = [PersonForPhoneTabularInline, ]

    fields = [
        'phone_number',
        'model_type',
        'status']

    # autocomplete_fields = ['person']

    def list_persons(self, obj):
        return mark_safe(', '.join([
            # f'<a href="{person.get_admin_url()}">{str(person)}</a>'
            f'<a href="#">{str(person)}</a>'
            # str(person)
            for person in obj.persons.all()
        ]))

    # list_persons.short_description = 'персоны'


# class PhoneTabularInline(admin.TabularInline):
#     model = Phone.persons.through
#     extra = 0
#     autocomplete_fields = ['phone', ]

@admin.register(PostOffice)
class PostOfficeAdmin(DraggableMPTTAdmin):
    list_display = ['tree_actions', 'indented_title', 'zipcode', 'name_post']
    list_display_links = ['indented_title', 'name_post']
    search_fields = ['name_post']

    fields = ['zipcode', 'name_post', 'parent',
              'model_type', 'address', 'schedule_post', 'holiday_post', 'status']
    autocomplete_fields = ['parent', 'address']


@admin.register(Region)
class RegionAdmin(ModelAdmin):
    list_display = ['code', 'name_rgn', 'country', 'status']
    list_display_links = ['code']
    list_select_related = ['country']
    search_fields = ['name_rgn']

    fields = ['code', 'name_rgn', 'country', 'status']
    autocomplete_fields = ['country']


@admin.register(Street)
class StreetAdmin(ModelAdmin):
    list_display = ['code', 'name_str_full', 'status']
    list_display_links = ['code']
    search_fields = ['name_str_full']

    fields = ['code', 'model_type', 'name_str', 'status']


@admin.register(Subdivision)
class SubdivisionAdmin(DraggableMPTTAdmin):
    list_display = ['tree_actions', 'indented_title', 'name_sd']
    list_display_links = ['indented_title', 'name_sd']
    search_fields = ['name_sd']

    fields = ['code', 'name_sd', 'parent',
              'model_type', 'location', 'chief', 'sub_chief', 'booker',
              'name_sd_full', 'code_ext', 'status']
    autocomplete_fields = ['parent', 'location', 'chief']
