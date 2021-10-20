from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from apps.references.models.base import BaseRefModel
from apps.references.models.flex_type import FlexType
from core.fields import PhoneTypeField


class Phone(BaseRefModel):
    phone_number = models.CharField(max_length=15,
                                    verbose_name='Номер телефона')
    flex_type = GenericRelation(FlexType, related_query_name='flex_type')
    phone_type = PhoneTypeField()

    class Meta:
        db_table = 'ref_phone'
        verbose_name = 'телефон'
        verbose_name_plural = 'телефоны'

    class Params(BaseRefModel.Params):
        route_list = 'phones'
        route_list_api = 'phone-list'
        fields_list = [
            {'name': 'id', 'title': 'Код'},
            {'name': 'phone_number', 'title': 'Номер телефона'},
            {'name': 'phone_type', 'title': 'Тип номера'},
            {'name': 'status', 'title': 'Статус'},
        ]

    def __str__(self):
        return self.phone_number
