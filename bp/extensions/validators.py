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
