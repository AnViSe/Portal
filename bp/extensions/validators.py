from django.core.exceptions import ValidationError
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _


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


def validate_image(content):
    """Validates if Content Type is an image."""
    if getattr(content.file, 'content_type', None):
        content_type = content.file.content_type.split('/')[0]
        if content_type != 'image':
            raise ValidationError(_("File type is not supported"), code='file-type')


def validate_size(content):
    """Validates if the size of the content in not too big."""
    if content.file.size > validate_size.MAX_UPLOAD_SIZE:
        message = _("Please keep file size under %(limit)s. Current file size %(current_size)s.")
        raise ValidationError(message, code='file-size', params={
            'limit': filesizeformat(validate_size.MAX_UPLOAD_SIZE),
            'current_size': filesizeformat(content.file.size),
        })


validate_size.MAX_UPLOAD_SIZE = 102400  # 100kB
validate_size.constraint = ('maxlength', validate_size.MAX_UPLOAD_SIZE)
