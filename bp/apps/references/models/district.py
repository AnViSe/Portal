from django.db import models

from apps.references.models.base import BaseRefModel
from apps.references.models.region import Region
from core.fields import CodeField


class District(BaseRefModel):
    """Район"""

    code = CodeField(unique=True)
    name_dst = models.CharField(max_length=60, db_index=True,
                                verbose_name='Наименование')
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, blank=True, null=True,
                               related_name='districts',
                               verbose_name='Область')

    class Meta(BaseRefModel.Meta):
        db_table = 'ref_district'
        verbose_name = 'район'
        verbose_name_plural = 'районы'
        ordering = ['id']

    class Params(BaseRefModel.Params):
        route_list = 'districts'
        route_list_api = 'district-list'
        fields_list = [
            {'data': 'id', 'name': 'id', 'title': 'ID'},
            {'data': 'code', 'name': 'code', 'title': 'Код'},
            {'data': 'name_dst', 'name': 'name_dst', 'title': 'Наименование'},
            {'data': 'region', 'name': 'region.name_rgn', 'title': 'Область'},
            {'data': 'status', 'name': 'status', 'title': 'Статус'},
        ]

    def __str__(self):
        return self.name_dst
