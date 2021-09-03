from django import template

register = template.Library()


@register.inclusion_tag('tags/menu_tree.html')
def show_menu_tree(params=None):
    menu_items = [{"title": "Меню 1", "url": "home", "icon": "fas fa-th", "badge": "12"},
                  {"title": "Меню 2", "url": "employees"}, ]
    return {"menus": menu_items}
