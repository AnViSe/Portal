from django.db import models

from mptt.models import MPTTModel, TreeForeignKey

from apps.references.models.base import BaseRefModel, FlexType
from apps.references.models.employee import Employee
from apps.references.models.location import Location
from core.fields import OBJ_TYPE_SUBDIVISION, OBJ_TYPE_GEN_IZV, CodeField


class Subdivision(BaseRefModel, MPTTModel):
    """Подразделение"""

    code = CodeField(unique=True)
    parent = TreeForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,
                            related_name='children',
                            verbose_name='Родитель')
    name_sd = models.CharField(max_length=50, db_index=True,
                               verbose_name='Наименование')
    name_sd_full = models.CharField(max_length=255, blank=True, null=True,
                                    verbose_name='Наименование полное')
    model_type = models.ForeignKey(FlexType, on_delete=models.SET_NULL, blank=True, null=True,
                                   limit_choices_to={'type_object_id': OBJ_TYPE_SUBDIVISION},
                                   related_name='model_type',
                                   verbose_name='Тип')
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, blank=True, null=True,
                                 verbose_name='Населенный пункт')
    chief = models.ForeignKey(Employee, on_delete=models.SET_NULL, blank=True, null=True,
                              related_name='chief',
                              verbose_name='Руководитель')
    sub_chief = models.ForeignKey(Employee, on_delete=models.SET_NULL, blank=True, null=True,
                                  related_name='sub_chief',
                                  verbose_name='Заместитель руководителя')
    booker = models.ForeignKey(Employee, on_delete=models.SET_NULL, blank=True, null=True,
                               related_name='booker',
                               verbose_name='Бухгалтер')
    gi_type = models.ForeignKey(FlexType, on_delete=models.SET_NULL, blank=True, null=True,
                                limit_choices_to={'type_object_id': OBJ_TYPE_GEN_IZV},
                                related_name='gi_type',
                                verbose_name='Тип генерации извещений')
    code_ext = models.CharField(max_length=15, blank=True, null=True,
                                verbose_name='Внешний код')

    class Meta(BaseRefModel.Meta):
        db_table = 'ref_subdivision'
        verbose_name = 'подразделение'
        verbose_name_plural = 'подразделения'

    class MPTTMeta:
        order_insertion_by = ['id']

    class Params(BaseRefModel.Params):
        route_list = 'subdivisions'
        route_list_api = 'subdivision-list'
        fields_list = [
            {'data': 'id', 'title': 'ID'},
            {'data': 'code', 'title': 'Код'},
            {'data': 'name_sd', 'title': 'Наименование'},
            {'data': 'parent', 'title': 'Родитель'},
            {'data': 'status', 'title': 'Статус'},
        ]

    def __str__(self):
        return self.name_sd
