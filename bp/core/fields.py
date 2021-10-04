from django.db import models


class StatusField(models.SmallIntegerField):
    ROW_INACTIVE = 0
    ROW_ACTIVE = 1
    ROW_STATUS = [
        (ROW_INACTIVE, 'Неактивна'),
        (ROW_ACTIVE, 'Активна'),
    ]

    def __init__(self, verbose_name=None, choices=None, default=None, **kwargs):
        if verbose_name is None:
            kwargs['verbose_name'] = 'Статус'
        else:
            kwargs['verbose_name'] = verbose_name
        super().__init__(**kwargs)
        # self.choices = ROW
