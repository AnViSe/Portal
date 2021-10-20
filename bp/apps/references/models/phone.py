from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models

from apps.references.models.base import BaseRefModel
from apps.references.models.flex_type import FlexType
from core.fields import PhoneTypeField


def limit_content_type(app, model):
    content_type = ContentType.objects.get_by_natural_key(app, model)
    return {'content_type': content_type.pk}


class Phone(BaseRefModel):
    phone_number = models.CharField(max_length=15,
                                    verbose_name='Номер телефона')

    model_type = models.ForeignKey(FlexType, on_delete=models.SET_NULL,
                                   blank=True, null=True,
                                   limit_choices_to=limit_content_type('references', 'phone'))

    # flex_type = GenericRelation(FlexType, related_query_name='flex_type')
    phone_type = PhoneTypeField()

    class Meta:
        db_table = 'ref_phone'
        verbose_name = 'телефон'
        verbose_name_plural = 'телефоны'
        ordering = ['id']

    class Params(BaseRefModel.Params):
        route_list = 'phones'
        route_list_api = 'phone-list'
        fields_list = [
            {'name': 'id', 'title': 'Код'},
            {'name': 'phone_number', 'title': 'Номер телефона'},
            # {'name': 'phone_type', 'title': 'Тип номера'},
            {'name': 'model_type', 'title': 'Тип номера'},
            {'name': 'status', 'title': 'Статус'},
        ]

    def __str__(self):
        return self.phone_number
