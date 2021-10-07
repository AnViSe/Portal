from django.db import models

# Значения статуса
ROW_INACTIVE = 0
ROW_ACTIVE = 1
ROW_STATUS = [
    (ROW_INACTIVE, 'Неактивна'),
    (ROW_ACTIVE, 'Активна'),
]

# Значения пола
GENDER_NONE = 0
GENDER_MEN = 1
GENDER_WOMEN = 2
GENDER_CHOICES = [
    (GENDER_NONE, 'Не указан'),
    (GENDER_MEN, 'Мужской'),
    (GENDER_WOMEN, 'Женский'),
]


class CodeField(models.CharField):
    """Код записи"""

    def __init__(self, *args, **kwargs):
        kwargs['verbose_name'] = 'Код'
        kwargs['max_length'] = 15
        kwargs['unique'] = True
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs["verbose_name"]
        del kwargs["max_length"]
        del kwargs["unique"]
        return name, path, args, kwargs


class StatusField(models.SmallIntegerField):
    """Статус записи"""

    def __init__(self, *args, **kwargs):
        kwargs['verbose_name'] = 'Статус'
        kwargs['choices'] = ROW_STATUS
        kwargs['default'] = ROW_ACTIVE
        kwargs['db_index'] = True
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs["verbose_name"]
        del kwargs["choices"]
        del kwargs["default"]
        del kwargs["db_index"]
        return name, path, args, kwargs


class CreateDateTimeField(models.DateTimeField):
    """Дата и время создания записи"""

    def __init__(self, *args, **kwargs):
        kwargs['verbose_name'] = 'Создана'
        kwargs['auto_now_add'] = True
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs["verbose_name"]
        del kwargs["auto_now_add"]
        return name, path, args, kwargs


class UpdateDateTimeField(models.DateTimeField):
    """Дата и время изменения записи"""

    def __init__(self, *args, **kwargs):
        kwargs['verbose_name'] = 'Изменена'
        kwargs['auto_now'] = True
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs["verbose_name"]
        del kwargs["auto_now"]
        return name, path, args, kwargs


class GenderField(models.SmallIntegerField):
    """Пол человека"""

    def __init__(self, *args, **kwargs):
        kwargs['verbose_name'] = 'Пол'
        kwargs['choices'] = GENDER_CHOICES
        kwargs['default'] = GENDER_NONE
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs["verbose_name"]
        del kwargs["choices"]
        del kwargs["default"]
        return name, path, args, kwargs
