from django.db import models

from core.fields import CodeField
from .base import BaseRefModel


class Country(BaseRefModel):
    code = CodeField(unique=True)
    name_cnt = models.CharField(max_length=60, verbose_name='Наименование')
    alpha2 = models.CharField(max_length=2, verbose_name='Код2')
    alpha3 = models.CharField(max_length=3, verbose_name='Код3')

    class Meta(BaseRefModel.Meta):
        db_table = 'ref_country'
        verbose_name = 'страна'
        verbose_name_plural = 'страны'
        ordering = ['id']

    class Params(BaseRefModel.Params):
        route_list = 'countries'
        route_list_api = 'country-list'
        fields_list = [
            {'data': 'id', 'title': 'ID'},
            {'data': 'code', 'title': 'Код'},
            {'data': 'name_cnt', 'title': 'Наименование'},
            {'data': 'alpha2', 'title': 'Код 2'},
            {'data': 'alpha3', 'title': 'Код 3'},
            {'data': 'status', 'title': 'Статус'},
        ]

    def __str__(self):
        return self.name_cnt
