from django.core.exceptions import ValidationError


def validate_phone_number(value):
    digits = ''.join([i for i in str(value) if i.isdigit()])
    if len(digits) == 12:
        if not digits.startswith('375'):
            raise ValidationError(message="Номер телефона должен начинаться на 375.",
                                  code="invalid_phone_number")
    else:
        raise ValidationError(message='Количество цифр в номере должно быть 12',
                              code='invalid_phone_number')


def validate_ident_num_2012(value: str):
    """Контроль личного номера паспорта до 2012 года"""
    _digit_pos = [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 13]
    _latin_pos = [7, 11, 12]
    _phase_1 = True
    _phase_2 = True
    result = None
    if value:
        if len(value) == 14:
            for i in _digit_pos:
                _phase_1 = value[i].isdigit()
                if not _phase_1:
                    continue
            if _phase_1:
                for i in _latin_pos:
                    _phase_2 = value[i].isascii() and value[i].isupper()
                    if not _phase_2:
                        continue
            if not (_phase_1 and _phase_2):
                result = 'Некорректный номер. Только цифры и заглавные латинские буквы.'
        else:
            result = 'Длина должна быть 14 символов.'

    return result
