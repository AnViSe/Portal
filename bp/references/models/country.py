from django.db import models

from references.models import BaseRefModel


class Country(BaseRefModel):
    code = models.PositiveSmallIntegerField(unique=True,
                                            verbose_name='Код1')
    name = models.CharField(max_length=60,
                            verbose_name='Наименование')
    alpha2 = models.CharField(max_length=2,
                              verbose_name='Код2')
    alpha3 = models.CharField(max_length=3,
                              verbose_name='Код3')

    def __str__(self):
        return self.name

    class Meta(BaseRefModel.Meta):
        db_table = 'ref_country'
        verbose_name = 'страна'
        verbose_name_plural = 'страны'
