from django.db import models

from mptt.models import MPTTModel, TreeForeignKey

from apps.references.models import BaseRefModel


class Subdivision(BaseRefModel):
    """Модель подразделения"""
    parent = models.ForeignKey('self', on_delete=models.SET_NULL,
                               blank=True, null=True, related_name='child',
                               verbose_name='Родитель')
    name = models.CharField(max_length=50,
                            verbose_name='Наименование')

    class Meta(BaseRefModel.Meta):
        db_table = 'ref_subdivision'
        verbose_name = 'подразделение'
        verbose_name_plural = 'подразделения'


class SB(BaseRefModel, MPTTModel):
    parent = TreeForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,
                            verbose_name='Родитель', related_name='children')
    name = models.CharField(verbose_name='Наименование', max_length=50)

    def __str__(self):
        return self.name

    class Meta(BaseRefModel.Meta):
        db_table = 'ref_sd'
        verbose_name = 'подразделение'
        verbose_name_plural = 'подразделения'

    class MPTTMeta:
        order_insertion_by = ['name']

    class Params(BaseRefModel.Params):
        route_list = 'subdivisions'
        route_list_api = 'sb-list'
        fields_list = [
            # {'name': None, 'title': '', 'className': 'treegrid-control'},
            {'name': 'id', 'title': 'Код'},
            {'name': 'name', 'title': 'Наименование'},
        ]
