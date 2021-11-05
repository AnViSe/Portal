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


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
