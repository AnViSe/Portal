from django.db import models

# Значения статуса
ROW_INACTIVE = 0
ROW_ACTIVE = 1
ROW_STATUS = [
    (ROW_INACTIVE, 'Неактивна'),
    (ROW_ACTIVE, 'Активна'),
]

# Значения пола
SEX_NONE = 0
SEX_MEN = 1
SEX_WOMEN = 2
SEX_CHOICES = [
    (SEX_NONE, 'Не указан'),
    (SEX_MEN, 'Мужской'),
    (SEX_WOMEN, 'Женский'),
]


class StatusField(models.SmallIntegerField):
    """Стутус записи"""

    def __init__(self, *args, **kwargs):
        kwargs['verbose_name'] = 'Статус'
        kwargs['choices'] = ROW_STATUS
        kwargs['default'] = ROW_ACTIVE
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs["verbose_name"]
        del kwargs["choices"]
        del kwargs["default"]
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


class SexField(models.SmallIntegerField):
    """Пол человека"""

    def __init__(self, *args, **kwargs):
        kwargs['verbose_name'] = 'Пол'
        kwargs['choices'] = SEX_CHOICES
        kwargs['default'] = SEX_NONE
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs["verbose_name"]
        del kwargs["choices"]
        del kwargs["default"]
        return name, path, args, kwargs
