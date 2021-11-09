from optparse import make_option

from django.core.management.base import BaseCommand
from django.db import transaction
from faker import Faker

from apps.references.models.phone import Phone
from apps.references.models.postoffice import PostOffice
from apps.references.models.subdivision import Subdivision
from config import settings
from apps.references.models.person import Person
from apps.references.models.employee import Employee


class Command(BaseCommand):
    help = 'Заполнение таблиц тестовыми данными'

    def add_arguments(self, parser):
        parser.add_argument('model', type=str, help='Имя модели')
        parser.add_argument('-c', '--count', action='store', type=int, default=10, help='Количество записей')

    def append_persons(self, count):
        faker = Faker([settings.LANGUAGE_CODE])
        with transaction.atomic():
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
                b = faker.date_of_birth()

                Person.objects.create(last_name=l, middle_name=m, first_name=f, gender=s, birth_date=b)

        count = Person.objects.all().count()
        return count

    def append_employees(self, count):
        faker = Faker([settings.LANGUAGE_CODE])
        sb_max = Subdivision.objects.count()
        with transaction.atomic():
            for p in Person.objects.all():
                Employee.objects.create(tab_num=faker.unique.random_int(10, 99999), person=p,
                                        subdivision_id=faker.unique.random_int(1, sb_max - 1))
        count = Employee.objects.all().count()
        return count

    def append_phones(self, count):
        faker = Faker([settings.LANGUAGE_CODE])
        phones = set()
        for i in range(count):
            fn = faker.unique.msisdn()
            Phone.objects.create(phone_number=fn)
        count = Phone.objects.all().count()
        return count

    def append_postoffice(self, count):
        PostOffice.objects.create(code='220000', zipcode=220000, name_post='Белпочта')
        PostOffice.objects.create(code='230000', zipcode=230000, name_post='Гродно')

        count = PostOffice.objects.all().count()
        return count

    def handle(self, *args, **kwargs):
        model_name = kwargs['model']
        record_count = kwargs['count']

        if model_name == 'person':
            result = self.append_persons(record_count)
            self.stdout.write(self.style.SUCCESS(f"Всего персон: {result}"))

        if model_name == 'employee':
            result = self.append_employees(record_count)
            self.stdout.write(self.style.SUCCESS(f"Всего сотрудников: {result}"))

        if model_name == 'phone':
            result = self.append_phones(record_count)
            self.stdout.write(self.style.SUCCESS(f"Всего телефонов: {result}"))

        if model_name == 'postoffice':
            result = self.append_postoffice(record_count)
            self.stdout.write(self.style.SUCCESS(f"Всего телефонов: {result}"))
