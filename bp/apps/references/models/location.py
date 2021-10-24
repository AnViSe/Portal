from django.db import models

from apps.references.models.base import BaseRefModel, FlexType
from apps.references.models.district import District
from apps.references.models.street import Street
from core.fields import CodeField, OBJ_TYPE_LOCATION


class Location(BaseRefModel):
    code = CodeField(unique=True)
    soato = models.BigIntegerField(unique=True,
                                   verbose_name='СОАТО')
    name_lct = models.CharField(max_length=100,
                                verbose_name='Наименование')
    name_lct_full = models.CharField(max_length=150, db_index=True, editable=False,
                                     verbose_name='Наименование полное')
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True,
                                 verbose_name='Район')
    model_type = models.ForeignKey(FlexType, on_delete=models.SET_NULL, blank=True, null=True,
                                   limit_choices_to=OBJ_TYPE_LOCATION,
                                   verbose_name='Тип')
    streets = models.ManyToManyField(Street, through='LocationStreets',
                                     related_name='streets',
                                     verbose_name='Улицы')

    class Meta(BaseRefModel.Meta):
        db_table = 'ref_location'
        verbose_name = 'населенный пункт'
        verbose_name_plural = 'населенные пункты'
        ordering = ['id']

    class Params(BaseRefModel.Params):
        route_list = 'locations'
        route_list_api = 'location-list'
        fields_list = [
            {'data': 'id', 'title': 'ID'},
            {'data': 'code', 'title': 'Код'},
            {'data': 'model_type', 'title': 'Тип'},
            {'data': 'name_lct', 'title': 'Наименование'},
            {'data': 'name_lct_full', 'title': 'Наименование полное'},
            {'data': 'district', 'name': 'district.name_dst', 'title': 'Район'},
            {'data': 'status', 'title': 'Статус'},
        ]

    def __str__(self):
        return self.name_lct

    def save(self, *args, **kwargs):
        if not self.name_lct_full:
            self.name_lct_full = f'{self.model_type.type_name} {self.name_lct}'
        super().save(*args, **kwargs)


class LocationStreets(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE,
                                 verbose_name='Населенный пункт')
    street = models.ForeignKey(Street, on_delete=models.CASCADE,
                               verbose_name='Улица')

    class Meta:
        app_label = 'references'
        db_table = 'ref_location_streets'
        verbose_name = 'Улица населенного пункта'
        verbose_name_plural = 'Улицы населенных пунктов'
        ordering = ['id']

