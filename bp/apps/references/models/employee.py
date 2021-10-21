from django.db import models

from .base import BaseRefModel
from .person import Person
from .subdivision import Subdivision


class Employee(BaseRefModel):
    """Модель сотрудника"""
    tab_num = models.PositiveIntegerField(verbose_name='Табельный', unique=True)
    person = models.ForeignKey(Person, verbose_name='Персона',
                               on_delete=models.SET_NULL, blank=True, null=True)
    subdivision = models.ForeignKey(Subdivision, verbose_name='Подразделение',
                                    on_delete=models.SET_NULL, blank=True, null=True)

    class Meta(BaseRefModel.Meta):
        db_table = 'ref_employee'
        verbose_name = 'сотрудник'
        verbose_name_plural = 'сотрудники'
        ordering = ['id']

    class Params(BaseRefModel.Params):
        route_list = 'employees'
        route_list_api = 'employee-list'
        fields_list = [
            {'data': 'id', 'title': 'Код'},
            {'data': 'tab_num', 'title': 'Табельный'},
            {'data': 'person', 'name': 'person.name_lfm', 'title': 'Физлицо'},
            {'data': 'subdivision', 'name': 'subdivision.name_sd', 'title': 'Подразделение'},
            {'data': 'status', 'title': 'Статус'},
        ]

    def __str__(self):
        if self.person:
            return f'{self.person} ({self.tab_num})'
        else:
            return str(self.tab_num)

    # def get_absolute_url(self):
    # return reverse('view_employee', kwargs={"pk": self.pk})
    # return reverse_lazy('employees')
