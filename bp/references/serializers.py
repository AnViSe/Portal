from rest_framework import serializers

from references.models import Country, Employee, Region


class EmployeeSerializer(serializers.ModelSerializer):
    """Список сотрудников"""

    class Meta:
        model = Employee
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    """Список стран"""

    class Meta:
        model = Country
        fields = '__all__'


class RegionSerializer(serializers.ModelSerializer):
    """Список областей"""

    class Meta:
        model = Region
        fields = '__all__'
