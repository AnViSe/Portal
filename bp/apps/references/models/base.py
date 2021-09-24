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

    # def __init__(self, *args, **kwargs):
    #     cls = self.__class__
    #     meta = getattr(cls, '_meta', None)
    #     setattr(meta, 'route_name', 'test_route')
    #     setattr(meta, 'url_list', 'test_url')
    #     super().__init__(*args, **kwargs)

    # @classmethod
    # def get_attr_value(cls, attr_name):
        # return getattr(cls, f'{attr_name}', 'test')
        # return cls.

    class Meta:
        managed = False
        app_label = 'references'
        abstract = True

    class Params:
        route_list = None
        route_list_api = None

        fields_list = []
