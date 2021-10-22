from rest_framework import serializers
from rest_framework.fields import ListField, SerializerMethodField
from rest_framework_recursive.fields import RecursiveField

from apps.references.models.country import Country
from apps.references.models.district import District
from apps.references.models.employee import Employee
from apps.references.models.location import Location
from apps.references.models.person import Person
from apps.references.models.phone import Phone
from apps.references.models.region import Region
from apps.references.models.street import Street
from apps.references.models.subdivision import Subdivision


class DistrictSerializer(serializers.ModelSerializer):
    """Список районов"""

    region = serializers.StringRelatedField(source='region.name_rgn',
                                            default=None, read_only=True,
                                            label='Область')
    status = serializers.CharField(source='get_status_display',
                                   label='Статус')

    class Meta:
        model = District
        fields = ['id', 'code', 'name_dst', 'region', 'status']


class LocationSerializer(serializers.ModelSerializer):
    """Список населенных пунктов"""

    district = serializers.StringRelatedField(source='district.name_dst',
                                              default=None, read_only=True,
                                              label='Район')
    status = serializers.CharField(source='get_status_display',
                                   label='Статус')

    class Meta:
        model = Location
        fields = ['id', 'code', 'name_lct', 'district', 'status']


# class RecursiveSerializer(serializers.Serializer):
#     """Рекурсивный вывод children"""
#
#     def to_representation(self, instance):
#         serializer = self.parent.parent.__class__(instance, context=self.context)
#         return serializer.data


class PersonSerializer(serializers.ModelSerializer):
    """Список личностей (персон)"""

    gender = serializers.CharField(source='get_gender_display', label='Пол')
    status = serializers.CharField(source='get_status_display', label='Статус')

    class Meta:
        model = Person
        fields = ['id', 'last_name', 'first_name', 'middle_name', 'name_lfm',
                  'gender', 'birth_date', 'pers_num', 'status']

    # def get_status(self, obj):
    #     return obj.get_status_display()


class PhoneSerializer(serializers.ModelSerializer):
    """Список телефонных номеров"""

    phone_type = serializers.CharField(source='get_phone_type_display', label='Тип')
    model_type = serializers.StringRelatedField(source='model_type.type_name', read_only=True,
                                                default=None,
                                                label='Тип')
    status = serializers.CharField(source='get_status_display', label='Статус')

    class Meta:
        model = Phone
        fields = ['id', 'phone_number', 'phone_type', 'model_type', 'status']


class EmployeeSerializer(serializers.ModelSerializer):
    """Список сотрудников"""

    person = serializers.StringRelatedField(source='person.name_lfm', read_only=True)
    subdivision = serializers.StringRelatedField(source='subdivision.name_sd', read_only=True,
                                                 default=None)
    status = serializers.CharField(source='get_status_display', label='Статус')

    class Meta:
        model = Employee
        fields = ['id', 'tab_num', 'person', 'subdivision', 'status']


class CountrySerializer(serializers.ModelSerializer):
    """Список стран"""

    status = serializers.CharField(source='get_status_display',
                                   label='Статус')

    class Meta:
        model = Country
        fields = ['id', 'code', 'name_cnt', 'alpha2', 'alpha3', 'status']


class RegionSerializer(serializers.ModelSerializer):
    """Список областей"""

    country = serializers.StringRelatedField(source='country.name_cnt',
                                             default=None, read_only=True,
                                             label='Страна')
    status = serializers.CharField(source='get_status_display',
                                   label='Статус')

    class Meta:
        model = Region
        fields = ['id', 'code', 'name_rgn', 'country', 'status']


class StreetSerializer(serializers.ModelSerializer):
    """Список улиц"""

    # country = serializers.StringRelatedField(source='country.name_cnt',
    #                                          default=None, read_only=True,
    #                                          label='Страна')
    status = serializers.CharField(source='get_status_display',
                                   label='Статус')

    class Meta:
        model = Street
        fields = ['id', 'code', 'name_str_full', 'status']


# class FilterSubdivisionListSerializer(serializers.ListSerializer):
#     """Фильтр подразделений, только родители"""
#
#     def to_representation(self, data):
#         print(data, type(data))
#         data = data.filter(parent=None)
#         return super().to_representation(data)


class SubdivisionSerializer(serializers.ModelSerializer):
    """Список подразделений"""

    parent = serializers.StringRelatedField(source='parent.name_sd', read_only=True, default=None)
    status = serializers.CharField(source='get_status_display', label='Статус')

    # children = RecursiveSerializer(many=True)
    # next = RecursiveField(allow_null=True)

    class Meta:
        # list_serializer_class = FilterSubdivisionListSerializer

        model = Subdivision
        fields = ('id', 'name_sd', 'parent', 'status')


class SubdivisionTreeSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True)

    # children = ListField(child=RecursiveField())

    class Meta:
        model = Subdivision
        fields = ('id', 'name', 'children', 'status')


class SubdivisionTreeSerializer1(serializers.ModelSerializer):
    children = SerializerMethodField(source='get_children')

    class Meta:
        fields = ('children',)  # add here rest of the fields from model

    def get_children(self, obj):
        children = self.context['children'].get(obj.id, [])
        serializer = SubdivisionTreeSerializer(children, many=True, context=self.context)
        return serializer.data
