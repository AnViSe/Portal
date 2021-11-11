from django.contrib.auth.models import Group
from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand
from django.db import transaction

from apps.home.models import Menu
from apps.modules.models import Module
from apps.references.models.base import FlexObject, FlexType

from config import settings
from core.fields import (OBJ_TYPE_NONE, OBJ_TYPE_LOCATION, OBJ_TYPE_STREET, OBJ_TYPE_PHONE,
                         OBJ_TYPE_ADDRESS, OBJ_TYPE_SUBDIVISION, OBJ_TYPE_NOTICE,
                         OBJ_TYPE_POST_OFFICE, OBJ_TYPE_PHONE_OPERATOR)


class Command(BaseCommand):
    help = 'Заполнение основных таблиц дефолтными данными'

    def handle(self, *args, **kwargs):
        site_mode = Site.objects.get(pk=1)
        site_mode.name = settings.PROJECT_NAME
        site_mode.domain = settings.PROJECT_DOMAIN
        site_mode.save()
        self.stdout.write(
            self.style.SUCCESS(
                f'Проект: "{settings.PROJECT_NAME}" по адресу: "{settings.PROJECT_DOMAIN}"'))

        with transaction.atomic():
            Group.objects.all().delete()
            Group.objects.create(name='Обычный пользователь')
            Group.objects.create(name='Администратор')
            Group.objects.create(name='Администратор филиала')
            Group.objects.create(name='Администратор РУПС')
            Group.objects.create(name='Администратор УПС')

        _count = Group.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f"Групп пользователей: {_count}"))

        with transaction.atomic():
            Menu.objects.all().delete()
            Menu.objects.create(title='Главная', route='home', icon='fas fa-home')
            parent_menu = Menu.objects.create(title='Справочники',
                                              route='refs', icon='fas fa-th-list')
            Menu.objects.create(title='Страны', parent=parent_menu,
                                perm='references.view_country', route='countries',
                                icon='fas fa-globe')
            Menu.objects.create(title='Области', parent=parent_menu,
                                perm='references.view_region', route='regions',
                                icon='fas fa-map')
            Menu.objects.create(title='Районы', parent=parent_menu,
                                perm='references.view_district', route='districts',
                                icon='fas fa-map-location-dot')
            Menu.objects.create(title='Населенные пункты', parent=parent_menu,
                                perm='references.view_location', route='locations',
                                icon='fas fa-city')
            Menu.objects.create(title='Улицы', parent=parent_menu,
                                perm='references.view_street', route='streets',
                                icon='fas fa-road')
            Menu.objects.create(title='Здания', parent=parent_menu,
                                perm='references.view_building', route='buildings',
                                icon='fas fa-building')
            Menu.objects.create(title='Адреса', parent=parent_menu,
                                perm='references.view_address', route='addresses',
                                icon='fas fa-location-dot')
            Menu.objects.create(title='Персоны', parent=parent_menu,
                                perm='references.view_person', route='persons',
                                icon='fas fa-person')
            Menu.objects.create(title='Сотрудники', parent=parent_menu,
                                perm='references.view_employee', route='employees',
                                icon='fas fa-user-tie')
            Menu.objects.create(title='Подразделения', parent=parent_menu,
                                perm='references.view_subdivision', route='subdivisions',
                                icon='fas fa-house-laptop')
            Menu.objects.create(title='Почтовые коды', parent=parent_menu,
                                perm='references.view_postoffice', route='postoffices',
                                icon='fas fa-envelopes-bulk')
            Menu.objects.create(title='Номера телефонов', parent=parent_menu,
                                perm='references.view_phone', route='phones',
                                icon='fas fa-square-phone')

        _count = Menu.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f"Пунктов меню: {_count}"))

        with transaction.atomic():
            FlexObject.objects.update_or_create(id=OBJ_TYPE_NONE,
                                                defaults={'object_name': 'Не указано',
                                                          'object_app': 'none',
                                                          'object_model': 'none'})
            FlexObject.objects.update_or_create(id=OBJ_TYPE_LOCATION,
                                                defaults={'object_name': 'Населенные пункты',
                                                          'object_app': 'references',
                                                          'object_model': 'location'})
            FlexObject.objects.update_or_create(id=OBJ_TYPE_STREET,
                                                defaults={'object_name': 'Улицы',
                                                          'object_app': 'references',
                                                          'object_model': 'street'})
            FlexObject.objects.update_or_create(id=OBJ_TYPE_ADDRESS,
                                                defaults={'object_name': 'Адреса',
                                                          'object_app': 'references',
                                                          'object_model': 'address'})
            FlexObject.objects.update_or_create(id=OBJ_TYPE_PHONE,
                                                defaults={'object_name': 'Номера телефонов',
                                                          'object_app': 'references',
                                                          'object_model': 'phone'})
            FlexObject.objects.update_or_create(id=OBJ_TYPE_SUBDIVISION,
                                                defaults={'object_name': 'Подразделения',
                                                          'object_app': 'references',
                                                          'object_model': 'subdivision'})
            FlexObject.objects.update_or_create(id=OBJ_TYPE_NOTICE,
                                                defaults={'object_name': 'Извещения',
                                                          'object_app': 'references',
                                                          'object_model': 'notice'})
            FlexObject.objects.update_or_create(id=OBJ_TYPE_POST_OFFICE,
                                                defaults={'object_name': 'Извещения',
                                                          'object_app': 'references',
                                                          'object_model': 'postcode'})
            FlexObject.objects.update_or_create(id=OBJ_TYPE_PHONE_OPERATOR,
                                                defaults={'object_name': 'Операторы',
                                                          'object_app': 'references',
                                                          'object_model': 'phoneoperator'})

        _count = FlexObject.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f"Видов сущностей: {_count}"))

        with transaction.atomic():
            fo_pk = OBJ_TYPE_LOCATION
            FlexType.objects.filter(type_object_id=fo_pk).delete()
            FlexType.objects.create(type_code='1', type_name='нет', type_name_full='Не указано',
                                    type_object_id=fo_pk)
            FlexType.objects.create(type_code='2', type_name='г.', type_name_full='город',
                                    type_object_id=fo_pk)
            FlexType.objects.create(type_code='3', type_name='гп.',
                                    type_name_full='городской поселок',
                                    type_object_id=fo_pk)
            FlexType.objects.create(type_code='4', type_name='аг.', type_name_full='агрогородок',
                                    type_object_id=fo_pk)
            FlexType.objects.create(type_code='5', type_name='д.', type_name_full='деревня',
                                    type_object_id=fo_pk)
            FlexType.objects.create(type_code='6', type_name='п.', type_name_full='поселок',
                                    type_object_id=fo_pk)
            FlexType.objects.create(type_code='7', type_name='х.', type_name_full='хутор',
                                    type_object_id=fo_pk)
            FlexType.objects.create(type_code='8', type_name='кп.',
                                    type_name_full='курортный поселок',
                                    type_object_id=fo_pk)
            FlexType.objects.create(type_code='9', type_name='рп.',
                                    type_name_full='рабочий поселок',
                                    type_object_id=fo_pk)
            FlexType.objects.create(type_code='10', type_name='с.', type_name_full='сельсовет',
                                    type_object_id=fo_pk)
            FlexType.objects.create(type_code='11', type_name='снп.',
                                    type_name_full='сельский населенный пункт',
                                    type_object_id=fo_pk)

            fo_pk = OBJ_TYPE_STREET
            FlexType.objects.filter(type_object_id=fo_pk).delete()
            FlexType.objects.create(type_code='12', type_name='б-р', type_name_full='бульвар',
                                    type_object_id=fo_pk)
            FlexType.objects.create(type_code='13', type_name='вг',
                                    type_name_full='военный городок',
                                    type_object_id=fo_pk)
            FlexType.objects.create(type_code='14', type_name='вч', type_name_full='военная часть',
                                    type_object_id=fo_pk)
            FlexType.objects.create(type_code='15', type_name='въезд', type_name_full='въезд',
                                    type_object_id=fo_pk)
            FlexType.objects.create(type_code='16', type_name='кв-л', type_name_full='квартал',
                                    type_object_id=fo_pk)
            FlexType.objects.create(type_code='17', type_name='мкр-н', type_name_full='микрорайон',
                                    type_object_id=fo_pk)
            FlexType.objects.create(type_code='18', type_name='наб.', type_name_full='набережная',
                                    type_object_id=fo_pk)
            FlexType.objects.create(type_code='19', type_name='пер.', type_name_full='переулок',
                                    type_object_id=fo_pk)
            FlexType.objects.create(type_code='20', type_name='пл.', type_name_full='площадь',
                                    type_object_id=fo_pk)
            FlexType.objects.create(type_code='21', type_name='пос.', type_name_full='поселок',
                                    type_object_id=fo_pk)
            FlexType.objects.create(type_code='22', type_name='пр.', type_name_full='проспект',
                                    type_object_id=fo_pk)
            FlexType.objects.create(type_code='23', type_name='пр-д', type_name_full='проезд',
                                    type_object_id=fo_pk)
            FlexType.objects.create(type_code='24', type_name='ст.', type_name_full='станция',
                                    type_object_id=fo_pk)
            FlexType.objects.create(type_code='25', type_name='тер.', type_name_full='территория',
                                    type_object_id=fo_pk)
            FlexType.objects.create(type_code='26', type_name='тр.', type_name_full='тракт',
                                    type_object_id=fo_pk)
            FlexType.objects.create(type_code='27', type_name='туп.', type_name_full='тупик',
                                    type_object_id=fo_pk)
            FlexType.objects.create(type_code='28', type_name='ул.', type_name_full='улица',
                                    type_object_id=fo_pk)
            FlexType.objects.create(type_code='29', type_name='уроч.', type_name_full='урочище',
                                    type_object_id=fo_pk)
            FlexType.objects.create(type_code='30', type_name='шоссе', type_name_full='шоссе',
                                    type_object_id=fo_pk)

            fo_pk = OBJ_TYPE_ADDRESS
            FlexType.objects.filter(type_object_id=fo_pk).delete()
            FlexType.objects.create(type_code='0', type_name='Не указан', type_object_id=fo_pk)
            FlexType.objects.create(type_code='1', type_name='Доставочный', type_object_id=fo_pk)
            FlexType.objects.create(type_code='2', type_name='Домашний', type_object_id=fo_pk)
            FlexType.objects.create(type_code='3', type_name='Рабочий', type_object_id=fo_pk)

            fo_pk = OBJ_TYPE_PHONE
            FlexType.objects.filter(type_object_id=fo_pk).delete()
            FlexType.objects.create(type_code='0', type_name='Не указан', type_object_id=fo_pk)
            FlexType.objects.create(type_code='1', type_name='Мобильный', type_object_id=fo_pk)
            FlexType.objects.create(type_code='2', type_name='Домашний', type_object_id=fo_pk)
            FlexType.objects.create(type_code='3', type_name='Рабочий', type_object_id=fo_pk)

            fo_pk = OBJ_TYPE_SUBDIVISION
            FlexType.objects.filter(type_object_id=fo_pk).delete()
            FlexType.objects.create(type_code='0', type_name='Не указан', type_object_id=fo_pk)
            FlexType.objects.create(type_code='1', type_name='РУП', type_object_id=fo_pk,
                                    type_name_full='Республиканское унитарное предприятие')
            FlexType.objects.create(type_code='2', type_name='Филиал', type_object_id=fo_pk,
                                    type_name_full='Областной филиал')
            FlexType.objects.create(type_code='6', type_name='Цех', type_object_id=fo_pk,
                                    type_name_full='Цех')
            FlexType.objects.create(type_code='3', type_name='РУПС', type_object_id=fo_pk,
                                    type_name_full='Региональный узел почтовой связи')
            FlexType.objects.create(type_code='4', type_name='УПС', type_object_id=fo_pk,
                                    type_name_full='Участок почтовой связи')
            FlexType.objects.create(type_code='5', type_name='ОПС', type_object_id=fo_pk,
                                    type_name_full='Отделение почтовой связи')
            FlexType.objects.create(type_code='61', type_name='ПС', type_object_id=fo_pk,
                                    type_name_full='Пункт связи')
            FlexType.objects.create(type_code='62', type_name='ППС', type_object_id=fo_pk,
                                    type_name_full='Передвижной Пункт Связи')
            FlexType.objects.create(type_code='63', type_name='ПОПС', type_object_id=fo_pk,
                                    type_name_full='Передвижное Отделение Почтовой Связи')
            FlexType.objects.create(type_code='21', type_name='Отдел', type_object_id=fo_pk,
                                    type_name_full='', status=0)
            FlexType.objects.create(type_code='22', type_name='Сектор', type_object_id=fo_pk,
                                    type_name_full='', status=0)

            fo_pk = OBJ_TYPE_NOTICE
            FlexType.objects.filter(type_object_id=fo_pk).delete()
            FlexType.objects.create(type_code='0', type_name='Сквозная нумерация',
                                    type_object_id=fo_pk,
                                    type_value='0')
            FlexType.objects.create(type_code='1', type_name='Каждый месяц', type_object_id=fo_pk,
                                    type_value='1')
            FlexType.objects.create(type_code='2', type_name='Каждый квартал', type_object_id=fo_pk,
                                    type_value='3')
            FlexType.objects.create(type_code='3', type_name='Каждое полугодие',
                                    type_object_id=fo_pk,
                                    type_value='6')
            FlexType.objects.create(type_code='4', type_name='Каждый год', type_object_id=fo_pk,
                                    type_value='12')

            fo_pk = OBJ_TYPE_POST_OFFICE
            FlexType.objects.filter(type_object_id=fo_pk).delete()
            FlexType.objects.create(type_code='0', type_name='Не указано',
                                    type_object_id=fo_pk)
            FlexType.objects.create(type_code='19', type_name='Сельское', type_object_id=fo_pk)
            FlexType.objects.create(type_code='20', type_name='Городское', type_object_id=fo_pk)
            FlexType.objects.create(type_code='21', type_name='Передвижное', type_object_id=fo_pk)
            FlexType.objects.create(type_code='22', type_name='Пункт связи', type_object_id=fo_pk)
            FlexType.objects.create(type_code='23', type_name='Прочие', type_object_id=fo_pk)
            FlexType.objects.create(type_code='24', type_name='Участок', type_object_id=fo_pk)
            FlexType.objects.create(type_code='25', type_name='Цех', type_object_id=fo_pk)
            FlexType.objects.create(type_code='26', type_name='РУПС', type_object_id=fo_pk)
            FlexType.objects.create(type_code='27', type_name='Область (для сортировки)',
                                    type_object_id=fo_pk)
            FlexType.objects.create(type_code='204', type_name='Администрация',
                                    type_object_id=fo_pk)
            FlexType.objects.create(type_code='215', type_name='Союзпечать', type_object_id=fo_pk)
            FlexType.objects.create(type_code='216', type_name='Филиал', type_object_id=fo_pk)
            FlexType.objects.create(type_code='283', type_name='Служба', type_object_id=fo_pk)
            FlexType.objects.create(type_code='287', type_name='Мотодоставка', type_object_id=fo_pk)

            fo_pk = OBJ_TYPE_PHONE_OPERATOR
            FlexType.objects.filter(type_object_id=fo_pk).delete()
            FlexType.objects.create(type_code='0', type_name='Не указано',
                                    type_object_id=fo_pk)
            FlexType.objects.create(type_code='1', type_name='Виртуальный',
                                    type_object_id=fo_pk)
            FlexType.objects.create(type_code='2', type_name='Внутренний',
                                    type_object_id=fo_pk)
            FlexType.objects.create(type_code='3', type_name='БТК',
                                    type_object_id=fo_pk)
            FlexType.objects.create(type_code='4', type_name='A1', type_value='mobile',
                                    type_object_id=fo_pk)
            FlexType.objects.create(type_code='5', type_name='MTS', type_value='mobile',
                                    type_object_id=fo_pk)
            FlexType.objects.create(type_code='6', type_name='life :)', type_value='mobile',
                                    type_object_id=fo_pk)

        _count = FlexType.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f"Типов сущностей: {_count}"))

        with transaction.atomic():
            Module.objects.create(name='Доставка ПО', desc='Создание и контроль доставки ПО',
                                  route='mailings', perm='modules.view_mailing',
                                  icon='fas fa-envelope')

        _count = Module.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f"Модулей: {_count}"))
