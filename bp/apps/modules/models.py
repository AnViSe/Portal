from django.db import models

from core.fields import StatusField


class Module(models.Model):
    """Модель описания модуля"""

    id = models.BigAutoField(primary_key=True,
                             verbose_name='Идентификатор')
    name = models.CharField(max_length=100,
                            verbose_name='Наименование')
    desc = models.CharField(max_length=255, blank=True, null=True,
                            verbose_name='Описание')
    perm = models.CharField(max_length=100, blank=True, null=True,
                            verbose_name='Разрешение')
    icon = models.CharField(max_length=30, blank=True, null=True,
                            default='fas fa-microchip',
                            verbose_name='Иконка')
    sort = models.SmallIntegerField(default=999, db_index=True,
                                    verbose_name='Сортировка')
    status = StatusField()

    class Meta:
        verbose_name = 'модуль'
        verbose_name_plural = 'модули'
