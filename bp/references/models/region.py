from django.db import models

from references.models import BaseRefModel, Country


class Region(BaseRefModel):
    code = models.PositiveSmallIntegerField(unique=True,
                                            verbose_name='Код1')
    country = models.ForeignKey(Country,
                                on_delete=models.SET_NULL,
                                blank=True, null=True,
                                related_name='region',
                                verbose_name='Страна')
    name = models.CharField(max_length=60,
                            verbose_name='Наименование')

    def __str__(self):
        return self.name

    class Meta(BaseRefModel.Meta):
        db_table = 'ref_region'
        verbose_name = 'область'
        verbose_name_plural = 'области'
