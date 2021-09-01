from rest_framework import serializers

from references.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    """Список сотрудников"""

    class Meta:
        model = Employee
        fields = '__all__'
