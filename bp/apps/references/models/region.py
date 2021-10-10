from django.db import models

from apps.references.models.base import BaseRefModel
from apps.references.models.country import Country
from core.fields import CodeField


class Region(BaseRefModel):
    code = CodeField()
    country = models.ForeignKey(Country,
                                on_delete=models.SET_NULL,
                                blank=True, null=True,
                                # related_name='region',
                                verbose_name='Страна')
    name = models.CharField(max_length=60,
                            verbose_name='Наименование')

    class Meta(BaseRefModel.Meta):
        abstract = True
        db_table = 'ref_region'
        verbose_name = 'область'
        verbose_name_plural = 'области'

    class Params(BaseRefModel.Params):
        route_list = 'regions'
        route_list_api = 'region-list'
        fields_list = [
            {'name': 'id', 'title': 'Код'},
            {'name': 'code', 'title': 'Код1'},
            {'name': 'name', 'title': 'Наименование'},
            {'name': 'country', 'title': 'Страна'},
        ]

    def __str__(self):
        return self.name
