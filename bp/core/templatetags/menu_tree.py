from django import template
from django.core.cache import cache

from apps.home.models import Menu

register = template.Library()


@register.inclusion_tag('inc/_sidebar_menu.html')
def get_menu_tree(cur_user=None, cur_url=None):
    perms = {None}
    if cur_user:
        cached_perms = cache.get(f'perms_user_{cur_user.id}')
        if cached_perms is None:
            perms |= cur_user.get_all_permissions()
            cache.set(f'perms_user_{cur_user.id}', perms)
        else:
            perms = cached_perms

    cached_menus = cache.get('menu_items')
    if cached_menus is None:
        menu_main = Menu.objects.filter(level=0)
        menu_items = menu_main.get_descendants(include_self=True).filter(status=1)
        cache.set('menu_items', menu_items)
    else:
        menu_items = cached_menus

    menus = []
    for menu in menu_items:
        if not menu.perm or menu.perm in perms:
            menus.append(menu)

    return {'menus': menus, 'cur_url': cur_url}
