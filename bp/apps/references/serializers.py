from rest_framework import serializers
from rest_framework.fields import ListField
from rest_framework_recursive.fields import RecursiveField

from apps.references.models import *


# class RecursiveSerializer(serializers.Serializer):
#     """Рекурсивный вывод children"""
#
#     def to_representation(self, instance):
#         serializer = self.parent.parent.__class__(instance, context=self.context)
#         return serializer.data


# class PersonSerializer(serializers.ModelSerializer):
#     """Список личностей (персон)"""

    # class Meta:
    #     model = Person
    #     exclude = ('dt_cr', 'dt_up')


# class EmployeeSerializer(serializers.ModelSerializer):
#     """Список сотрудников"""
#
#     class Meta:
#         model = Employee
#         exclude = ('dt_cr', 'dt_up')


# class CountrySerializer(serializers.ModelSerializer):
#     """Список стран"""
#
#     class Meta:
#         model = Country
#         exclude = ('dt_cr', 'dt_up')


# class RegionSerializer(serializers.ModelSerializer):
#     """Список областей"""
#     country = serializers.StringRelatedField(source='country.name', read_only=True)

    # country = CountrySerializer(read_only=True)
    # country = serializers.CharField(source='country.name', default='', read_only=True)

    # class Meta:
    #     model = Region
    #     fields = ['id', 'code', 'name', 'country', 'status']
        # exclude = ('dt_cr', 'dt_up')


# class FilterSubdivisionListSerializer(serializers.ListSerializer):
#     """Фильтр подразделений, только родители"""

    # def to_representation(self, data):
    #     print(data, type(data))
    #     data = data.filter(parent=None)
        # return super().to_representation(data)


# class SubdivisionSerializer(serializers.ModelSerializer):
#     """Список подразделений"""
    # children = RecursiveSerializer(many=True)
#    next = RecursiveField(allow_null=True)

#     class Meta:
        # list_serializer_class = FilterSubdivisionListSerializer
#        model = SB
#        fields = ('name', 'children')
        # exclude = ('dt_cr', 'dt_up')


# class SubdivisionTreeSerializer(serializers.ModelSerializer):
#     children = RecursiveField(many=True)
    # children = ListField(child=RecursiveField())

    # class Meta:
    #     model = SB
    #     fields = ('id', 'name', 'children', 'status')
