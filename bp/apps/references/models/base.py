from django.db import models

from core.fields import *


class BaseRefModel(models.Model):
    """Базовая модель для справочников"""

    id = models.BigAutoField(primary_key=True,
                             verbose_name='Идентификатор')
    dt_cr = CreateDateTimeField()
    dt_up = UpdateDateTimeField()
    status = StatusField()

    class Meta:
        app_label = 'references'
        abstract = True

    class Params:
        route_list = None
        route_list_api = None
        fields_list = []

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

