from django.db import models

from .base import BaseRefModel
from .person import Person


class Employee(BaseRefModel):
    """Модель сотрудника"""
    tab_num = models.PositiveIntegerField(unique=True,
                                          verbose_name='Табельный')
    person = models.ForeignKey(Person, on_delete=models.SET_NULL, blank=True, null=True,
                               verbose_name='Персона')
    subdivision = models.ForeignKey(to='references.Subdivision', on_delete=models.SET_NULL, blank=True, null=True,
                                    verbose_name='Подразделение')

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
