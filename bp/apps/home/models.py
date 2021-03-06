from django.core.cache import cache
from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from mptt.models import MPTTModel, TreeForeignKey

from core.fields import StatusField


class Menu(MPTTModel):
    """Модель меню"""

    parent = TreeForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,
                            verbose_name='Родитель', related_name='children')
    title = models.CharField(max_length=100,
                             verbose_name='Заголовок')
    route = models.CharField(max_length=100, blank=True, null=True,
                             verbose_name='Имя маршрута')
    perm = models.CharField(max_length=100, blank=True, null=True,
                            verbose_name='Разрешение')
    icon = models.CharField(max_length=30, blank=True, null=True,
                            default='far fa-circle',
                            verbose_name='Иконка')
    badge = models.CharField(max_length=20, blank=True, null=True,
                             verbose_name='Метка')
    header = models.BooleanField(default=False,
                                 verbose_name='Заголовок')
    status = StatusField()

    class Meta:
        verbose_name = 'пункт меню'
        verbose_name_plural = 'пункты меню'

    class MPTTMeta:
        order_insertion_by = ['-id']

    def __str__(self):
        return self.title

    # @staticmethod
    # def get_user_menu(user=None):
    #     menus = []
    #     if user:
    #         cached_perms = cache.get(f"user_perms_{user.id}")
    #         if cached_perms is None:
    #             perms = user.get_all_permissions()
    #             cache.set(f"user_perms_{user.id}", perms)
    #         else:
    #             perms = cached_perms
    #     else:
    #         perms = []
    #     cached_menus = cache.get('menu_items')
    #     if cached_menus is None:
    #         all_items = Menu.objects.filter(status=1).order_by('title').values()
    #         cache.set('menu_items', all_items)
    #     else:
    #         all_items = cached_menus
    #
    #     for item in all_items:
    #         if item['perm']:
    #             if item['perm'] in perms:
    #                 menus.append(item)
    #         else:
    #             menus.append(item)
    #
    #     menus = build_tree_menu(menus, None)
    #     return menus


@receiver(post_save, sender=Menu)
def menu_save(sender, instance, **kwargs):
    cache.delete('menu_items')


@receiver(pre_delete, sender=Menu)
def menu_delete(sender, instance, **kwargs):
    cache.delete('menu_items')
