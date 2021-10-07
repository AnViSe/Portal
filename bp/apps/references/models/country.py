from django.db import models

from .base import BaseRefModel


class Country(BaseRefModel):
    code = models.PositiveSmallIntegerField(unique=True,
                                            verbose_name='Код1')
    name = models.CharField(max_length=60,
                            verbose_name='Наименование')
    alpha2 = models.CharField(max_length=2,
                              verbose_name='Код2')
    alpha3 = models.CharField(max_length=3,
                              verbose_name='Код3')

    class Meta(BaseRefModel.Meta):
        abstract = True
        db_table = 'ref_country'
        verbose_name = 'страна'
        verbose_name_plural = 'страны'

    class Params(BaseRefModel.Params):
        route_list = 'countries'
        route_list_api = 'country-list'
        fields_list = [
            {'name': 'id', 'title': 'Код'},
            {'name': 'code', 'title': 'Код1'},
            {'name': 'name', 'title': 'Наименование'},
            {'name': 'alpha2', 'title': 'ISO2'},
            {'name': 'alpha3', 'title': 'ISO3'},
        ]

    def __str__(self):
        return self.name
