from django.core.exceptions import ValidationError
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from extensions.service import get_fml, get_lfm
from apps.references.models import BaseRefModel
from extensions.validators import validate_phone_number


class Person(BaseRefModel):
    """Модель персоны"""
    SEX_NONE = 0
    SEX_MEN = 1
    SEX_WOMEN = 2
    SEX_CHOICES = [
        (SEX_NONE, 'Не указан'),
        (SEX_MEN, 'Мужской'),
        (SEX_WOMEN, 'Женский'),
    ]

    lastname = models.CharField(verbose_name='Фамилия', max_length=100)
    firstname = models.CharField(verbose_name='Имя', max_length=100, null=True, blank=True)
    middlename = models.CharField(verbose_name='Отчество', max_length=100, null=True, blank=True)
    name_lfm = models.CharField(verbose_name='Фамилия И.О.', max_length=150, editable=False)
    name_fml = models.CharField(verbose_name='И.О. Фамилия', max_length=150, editable=False)
    ident_num = models.CharField(verbose_name='Личный номер', max_length=14, null=True, blank=True)
    birth_date = models.DateField(verbose_name='Дата рождения', null=True, blank=True)
    sex = models.SmallIntegerField(verbose_name='Пол', choices=SEX_CHOICES, default=SEX_NONE)
    phone = PhoneNumberField(verbose_name='Телефон', blank=True, null=True)
    fax = models.CharField(verbose_name='Факс', max_length=12, blank=True, null=True,
                           validators=[validate_phone_number])

    # def __init__(self, *args, **kwargs):
    #     cls = self.__class__
    #     meta = getattr(cls, '_meta', None)
    #     setattr(meta, 'route_name', 'test_route')
    #     setattr(meta, 'url_list', 'test_url')
    #     super().__init__(*args, **kwargs)

    def __str__(self):
        return self.name_lfm

    # def clean(self):
    #     if not str(self.fax).startswith('375'):
    #         raise ValidationError('Номер должен начинаться на 375')

    def save(self, *args, **kwargs):
        self.name_lfm = get_lfm(self.lastname, self.firstname, self.middlename)
        self.name_fml = get_fml(self.lastname, self.firstname, self.middlename)
        super().save(*args, **kwargs)

    class Meta(BaseRefModel.Meta):
        db_table = 'ref_person'
        verbose_name = 'персона'
        verbose_name_plural = 'персоны'

    class Params(BaseRefModel.Params):
        route_list = 'persons'
        route_list_api = 'person-list'
        fields_list = [
            {'name': 'id', 'title': 'Код'},
            {'name': 'lastname', 'title': 'Фамилия'},
            {'name': 'firstname', 'title': 'Имя'},
            {'name': 'middlename', 'title': 'Отчество'},
            {'name': 'name_lfm', 'title': 'Фамилия И.О.'},
            # {'name': 'phone', 'title': 'Телефон'},
            # {'name': 'fax', 'title': 'Факс'},
            # {"name": None, "title": "Операции"},
        ]
