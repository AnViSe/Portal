from django.contrib.contenttypes.models import ContentType
from django.db import models

from core.fields import CodeField, CreateDateTimeField, StatusField, UpdateDateTimeField


class BaseRefModel(models.Model):
    """Базовая модель для справочников"""

    id = models.BigAutoField(primary_key=True,
                             verbose_name='ID')
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


class FlexType(models.Model):
    """Гибкая модель типов сущностей"""

    type_code = CodeField(blank=True, null=True)
    type_name = models.CharField(max_length=100,
                                 verbose_name='Наименование')
    type_name_full = models.CharField(max_length=255, blank=True, null=True,
                                      verbose_name='Наименование полное')
    type_desc = models.CharField(max_length=255, blank=True, null=True,
                                 verbose_name='Описание')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,
                                     verbose_name='Объект')
    # object_id = models.PositiveIntegerField()
    # content_object = GenericForeignKey('content_type', 'object_id')
    status = StatusField()

    class Meta:
        app_label = 'references'
        db_table = 'ref_type'
        verbose_name = 'тип'
        verbose_name_plural = 'типы'
        ordering = ['id']

    def __str__(self):
        return self.type_name
