from django.db import models
from django.db.models import Count

from extensions.service import build_tree_menu


class Menu(models.Model):
    parent = models.ForeignKey('self', on_delete=models.SET_NULL,
                               blank=True, null=True, related_name='child',
                               verbose_name='Родитель')
    name = models.CharField(max_length=100,
                            verbose_name='Заголовок')
    route = models.CharField(max_length=100,
                             blank=True, null=True,
                             verbose_name='Имя маршрута')
    perm = models.CharField(max_length=100,
                            blank=True, null=True,
                            verbose_name='Разрешение')
    icon = models.CharField(max_length=30,
                            blank=True, null=True,
                            default='far fa-circle',
                            verbose_name='Иконка')
    badge = models.CharField(max_length=20,
                             blank=True, null=True,
                             verbose_name='Метка')
    header = models.BooleanField(default=False,
                                 verbose_name='Заголовок')
    sort = models.SmallIntegerField(default=999, db_index=True,
                                    verbose_name='Сортировка')
    status = models.SmallIntegerField(default=1, db_index=True,
                                      verbose_name='Статус')

    def __str__(self):
        return self.name

    def get_user_menu(user=None):
        menus = []
        if user:
            perms = user.get_all_permissions()
        else:
            perms = []

        all_items = Menu.objects.filter(status=1).order_by('sort').values()

        for item in all_items:
            if item['perm']:
                if item['perm'] in perms:
                    menus.append(item)
            else:
                menus.append(item)

        menus = build_tree_menu(menus, None)
        return menus

    class Meta:
        verbose_name = 'пункт меню'
        verbose_name_plural = 'пункты меню'
