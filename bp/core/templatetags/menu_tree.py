from django import template
from django.core.cache import cache

from apps.home.models import Menu

register = template.Library()


# @register.inclusion_tag('tags/menu_tree.html')
# def show_menu_tree(cur_user=None, cur_url=None):
#     menu_items = Menu.get_user_menu(user=cur_user)
#     return {"menus": menu_items, "cur_url": cur_url}


@register.inclusion_tag('inc/_sidebar_menu.html')
def get_menu_tree(cur_user=None, cur_url=None):
    perms = {None}
    if cur_user:
        cached_perms = cache.get(f'user_perms_{cur_user.id}')
        if cached_perms is None:
            perms |= cur_user.get_all_permissions()
            cache.set(f'user_perms_{cur_user.id}', perms)
        else:
            perms = cached_perms

    menu_items = Menu.objects.filter(level=0)
    menus = menu_items.get_descendants(include_self=True).filter(status=1)
    return {'menus': menus, 'cur_url': cur_url, 'perms': perms}
