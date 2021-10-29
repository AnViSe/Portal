from django.db import models

from apps.references.models.address import Address
from apps.references.models.person import Person
from apps.references.models.phone import Phone
from apps.references.models.subdivision import Subdivision
from core.fields import BarcodeField, CreateDateTimeField, UpdateDateTimeField


class Mailing(models.Model):
    barcode = BarcodeField(unique=True)
    subdivision = models.ForeignKey(Subdivision, on_delete=models.CASCADE,
                                    verbose_name='Подразделение')
    person = models.ForeignKey(Person, on_delete=models.SET_NULL, blank=True, null=True,
                               verbose_name='Получатель')
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, blank=True, null=True,
                                verbose_name='Адрес доставки')
    phone = models.ForeignKey(Phone, on_delete=models.SET_NULL, blank=True, null=True,
                              verbose_name='Телефон получателя')
    notice_number = models.PositiveIntegerField(blank=True, null=True,
                                                verbose_name='№ извещения')

    dt_cr = CreateDateTimeField()
    dt_up = UpdateDateTimeField()

    class Meta:
        app_label = 'delivery'
        db_table = 'mdl_dlv_mailing'
        verbose_name = 'отправление'
        verbose_name_plural = 'отправления'

    def __str__(self):
        return self.barcode

    # def clean_fields(self, exclude=None):
    #     pass

    # def save(self, *args, **kwargs):
    #     if not self.notice_number:
    #         self.notice_number = self.get_notice_number(500)
    #     super().save(*args, **kwargs)

    # @staticmethod
    # def get_notice_number(arg):
    #     return arg
