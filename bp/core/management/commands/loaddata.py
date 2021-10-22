from collections import namedtuple

from django.core.management import BaseCommand
from django.db import connections, transaction

from apps.references.models.base import FlexType
from apps.references.models.street import Street
from core.fields import OBJ_TYPE_STREET


class Command(BaseCommand):
    help = 'Импорт справочных данных'

    def namedtuplefetchall(self, cursor):
        "Return all rows from a cursor as a namedtuple"
        desc = cursor.description
        nt_result = namedtuple('Result', [col[0] for col in desc])
        return [nt_result(*row) for row in cursor.fetchall()]

    def get_custom_data(self, sql):
        with connections['ref'].cursor() as cursor:
            cursor.execute(sql)
            results = self.namedtuplefetchall(cursor)
        return results

    def handle(self, *args, **kwargs):
        sql_street = 'SELECT s.ID_REC, s.ID_TYPE, s.NAME_STR, s.STR_FULL FROM STREETS s WHERE s.STATUS = 1 ORDER BY s.ID_REC'
        mt = {res['type_code']: res['id'] for res in FlexType.objects.filter(type_object_id=OBJ_TYPE_STREET).values('type_code', 'id')}
        ress = self.get_custom_data(sql_street)
        count = 0
        with transaction.atomic():
            for res in ress:
                Street.objects.create(code=str(res.ID_REC), model_type_id=mt[str(res.ID_TYPE)],
                                      name_str=res.NAME_STR, name_str_full=res.STR_FULL)
                count += 1
                if count % 100 == 0:
                    print(count)
