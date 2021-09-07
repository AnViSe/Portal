from django.core.management.base import BaseCommand
from faker import Faker

from config import settings
from references.models import Employee


class Command(BaseCommand):
    help = 'Заполнение таблиц тестовыми данными'

    def handle(self, *args, **options):
        count = options['count']
        faker = Faker([settings.LANGUAGE_CODE])
        for _ in range(count):
            l = faker.last_name_male()
            m = faker.middle_name_male()
            f = faker.first_name_male()
            Employee.objects.create(lastname=l, middlename=m, firstname=f)
        count_employee = Employee.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f"Всего сотрудников: {count_employee}"))

    def add_arguments(self, parser):
        parser.add_argument(
            '-c',
            '--count',
            action='store',
            type=int,
            default=10,
            help='Количество добавляемых записей. По умолчанию: 10'
        )
