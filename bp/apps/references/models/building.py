from django.db import models

from apps.references.models.base import BaseRefModel
from apps.references.models.location import Location
from apps.references.models.street import Street
from core.fields import CodeField


class Building(BaseRefModel):
    code = CodeField(unique=True)
    name_bld = models.CharField(max_length=10,
                                verbose_name='Здание')
    name_bld_full = models.CharField(max_length=200, db_index=True, editable=False,
                                     verbose_name='Полный адрес здания')
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, blank=True, null=True,
                                 verbose_name='Населенный пункт')
    street = models.ForeignKey(Street, on_delete=models.SET_NULL, blank=True, null=True,
                               verbose_name='Улица')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True,
                                   verbose_name='Широта')
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True,
                                    verbose_name='Долгота')

    class Meta(BaseRefModel.Meta):
        db_table = 'ref_building'
        verbose_name = 'здание'
        verbose_name_plural = 'здания'
        ordering = ['id']

    class Params(BaseRefModel.Params):
        route_list = 'buildings'
        route_list_api = 'building-list'
        fields_list = [
            {'data': 'id', 'title': 'ID'},
            {'data': 'code', 'title': 'Код'},
            {'data': 'name_bld_full', 'title': 'Здание'},
            {'data': 'status', 'title': 'Статус'},
        ]

    def __str__(self):
        return self.name_bld_full

    def save(self, *args, **kwargs):
        if not self.name_bld_full:
            self.name_bld_full = f'{self.location.name_lct_full}, {self.street.name_str_full}, д. {self.name_bld}'
        super().save(*args, **kwargs)
