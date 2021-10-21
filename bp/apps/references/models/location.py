from django.db import models

from apps.references.models.base import BaseRefModel, FlexType
from apps.references.models.district import District
from core.fields import CodeField
from extensions.utils import limit_content_type


class Location(BaseRefModel):
    code = CodeField(unique=True)
    soato = models.BigIntegerField(unique=True,
                                   verbose_name='СОАТО')
    name_lct = models.CharField(max_length=100, verbose_name='Наименование')
    name_lct_full = models.CharField(max_length=150, verbose_name='Наименование полное',
                                     editable=False)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True,
                                 verbose_name='район')
    model_type = models.ForeignKey(FlexType, on_delete=models.SET_NULL,
                                   blank=True, null=True,
                                   limit_choices_to=limit_content_type('references', 'location'),
                                   verbose_name='Тип')

    class Meta(BaseRefModel.Meta):
        db_table = 'ref_location'
        verbose_name = 'населенный пункт'
        verbose_name_plural = 'населенные пункты'
        ordering = ['id']

    class Params(BaseRefModel.Params):
        route_list = 'locations'
        route_list_api = 'location-list'
        fields_list = [
            {'data': 'id', 'title': 'ID'},
            {'data': 'code', 'title': 'Код'},
            {'data': 'model_type', 'title': 'Тип'},
            {'data': 'name_lct', 'title': 'Наименование'},
            {'data': 'name_lct_full', 'title': 'Наименование полное'},
            {'data': 'district', 'name': 'district.name_dst', 'title': 'Район'},
            {'data': 'status', 'title': 'Статус'},
        ]

    def __str__(self):
        return self.name_lct
