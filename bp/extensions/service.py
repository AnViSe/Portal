def get_lfm(last_name, first_name=None, middle_name=None) -> str:
    """Из фаМиЛИя иМя ОтчЕство возвращает Фамилия И.О."""
    result = ''
    if last_name:
        result = last_name.capitalize()
        if first_name:
            result += ' ' + first_name[0].upper() + '.'
            if middle_name:
                result += middle_name[0].upper() + '.'
    return result


def get_fml(last_name, first_name=None, middle_name=None) -> str:
    """Из фаМиЛИя иМя ОтчЕство возвращает И.О. Фамилия"""
    result = ''
    if last_name:
        if first_name:
            result = first_name[0].upper() + '.'
            if middle_name:
                result += middle_name[0].upper() + '. ' + last_name.capitalize()
    return result


def build_tree_menu(items, parent):
    """Построение дерева меню"""
    result = []
    for item in items:
        if item['parent_id'] == parent:
            children = build_tree_menu(items, item['id'])
            if children:
                item['childs'] = children
                item['has_child'] = True
            else:
                item['childs'] = []
                item['has_child'] = False
            result.append(item)
    return result


def get_columns(model=None):
    fields = []
    if model:
        model_fields = model._meta.get_fields(include_parents=False, include_hidden=False)
        for field in model_fields:
            fields.append({"name": field.name,
                           "title": field.verbose_name,
                           "value": None,
                           })
    return fields
