from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from core.fields import CodeField, StatusField


class FlexType(models.Model):
    """Гибкая модель типов сущностей"""

    type_code = CodeField(blank=True, null=True)
    type_name = models.CharField(max_length=100, verbose_name='Наименование')
    type_name_full = models.CharField(max_length=255, blank=True, null=True, verbose_name='Полное наименование')
    type_desc = models.CharField(max_length=255, blank=True, null=True, verbose_name='Описание')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, verbose_name='Объект')
    # object_id = models.PositiveIntegerField()
    # content_object = GenericForeignKey('content_type', 'object_id')
    # status = StatusField()

    class Meta:
        db_table = 'ref_type'
        verbose_name = 'тип'
        verbose_name_plural = 'типы'
        ordering = ['id']

    def __str__(self):
        return self.type_name
