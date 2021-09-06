from django.core.management.base import BaseCommand

from ...models import Menu


class Command(BaseCommand):
    help = 'Заполнение таблиц дефолтными данными'

    def handle(self, *args, **options):
        Menu.objects.create(name='Главное меню', route='home', icon='fas fa-home', sort=100)
        parent_menu = Menu.objects.create(name='Справочники',
                                          route='refs', icon='fas fa-th-list', sort=800)
        Menu.objects.create(name='Сотрудники', parent=parent_menu,
                            route='employees', icon='far fa-address-book')

        count_menu = Menu.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f"Пунктов меню: {count_menu}"))

    def add_arguments(self, parser):
        pass
