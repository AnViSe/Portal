from django.db import models

from apps.references.models.base import BaseRefModel, FlexType
from core.fields import CodeField, OBJ_TYPE_STREET


class Street(BaseRefModel):
    code = CodeField(unique=True)
    name_str = models.CharField(max_length=100,
                                verbose_name='Наименование')
    name_str_full = models.CharField(max_length=150, db_index=True, editable=False,
                                     verbose_name='Наименование полное')
    model_type = models.ForeignKey(FlexType, on_delete=models.SET_NULL, blank=True, null=True,
                                   limit_choices_to={'type_object_id': OBJ_TYPE_STREET},
                                   verbose_name='Тип')

    class Meta(BaseRefModel.Meta):
        db_table = 'ref_street'
        verbose_name = 'улица'
        verbose_name_plural = 'улицы'
        ordering = ['id']

    class Params(BaseRefModel.Params):
        route_list = 'streets'
        route_list_api = 'street-list'
        fields_list = [
            {'data': 'id', 'title': 'ID'},
            {'data': 'code', 'title': 'Код'},
            # {'data': 'model_type', 'title': 'Тип'},
            # {'data': 'name_str', 'title': 'Наименование'},
            {'data': 'name_str_full', 'title': 'Наименование полное'},
            {'data': 'status', 'title': 'Статус'},
        ]

    def __str__(self):
        return self.name_str_full

    def save(self, *args, **kwargs):
        if not self.name_str_full:
            self.name_str_full = f'{self.model_type.type_name} {self.name_str}'
        super().save(*args, **kwargs)
