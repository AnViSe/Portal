from django.core.exceptions import ValidationError


def validate_phone_number(value):
    if value and not str(value).startswith('375'):
        raise ValidationError(message="Введенный номер телефона некорректен.",
                              code="invalid_phone_number")
