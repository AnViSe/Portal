from django.db import models

from apps.references.models.address import Address
from apps.references.models.phone import Phone
from core.fields import GenderField, OBJ_TYPE_PHONE, StatusField, OBJ_TYPE_ADDRESS
from extensions.service import get_fml, get_lfm
from apps.references.models.base import BaseRefModel, FlexType


class Person(BaseRefModel):
    """Модель персоны"""

    last_name = models.CharField(max_length=100,
                                 verbose_name='Фамилия')
    first_name = models.CharField(max_length=100, blank=True, null=True,
                                  verbose_name='Имя')
    middle_name = models.CharField(max_length=100, blank=True, null=True,
                                   verbose_name='Отчество')
    name_lfm = models.CharField(max_length=150, db_index=True, editable=False,
                                verbose_name='Фамилия И.О.')
    name_fml = models.CharField(max_length=150, editable=False,
                                verbose_name='И.О. Фамилия')
    pers_num = models.CharField(max_length=14, db_index=True, blank=True, null=True,
                                verbose_name='Личный номер')
    birth_date = models.DateField(blank=True, null=True,
                                  verbose_name='Дата рождения')
    gender = GenderField()
    phones = models.ManyToManyField(Phone, through='PersonPhones',
                                    related_name='persons',
                                    verbose_name='Телефоны')
    addresses = models.ManyToManyField(Address, through='PersonAddresses',
                                       related_name='persons',
                                       verbose_name='Адреса')

    class Meta(BaseRefModel.Meta):
        db_table = 'ref_person'
        verbose_name = 'персона'
        verbose_name_plural = 'персоны'
        ordering = ['id']

    class Params(BaseRefModel.Params):
        route_list = 'persons'
        route_list_api = 'person-list'
        fields_list = [
            {'data': 'id', 'title': 'Код'},
            {'data': 'last_name', 'title': 'Фамилия'},
            {'data': 'first_name', 'title': 'Имя'},
            {'data': 'middle_name', 'title': 'Отчество'},
            {'data': 'pers_num', 'title': 'Личный номер'},
            {'data': 'status', 'title': 'Статус'},
        ]

    def __str__(self):
        return self.name_lfm

    def save(self, *args, **kwargs):
        self.last_name = str(self.last_name).capitalize()
        if self.first_name:
            self.first_name = str(self.first_name).capitalize()
        if self.middle_name:
            self.middle_name = str(self.middle_name).capitalize()
        self.name_lfm = get_lfm(self.last_name, self.first_name, self.middle_name)
        self.name_fml = get_fml(self.last_name, self.first_name, self.middle_name)
        super().save(*args, **kwargs)


class PersonPhones(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE,
                               verbose_name='Персона')
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE,
                              verbose_name='Телефон')
    phone_type = models.ForeignKey(FlexType, on_delete=models.SET_NULL, blank=True, null=True,
                                   limit_choices_to={'type_object_id': OBJ_TYPE_PHONE},
                                   verbose_name='Тип')
    phone_desc = models.CharField(max_length=100, blank=True, null=True,
                                  verbose_name='Примечание')
    status = StatusField()

    class Meta:
        app_label = 'references'
        db_table = 'ref_person_phones'
        verbose_name = 'Телефон персоны'
        verbose_name_plural = 'Телефоны персоны'

    def __str__(self):
        return ''


class PersonAddresses(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE,
                               verbose_name='Персона')
    address = models.ForeignKey(Address, on_delete=models.CASCADE,
                                verbose_name='Адрес')
    address_type = models.ForeignKey(FlexType, on_delete=models.SET_NULL, blank=True, null=True,
                                     limit_choices_to=OBJ_TYPE_ADDRESS,
                                     verbose_name='Тип')
    address_desc = models.CharField(max_length=100, blank=True, null=True,
                                    verbose_name='Примечание')
    status = StatusField()

    class Meta:
        app_label = 'references'
        db_table = 'ref_person_addresses'
        verbose_name = 'Адрес персоны'
        verbose_name_plural = 'Адреса персоны'

    def __str__(self):
        return ''
