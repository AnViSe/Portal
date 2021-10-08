from django.db import models

from mptt.models import MPTTModel, TreeForeignKey

from apps.references.models.base import BaseRefModel


class Subdivision(BaseRefModel, MPTTModel):
    """Модель подразделения"""
    parent = TreeForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,
                            verbose_name='Родитель', related_name='children')
    name = models.CharField(max_length=50, db_index=True,
                            verbose_name='Наименование')
    name_full = models.CharField(max_length=255, blank=True, null=True,
                                 verbose_name='Наименование полное')

    class Meta(BaseRefModel.Meta):
        db_table = 'ref_subdivision'
        verbose_name = 'подразделение'
        verbose_name_plural = 'подразделения'

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

    class Params(BaseRefModel.Params):
        route_list = 'subdivisions'
        route_list_api = 'subdivision-list'
        fields_list = [
            # {'name': None, 'title': '', 'className': 'treegrid-control'},
            # {'name': 'id', 'title': 'Код'},
            {'name': 'name', 'title': 'Наименование'},
            {'name': 'parent', 'title': 'Родитель'},
            {'name': 'status', 'title': 'Статус'},
        ]
