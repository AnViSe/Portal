from django.db import models

from apps.references.models.base import BaseRefModel, FlexType
from core.fields import OBJ_TYPE_PHONE_OPERATOR


class MobileManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related('model_type').filter(model_type__type_value='mobile')


class Phone(BaseRefModel):
    """Телефон"""

    phone_number = models.CharField(max_length=15, db_index=True,
                                    verbose_name='Номер телефона')
    model_type = models.ForeignKey(FlexType, on_delete=models.SET_NULL, blank=True, null=True,
                                   limit_choices_to={'type_object_id': OBJ_TYPE_PHONE_OPERATOR},
                                   related_name='+',
                                   verbose_name='Оператор')
    objects = models.Manager()
    mobiles = MobileManager()

    class Meta(BaseRefModel.Meta):
        db_table = 'ref_phone'
        verbose_name = 'телефон'
        verbose_name_plural = 'телефоны'
        ordering = ['id']

    class Params(BaseRefModel.Params):
        route_list = 'phones'
        route_list_api = 'phone-list'
        fields_list = [
            {'data': 'id', 'name': 'id', 'title': 'ID'},
            {'data': 'phone_number', 'name': 'phone_number', 'title': 'Номер телефона'},
            {'data': 'model_type', 'name': 'model_type', 'title': 'Тип номера'},
            {'data': 'status', 'name': 'status', 'title': 'Статус'},
        ]

    def __str__(self):
        return self.phone_number
