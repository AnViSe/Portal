from django.db import models

from apps.references.models.phone import Phone
from core.fields import GenderField, PhoneTypeField, StatusField
from extensions.service import get_fml, get_lfm
from apps.references.models.base import BaseRefModel


class Person(BaseRefModel):
    """Модель персоны"""

    last_name = models.CharField(verbose_name='Фамилия', max_length=100, db_index=True)
    first_name = models.CharField(verbose_name='Имя', max_length=100, null=True, blank=True)
    middle_name = models.CharField(verbose_name='Отчество', max_length=100, null=True, blank=True)
    name_lfm = models.CharField(verbose_name='Фамилия И.О.', max_length=150, editable=False)
    name_fml = models.CharField(verbose_name='И.О. Фамилия', max_length=150, editable=False)
    pers_num = models.CharField(verbose_name='Личный номер', max_length=14,
                                null=True, blank=True, db_index=True)
    birth_date = models.DateField(verbose_name='Дата рождения', null=True, blank=True)
    gender = GenderField()
    phones = models.ManyToManyField(Phone, through='PersonPhones',
                                    related_name='persons',
                                    verbose_name='Телефоны')

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
    phone_type = PhoneTypeField()
    status = StatusField()

    class Meta:
        db_table = 'ref_person_phones'
        verbose_name = 'Телефон персоны'
        verbose_name_plural = 'Телефоны персоны'

    def __str__(self):
        return ''
