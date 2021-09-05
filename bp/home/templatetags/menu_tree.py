from django import template

from ..models import Menu

register = template.Library()


@register.inclusion_tag('tags/menu_tree.html')
def show_menu_tree(params=None, url=None):
    # menu_items = Menu.objects.filter(status=1).order_by('sort')
    # menu_items = [{"title": "Меню 1", "url": "home", "icon": "fas fa-th", "badge": "12"},
    #               {"title": "Меню 2", "url": "employees"}, ]
    menu_items = Menu.get_user_menu(user=params)
    return {"menus": menu_items, "cur_url": url}
