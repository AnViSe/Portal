from django import template

from apps.home.models import Menu

register = template.Library()


@register.inclusion_tag('tags/menu_tree.html')
def show_menu_tree(cur_user=None, cur_url=None):
    menu_items = Menu.get_user_menu(user=cur_user)
    return {"menus": menu_items, "cur_url": cur_url}
