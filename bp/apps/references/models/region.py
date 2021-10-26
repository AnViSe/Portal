from django.db import models

from apps.references.models.base import BaseRefModel
from apps.references.models.country import Country
from core.fields import CodeField


class Region(BaseRefModel):
    """Область"""

    code = CodeField(unique=True)
    name_rgn = models.CharField(max_length=60, db_index=True,
                                verbose_name='Наименование')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True,
                                verbose_name='Страна')

    class Meta(BaseRefModel.Meta):
        db_table = 'ref_region'
        verbose_name = 'область'
        verbose_name_plural = 'области'
        ordering = ['id']

    class Params(BaseRefModel.Params):
        route_list = 'regions'
        route_list_api = 'region-list'
        fields_list = [
            {'data': 'id', 'title': 'ID'},
            {'data': 'code', 'title': 'Код'},
            {'data': 'name_rgn', 'title': 'Наименование'},
            {'data': 'country', 'name': 'country.name_cnt', 'title': 'Страна'},
            {'data': 'status', 'title': 'Статус'},
        ]

    def __str__(self):
        return self.name_rgn
