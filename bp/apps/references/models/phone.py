from django.db import models

from apps.references.models.base import BaseRefModel, FlexType
from extensions.utils import limit_content_type


class Phone(BaseRefModel):
    phone_number = models.CharField(max_length=15,
                                    verbose_name='Номер телефона')

    model_type = models.ForeignKey(FlexType, on_delete=models.SET_NULL,
                                   blank=True, null=True,
                                   limit_choices_to=limit_content_type('references', 'phone'),
                                   verbose_name='Тип')

    class Meta(BaseRefModel.Meta):
        db_table = 'ref_phone'
        verbose_name = 'телефон'
        verbose_name_plural = 'телефоны'
        ordering = ['id']

    class Params(BaseRefModel.Params):
        route_list = 'phones'
        route_list_api = 'phone-list'
        fields_list = [
            {'data': 'id', 'title': 'Код'},
            {'data': 'phone_number', 'title': 'Номер телефона'},
            {'data': 'model_type', 'title': 'Тип номера'},
            {'data': 'status', 'title': 'Статус'},
        ]

    def __str__(self):
        return self.phone_number
