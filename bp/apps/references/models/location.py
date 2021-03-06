from django.db import models

from apps.references.models.base import BaseRefModel, FlexType
from apps.references.models.district import District
from apps.references.models.street import Street
from core.fields import CodeField, OBJ_TYPE_LOCATION


class StreetsManager(models.Manager):
    def get_queryset(self):
        return Location.streets_set.filter(location=4)


class Location(BaseRefModel):
    """Населенный пункт"""

    code = CodeField(unique=True)
    soato = models.BigIntegerField(unique=True,
                                   verbose_name='СОАТО')
    name_lct = models.CharField(max_length=100,
                                verbose_name='Наименование')
    name_lct_full = models.CharField(max_length=150, db_index=True, editable=False,
                                     verbose_name='Наименование полное')
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True,
                                 related_name='locations',
                                 verbose_name='Район')
    model_type = models.ForeignKey(FlexType, on_delete=models.SET_NULL, blank=True, null=True,
                                   limit_choices_to={'type_object_id': OBJ_TYPE_LOCATION},
                                   related_name='+',
                                   verbose_name='Тип')
    streets = models.ManyToManyField(Street, through='LocationStreets',
                                     # related_name='streets',
                                     verbose_name='Улицы')

    objects = models.Manager
    loc_streets = StreetsManager

    class Meta(BaseRefModel.Meta):
        db_table = 'ref_location'
        verbose_name = 'населенный пункт'
        verbose_name_plural = 'населенные пункты'
        ordering = ['id']

    class Params(BaseRefModel.Params):
        route_list = 'locations'
        route_list_api = 'location-list'
        fields_list = [
            {'data': 'id', 'name': 'id', 'title': 'ID'},
            {'data': 'code', 'name': 'code', 'title': 'Код'},
            {'data': 'soato', 'name': 'soato', 'title': 'СОАТО'},
            # {'data': 'model_type', 'name': 'model_type.', 'title': 'Тип'},
            # {'data': 'name_lct', 'title': 'Наименование'},
            {'data': 'name_lct_full', 'name': 'name_lct_full', 'title': 'Наименование полное'},
            {'data': 'district', 'name': 'district.name_dst', 'title': 'Район'},
            {'data': 'status', 'name': 'status', 'title': 'Статус'},
        ]

    def __str__(self):
        return self.name_lct_full

    def save(self, *args, **kwargs):
        if not self.name_lct_full:
            self.name_lct_full = f'{self.model_type.type_name} {self.name_lct}'
        super().save(*args, **kwargs)


class LocationStreets(models.Model):
    """Улицы населенного пункта"""

    location = models.ForeignKey(Location, on_delete=models.CASCADE,
                                 verbose_name='Населенный пункт')
    street = models.ForeignKey(Street, on_delete=models.CASCADE,
                               verbose_name='Улица')
    street_desc = models.CharField(max_length=100, blank=True, null=True,
                                   verbose_name='Примечание')

    class Meta:
        app_label = 'references'
        db_table = 'ref_location_streets'
        unique_together = ['location', 'street']
        verbose_name = 'Улица населенного пункта'
        verbose_name_plural = 'Улицы населенных пунктов'

    def __str__(self):
        return self.street.name_str_full
