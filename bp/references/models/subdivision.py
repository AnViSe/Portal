from django.db import models

from references.models import BaseRefModel


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
