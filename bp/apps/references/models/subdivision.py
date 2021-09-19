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
    parent = TreeForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')
    name = models.CharField(max_length=50)

    class MPTTMeta:
        app_label = 'references'
        db_table = 'ref_sd'
        verbose_name = 'подразделение'
        verbose_name_plural = 'подразделения'
        order_insertion_by = ['name']
