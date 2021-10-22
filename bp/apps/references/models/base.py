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


class FlexObject(models.Model):
    """Список моделей для которых есть типы"""

    id = models.PositiveIntegerField(primary_key=True,
                                     verbose_name='ID')
    object_name = models.CharField(max_length=100,
                                   verbose_name='Наименование')
    object_app = models.CharField(max_length=100,
                                  verbose_name='Приложение')
    object_model = models.CharField(max_length=100,
                                    verbose_name='Модель')

    class Meta:
        app_label = 'references'
        db_table = 'ref_object'
        unique_together = ['object_app', 'object_model']
        verbose_name = 'объект'
        verbose_name_plural = 'объекты'
        ordering = ['id']

    def __str__(self):
        return self.object_name


class FlexType(models.Model):
    """Гибкая модель типов сущностей"""

    type_code = CodeField()
    type_name = models.CharField(max_length=100,
                                 verbose_name='Наименование')
    type_name_full = models.CharField(max_length=255, blank=True, null=True,
                                      verbose_name='Наименование полное')
    type_desc = models.CharField(max_length=255, blank=True, null=True,
                                 verbose_name='Описание')
    type_object = models.ForeignKey(FlexObject, on_delete=models.SET_NULL, blank=True, null=True,
                                    verbose_name='Имя модели')
    status = StatusField()

    class Meta:
        app_label = 'references'
        db_table = 'ref_type'
        unique_together = ['type_object', 'type_code']
        verbose_name = 'тип'
        verbose_name_plural = 'типы'
        ordering = ['id']

    def __str__(self):
        return self.type_name
