from django.core.management.base import BaseCommand
from faker import Faker

from config import settings
from references.models import Person


class Command(BaseCommand):
    help = 'Заполнение таблиц тестовыми данными'

    def handle(self, *args, **options):
        count = options['count']
        faker = Faker([settings.LANGUAGE_CODE])
        for i in range(count):
            if i % 2 == 0:
                l = faker.last_name_male()
                m = faker.middle_name_male()
                f = faker.first_name_male()
                s = 1
            else:
                l = faker.last_name_female()
                m = faker.middle_name_female()
                f = faker.first_name_female()
                s = 2

            # Employee.objects.create(lastname=l, middlename=m, firstname=f)
            Person.objects.create(lastname=l, middlename=m, firstname=f, sex=s)

        count_person = Person.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f"Всего персон: {count_person}"))

    def add_arguments(self, parser):
        parser.add_argument(
            '-c',
            '--count',
            action='store',
            type=int,
            default=10,
            help='Количество добавляемых записей. По умолчанию: 10'
        )
