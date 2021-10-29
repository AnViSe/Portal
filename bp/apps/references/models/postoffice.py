from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from apps.references.models.address import Address
from apps.references.models.base import BaseRefModel, FlexType
from apps.references.models.phone import Phone
from core.fields import CodeField, OBJ_TYPE_PHONE, OBJ_TYPE_POST_OFFICE, StatusField


class PostOffice(BaseRefModel, MPTTModel):
    """Почтовое отделение"""

    code = CodeField(unique=True)
    zipcode = models.DecimalField(max_digits=6, decimal_places=0, unique=True,
                                  verbose_name='Индекс')
    parent = TreeForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,
                            related_name='children',
                            verbose_name='Родитель')
    name_post = models.CharField(max_length=100,
                                 verbose_name='Наименование')
    model_type = models.ForeignKey(FlexType, on_delete=models.SET_NULL, blank=True, null=True,
                                   limit_choices_to={'type_object_id': OBJ_TYPE_POST_OFFICE},
                                   verbose_name='Тип')
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, blank=True, null=True,
                                verbose_name='Адрес')
    phones = models.ManyToManyField(Phone, through='PostPhones',
                                    related_name='post_offices',
                                    verbose_name='Телефоны')
    schedule_post = models.CharField(max_length=200, blank=True, null=True,
                                     verbose_name='График работы')
    holiday_post = models.CharField(max_length=50, blank=True, null=True,
                                    verbose_name='Выходные дни')

    class Meta(BaseRefModel.Meta):
        db_table = 'ref_post_office'
        verbose_name = 'почтовое отделение'
        verbose_name_plural = 'почтовые отделения'

    class MPTTMeta:
        order_insertion_by = ['id']

    class Params(BaseRefModel.Params):
        route_list = 'postoffices'
        route_list_api = 'postoffice-list'
        fields_list = [
            {'data': 'id', 'title': 'ID'},
            # {'data': 'code', 'title': 'Код'},
            {'data': 'zipcode', 'title': 'Индекс'},
            {'data': 'name_post', 'title': 'Наименование'},
            {'data': 'model_type', 'name': 'model_type.type_name', 'title': 'Тип'},
            {'data': 'parent', 'name': 'parent.name_post', 'title': 'Родитель'},
            {'data': 'address', 'name': 'address.name_adds_full', 'title': 'Адрес'},
            {'data': 'status', 'title': 'Статус'},
        ]

    def __str__(self):
        return self.name_post


class PostPhones(models.Model):
    """Телефоны почтового отделения"""

    post_office = models.ForeignKey(PostOffice, on_delete=models.CASCADE,
                                    verbose_name='Почтовое отделение')
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE,
                              verbose_name='Телефон')
    phone_type = models.ForeignKey(FlexType, on_delete=models.SET_NULL, blank=True, null=True,
                                   limit_choices_to={'type_object_id': OBJ_TYPE_PHONE},
                                   verbose_name='Тип')
    phone_desc = models.CharField(max_length=100, blank=True, null=True,
                                  verbose_name='Примечание')
    status = StatusField()

    class Meta:
        app_label = 'references'
        db_table = 'ref_post_phones'
        unique_together = ['post_office', 'phone']
        verbose_name = 'Телефон отделения'
        verbose_name_plural = 'Телефоны отделения'

    def __str__(self):
        return ''
