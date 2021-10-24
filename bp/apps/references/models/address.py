from django.db import models

from apps.references.models.base import BaseRefModel
from apps.references.models.building import Building
from core.fields import CodeField


class Address(BaseRefModel):
    code = CodeField(unique=True)
    name_adds = models.CharField(max_length=10, blank=True, null=True,
                                 verbose_name='Квартира')
    name_adds_full = models.CharField(max_length=255, db_index=True, editable=False,
                                      verbose_name='Полный адрес')
    building = models.ForeignKey(Building, on_delete=models.SET_NULL, blank=True, null=True,
                                 verbose_name='Здание')

    class Meta(BaseRefModel.Meta):
        db_table = 'ref_address'
        verbose_name = 'адрес'
        verbose_name_plural = 'адреса'
        ordering = ['id']

    class Params(BaseRefModel.Params):
        route_list = 'addresses'
        route_list_api = 'address-list'
        fields_list = [
            {'data': 'id', 'title': 'ID'},
            {'data': 'code', 'title': 'Код'},
            {'data': 'name_adds_full', 'title': 'Адрес'},
            {'data': 'status', 'title': 'Статус'},
        ]

    def __str__(self):
        return self.name_adds_full

    def save(self, *args, **kwargs):
        if not self.name_adds_full:
            if self.name_adds:
                self.name_adds_full = f'{self.building.name_bld_full}, кв. {self.name_adds}'
            else:
                self.name_adds_full = f'{self.building.name_bld_full}'
        super().save(*args, **kwargs)
