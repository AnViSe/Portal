from rest_framework import serializers

from apps.references.models import *


class PersonSerializer(serializers.ModelSerializer):
    """Список личностей (персон)"""

    class Meta:
        model = Person
        exclude = ('dt_cr', 'dt_up')


class EmployeeSerializer(serializers.ModelSerializer):
    """Список сотрудников"""

    class Meta:
        model = Employee
        exclude = ('dt_cr', 'dt_up')


class CountrySerializer(serializers.ModelSerializer):
    """Список стран"""

    class Meta:
        model = Country
        exclude = ('dt_cr', 'dt_up')


class RegionSerializer(serializers.ModelSerializer):
    """Список областей"""
    country = serializers.StringRelatedField(source='country.name', read_only=True)

    # country = CountrySerializer(read_only=True)
    # country = serializers.CharField(source='country.name', default='', read_only=True)

    class Meta:
        model = Region
        # fields = ['id', 'code', 'name', 'country', 'status']
        exclude = ('dt_cr', 'dt_up')
