from django.db import models

from core.fields import StatusField


class Module(models.Model):
    """Модуль"""

    id = models.BigAutoField(primary_key=True,
                             verbose_name='ID')
    name = models.CharField(max_length=100,
                            verbose_name='Наименование')
    desc = models.CharField(max_length=255, blank=True, null=True,
                            verbose_name='Описание')
    route = models.CharField(max_length=100, blank=True, null=True,
                             verbose_name='Имя маршрута')
    perm = models.CharField(max_length=100, blank=True, null=True,
                            verbose_name='Разрешение')
    icon = models.CharField(max_length=30, blank=True, null=True,
                            default='fas fa-microchip',
                            verbose_name='Иконка')
    sort = models.SmallIntegerField(default=999, db_index=True,
                                    verbose_name='Сортировка')
    status = StatusField()

    class Meta:
        app_label = 'modules'
        db_table = 'mdl_module'
        verbose_name = 'модуль'
        verbose_name_plural = 'модули'

    def __str__(self):
        return self.name
