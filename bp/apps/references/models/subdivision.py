from django.db import models

from mptt.models import MPTTModel, TreeForeignKey

from apps.references.models.base import BaseRefModel


class Subdivision(BaseRefModel, MPTTModel):
    """Модель подразделения"""

    parent = TreeForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,
                            related_name='children',
                            verbose_name='Родитель')
    name_sd = models.CharField(max_length=50, db_index=True,
                               verbose_name='Наименование')
    name_sd_full = models.CharField(max_length=255, blank=True, null=True,
                                    verbose_name='Наименование полное')

    class Meta(BaseRefModel.Meta):
        db_table = 'ref_subdivision'
        verbose_name = 'подразделение'
        verbose_name_plural = 'подразделения'

    class MPTTMeta:
        order_insertion_by = ['id']

    class Params(BaseRefModel.Params):
        route_list = 'subdivisions'
        route_list_api = 'subdivision-list'
        fields_list = [
            {'data': 'id', 'title': 'Код'},
            {'data': 'name_sd', 'title': 'Наименование'},
            {'data': 'parent', 'title': 'Родитель'},
            {'data': 'status', 'title': 'Статус'},
        ]

    def __str__(self):
        return self.name_sd
