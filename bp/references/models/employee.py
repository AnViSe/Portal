from django.db import models

from .base import BaseRefModel
from extensions.service import get_fml, get_lfm


class Employee(BaseRefModel):
    """Модель сотрудника"""
    lastname = models.CharField(verbose_name='Фамилия', max_length=100)
    firstname = models.CharField(verbose_name='Имя', max_length=100, null=True, blank=True)
    middlename = models.CharField(verbose_name='Отчество', max_length=100, null=True, blank=True)
    name_lfm = models.CharField(verbose_name='Фамилия И.О.', max_length=150, editable=False)
    name_fml = models.CharField(verbose_name='И.О. Фамилия', max_length=150, editable=False)
    # persnum = models.PositiveIntegerField(verbose_name='Табельный', unique=True)

    def __str__(self):
        return self.name_lfm

    def save(self, *args, **kwargs):
        self.name_lfm = get_lfm(self.lastname, self.firstname, self.middlename)
        self.name_fml = get_fml(self.lastname, self.firstname, self.middlename)
        super().save(*args, **kwargs)

    class Meta(BaseRefModel.Meta):
        db_table = 'ref_employee'
        verbose_name = 'сотрудник'
        verbose_name_plural = 'сотрудники'
