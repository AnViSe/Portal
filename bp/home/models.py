from django.db import models


class Menu(models.Model):
    parent = models.ForeignKey('self', on_delete=models.SET_NULL,
                               blank=True, null=True,
                               verbose_name='Родитель')
    name = models.CharField(max_length=100,
                            verbose_name='Заголовок')
    route = models.CharField(max_length=100,
                             blank=True, null=True,
                             verbose_name='Имя маршрута')
    icon = models.CharField(max_length=30,
                            blank=True, null=True,
                            default='fas fa-circle',
                            verbose_name='Иконка')
    badge = models.CharField(max_length=20,
                             blank=True, null=True,
                             verbose_name='Метка')
    sort = models.SmallIntegerField(default=999, db_index=True,
                                    verbose_name='Сортировка')
    status = models.SmallIntegerField(default=1, db_index=True,
                                      verbose_name='Статус')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
