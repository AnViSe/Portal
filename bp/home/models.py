from django.db import models
from django.db.models import Count


class Menu(models.Model):
    parent = models.ForeignKey('self', on_delete=models.SET_NULL,
                               blank=True, null=True,
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
                            default='fas fa-circle',
                            verbose_name='Иконка')
    badge = models.CharField(max_length=20,
                             blank=True, null=True,
                             verbose_name='Метка')
    sort = models.SmallIntegerField(default=999, db_index=True,
                                    verbose_name='Сортировка')
    status = models.SmallIntegerField(default=1, db_index=True,
                                      verbose_name='Статус')

    def __str__(self):
        return self.name

    def get_user_menu(user=None):
        perms = user.get_all_permissions()
        menus = []
        for menu in Menu.objects.filter(status=1).order_by('sort').annotate(childs=Count('menu')):
            if menu.perm:
                if menu.perm in perms:
                    menus.append(menu)
            else:
                menus.append(menu)

        return menus

    class Meta:
        verbose_name = 'пункт меню'
        verbose_name_plural = 'пункты меню'
