from django.db import models


class BaseRefModel(models.Model):
    """Базовая модель для справочников"""
    ROW_INACTIVE = 0
    ROW_ACTIVE = 1
    ROW_STATUS = [
        (ROW_INACTIVE, 'Неактивна'),
        (ROW_ACTIVE, 'Активна'),
    ]

    id = models.BigAutoField(primary_key=True,
                             verbose_name='Код')
    dt_cr = models.DateTimeField(verbose_name='Создана',
                                 auto_now_add=True)
    dt_up = models.DateTimeField(verbose_name='Изменена',
                                 auto_now=True)
    status = models.SmallIntegerField(verbose_name='Статус',
                                      choices=ROW_STATUS,
                                      default=ROW_ACTIVE)

    # @property
    # def actions(self):
    #     return '<button>Action</button>'

    class Meta:
        app_label = 'references'
        abstract = True
