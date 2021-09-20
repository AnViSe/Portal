from optparse import make_option

from django.core.management.base import BaseCommand
from faker import Faker

from config import settings
from apps.references.models import Person


class Command(BaseCommand):
    help = 'Заполнение таблиц тестовыми данными'

    def add_arguments(self, parser):
        parser.add_argument('model', type=str, help='Имя модели')
        parser.add_argument('-c', '--count', action='store', type=int, default=10, help='Количество записей')

    def append_persons(self, count):
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

            Person.objects.create(lastname=l, middlename=m, firstname=f, sex=s)

        count = Person.objects.all().count()
        return count

    def handle(self, *args, **kwargs):
        model_name = kwargs['model']
        record_count = kwargs['count']

        if model_name == 'person':
            result = self.append_persons(record_count)
            self.stdout.write(self.style.SUCCESS(f"Всего персон: {result}"))
