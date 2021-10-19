from django.db import models

from apps.references.models.base import BaseRefModel
from core.fields import PhoneTypeField


class Phone(BaseRefModel):
    phone_number = models.CharField(max_length=15,
                                    verbose_name='Номер телефона')
    phone_type = PhoneTypeField()

    class Meta:
        db_table = 'ref_phone'
        verbose_name = 'телефон'
        verbose_name_plural = 'телефоны'

    def __str__(self):
        return self.phone_number
