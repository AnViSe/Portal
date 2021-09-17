from django.core.management.base import BaseCommand

from home.models import Menu
from references.models import Country, Region


class Command(BaseCommand):
    help = 'Заполнение таблиц дефолтными данными'

    def handle(self, *args, **options):
        Menu.objects.all().delete()
        Menu.objects.create(name='Главное меню', route='home', icon='fas fa-home', sort=100)
        parent_menu = Menu.objects.create(name='Справочники',
                                          route='refs', icon='fas fa-th-list', sort=800)
        Menu.objects.create(name='Сотрудники', parent=parent_menu, perm='references.view_employee',
                            route='employees', icon='far fa-address-book')
        Menu.objects.create(name='Страны', parent=parent_menu, perm='references.view_country',
                            route='countries')
        Menu.objects.create(name='Области', parent=parent_menu, perm='references.view_region',
                            route='regions')

        _count = Menu.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f"Пунктов меню: {_count}"))

        Country.objects.all().delete()
        Country.objects.create(code=112, name='Беларусь', alpha2='BY', alpha3='BLR')
        Country.objects.create(code=643, name='Россия', alpha2='RU', alpha3='RUS')

        _count = Country.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f"Стран: {_count}"))

        blr = Country.objects.get(code=112)
        Region.objects.all().delete()
        Region.objects.create(country=blr, code=100, name='Брестская')
        Region.objects.create(country=blr, code=200, name='Витебская')
        Region.objects.create(country=blr, code=300, name='Гомельская')
        Region.objects.create(country=blr, code=400, name='Гродненская')
        Region.objects.create(country=blr, code=500, name='Минская')
        Region.objects.create(country=blr, code=600, name='Могилёвская')
        Region.objects.create(country=blr, code=700, name='г. Минск')

        _count = Region.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f"Областей: {_count}"))

    def add_arguments(self, parser):
        pass
