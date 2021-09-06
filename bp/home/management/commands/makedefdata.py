from django.core.management.base import BaseCommand

from references.models import Country
from ...models import Menu


class Command(BaseCommand):
    help = 'Заполнение таблиц дефолтными данными'

    def handle(self, *args, **options):
        Menu.objects.create(name='Главное меню', route='home', icon='fas fa-home', sort=100)
        parent_menu = Menu.objects.create(name='Справочники',
                                          route='refs', icon='fas fa-th-list', sort=800)
        Menu.objects.create(name='Сотрудники', parent=parent_menu,
                            route='employees', icon='far fa-address-book')

        _count = Menu.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f"Пунктов меню: {_count}"))

        Country.objects.create(code=112, name='Беларусь', alpha2='BY', alpha3='BLR')
        Country.objects.create(code=643, name='Россия', alpha2='RU', alpha3='RUS')

        _count = Country.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f"Стран: {_count}"))

    def add_arguments(self, parser):
        pass
