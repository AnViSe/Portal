from django.db import models
from django.urls import reverse_lazy

from .person import Person
from .subdivision import Subdivision
from .base import BaseRefModel


# from extensions.service import get_fml, get_lfm


class Employee(BaseRefModel):
    """Модель сотрудника"""
    pers_num = models.PositiveIntegerField(verbose_name='Табельный', unique=True)
    person = models.ForeignKey(Person, verbose_name='Персона',
                               on_delete=models.SET_NULL, blank=True, null=True,
                               related_name='employees')
    subdivision = models.ForeignKey(Subdivision, verbose_name='Подразделение',
                                    on_delete=models.SET_NULL, blank=True, null=True,
                                    related_name='employees')

    def __str__(self):
        if self.person:
            return f'{self.person} ({self.pers_num})'
        else:
            return str(self.pers_num)

    # def get_absolute_url(self):
    # return reverse('view_employee', kwargs={"pk": self.pk})
    # return reverse_lazy('employees')

    class Meta(BaseRefModel.Meta):
        db_table = 'ref_employee'
        verbose_name = 'сотрудник'
        verbose_name_plural = 'сотрудники'

    # class Params(BaseRefModel.Params):
    #     route_list = 'employees'
    #     route_list_api = 'employee-list'
    #     fields_list = [
    #         {'name': 'id', 'title': 'Код'},
    #         {'name': 'lastname', 'title': 'Фамилия'},
    #         {'name': 'firstname', 'title': 'Имя'},
    #         {'name': 'middlename', 'title': 'Отчество'},
    #         {'name': 'name_lfm', 'title': 'Фамилия И.О.'},
    #     ]
