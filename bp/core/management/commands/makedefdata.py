from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand

from apps.home.models import Menu
from apps.references.models.country import Country
from apps.references.models.region import Region
from apps.references.models.subdivision import Subdivision
from config import settings


class Command(BaseCommand):
    help = 'Заполнение таблиц дефолтными данными'

    def handle(self, *args, **kwargs):
        site_mode = Site.objects.get(pk=1)
        site_mode.name = settings.PROJECT_NAME
        site_mode.domain = settings.PROJECT_DOMAIN
        site_mode.save()
        self.stdout.write(
            self.style.SUCCESS(
                f'Проект: "{settings.PROJECT_NAME}" по адресу: "{settings.PROJECT_DOMAIN}"'))

        Menu.objects.all().delete()
        Menu.objects.create(name='Главная', route='home', icon='fas fa-home', sort=100)
        parent_menu = Menu.objects.create(name='Справочники',
                                          route='refs', icon='fas fa-th-list', sort=800)

        Menu.objects.create(name='Страны', parent=parent_menu,
                            perm='references.view_country', route='countries',
                            icon='fas fa-globe')
        Menu.objects.create(name='Области', parent=parent_menu,
                            perm='references.view_region', route='regions',
                            icon='fas fa-map')
        Menu.objects.create(name='Районы', parent=parent_menu,
                            perm='references.view_district', route='districts',
                            icon='fas fa-map-location-dot',
                            status=0)
        Menu.objects.create(name='Населенные пункты', parent=parent_menu,
                            perm='references.view_location', route='locations',
                            icon='fas fa-city',
                            status=0)
        Menu.objects.create(name='Улицы', parent=parent_menu,
                            perm='references.view_street', route='streets',
                            icon='fas fa-road',
                            status=0)
        Menu.objects.create(name='Здания', parent=parent_menu,
                            perm='references.view_building', route='buildings',
                            icon='fas fa-building',
                            status=0)

        Menu.objects.create(name='Персоны', parent=parent_menu,
                            perm='references.view_person', route='persons',
                            icon='fas fa-person')
        Menu.objects.create(name='Сотрудники', parent=parent_menu,
                            perm='references.view_employee', route='employees',
                            icon='fas fa-user-tie')

        Menu.objects.create(name='Подразделения', parent=parent_menu,
                            perm='references.view_subdivision', route='subdivisions',
                            icon='fas fa-house-laptop')

        _count = Menu.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f"Пунктов меню: {_count}"))

        # Country.objects.all().delete()
        # Country.objects.create(code='112', name='Беларусь', alpha2='BY', alpha3='BLR')
        # Country.objects.create(code='643', name='Россия', alpha2='RU', alpha3='RUS')

        # _count = Country.objects.all().count()
        # self.stdout.write(self.style.SUCCESS(f"Стран: {_count}"))

        # blr = Country.objects.get(code='112')
        # Region.objects.all().delete()
        # Region.objects.create(country=blr, code='100', name='Брестская')
        # Region.objects.create(country=blr, code='200', name='Витебская')
        # Region.objects.create(country=blr, code='300', name='Гомельская')
        # Region.objects.create(country=blr, code='400', name='Гродненская')
        # Region.objects.create(country=blr, code='500', name='Минская')
        # Region.objects.create(country=blr, code='600', name='Могилёвская')
        # Region.objects.create(country=blr, code='700', name='г. Минск')

        # _count = Region.objects.all().count()
        # self.stdout.write(self.style.SUCCESS(f"Областей: {_count}"))

        Subdivision.objects.all().delete()
        belpost = Subdivision.objects.create(name='Белпочта')
        Subdivision.objects.create(parent=belpost, name='Брестский филиал')
        Subdivision.objects.create(parent=belpost, name='Витебский филиал')
        Subdivision.objects.create(parent=belpost, name='Гомельский филиал')
        Subdivision.objects.create(parent=belpost, name='Гродненский филиал')
        Subdivision.objects.create(parent=belpost, name='Минский филиал')
        Subdivision.objects.create(parent=belpost, name='Могилевский филиал')
        Subdivision.objects.create(parent=belpost, name='Минск - город')

        _count = Subdivision.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f"Подразделений: {_count}"))
