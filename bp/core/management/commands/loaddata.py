from collections import namedtuple

from django.core.management import BaseCommand
from django.db import connections, transaction

from apps.references.models.address import Address
from apps.references.models.base import FlexType
from apps.references.models.building import Building
from apps.references.models.country import Country
from apps.references.models.district import District
from apps.references.models.location import Location
from apps.references.models.region import Region
from apps.references.models.street import Street
from apps.references.models.subdivision import Subdivision
from core.fields import OBJ_TYPE_STREET, OBJ_TYPE_LOCATION, OBJ_TYPE_SUBDIVISION, OBJ_TYPE_GEN_IZV


class Command(BaseCommand):
    help = 'Импорт справочных данных'

    def named_tuple_fetch_all(self, cursor):
        """Return all rows from a cursor as a namedtuple"""
        desc = cursor.description
        nt_result = namedtuple('Result', [col[0] for col in desc])
        return [nt_result(*row) for row in cursor.fetchall()]

    def get_custom_data(self, db, sql):
        with connections[db].cursor() as cursor:
            cursor.execute(sql)
            results = self.named_tuple_fetch_all(cursor)
        return results

    def handle(self, *args, **kwargs):

        print('Загрузка справочника стран...')
        sql = 'SELECT c.ID_REC, c.NAME_CNT, c.ALPHA2, c.ALPHA3 FROM COUNTRIES c WHERE c.STATUS = 1 AND c.ID_REC > 0 ORDER BY c.ID_REC'
        results = self.get_custom_data('ref', sql)
        count = 0
        with transaction.atomic():
            for res in results:
                Country.objects.create(code=str(res.ID_REC), name_cnt=res.NAME_CNT, alpha2=res.ALPHA2,
                                       alpha3=res.ALPHA3)
                count += 1
                if count % 100 == 0:
                    print(count)
        print(f'Всего загружно: {count}')

        print('Загрузка справочника областей...')
        sql = 'SELECT r.ID_REC, r.ID_CNT, r.NAME_RGN FROM REGIONS r WHERE r.STATUS = 1 AND r.ID_REC > 0 ORDER BY r.ID_REC'
        cnt = {res['code']: res['id'] for res in Country.objects.values('code', 'id')}
        results = self.get_custom_data('ref', sql)
        count = 0
        with transaction.atomic():
            for res in results:
                Region.objects.create(code=str(res.ID_REC), name_rgn=res.NAME_RGN, country_id=cnt[str(res.ID_CNT)])
                count += 1
                if count % 100 == 0:
                    print(count)
        print(f'Всего загружно: {count}')

        print('Загрузка справочника районов...')
        sql = 'SELECT d.ID_REC, d.ID_RGN, d.NAME_DST FROM DISTRICTS d WHERE d.STATUS = 1 AND d.ID_REC > 0 ORDER BY d.ID_REC'
        rgn = {res['code']: res['id'] for res in Region.objects.values('code', 'id')}
        results = self.get_custom_data('ref', sql)
        count = 0
        with transaction.atomic():
            for res in results:
                District.objects.create(code=str(res.ID_REC), name_dst=res.NAME_DST, region_id=rgn[str(res.ID_RGN)])
                count += 1
                if count % 100 == 0:
                    print(count)
        print(f'Всего загружно: {count}')

        print('Загрузка справочника населенных пунктов...')
        sql = 'SELECT l.ID_REC, l.ID_DST, l.ID_TYPE, l.SOATO, l.NAME_LOC, l.LOC_FULL FROM LOCATIONS l WHERE l.STATUS = 1 AND l.ID_REC < 23902 ORDER BY l.ID_REC'
        mt = {res['type_code']: res['id'] for res in
              FlexType.objects.filter(type_object_id=OBJ_TYPE_LOCATION).values('type_code', 'id')}
        dst = {res['code']: res['id'] for res in District.objects.values('code', 'id')}
        results = self.get_custom_data('ref', sql)
        count = 0
        with transaction.atomic():
            for res in results:
                Location.objects.create(code=str(res.ID_REC), soato=res.SOATO, district_id=dst[str(res.ID_DST)],
                                        name_lct=res.NAME_LOC, name_lct_full=res.LOC_FULL,
                                        model_type_id=mt[str(res.ID_TYPE)])
                count += 1
                if count % 100 == 0:
                    print(count)
        print(f'Всего загружно: {count}')

        print('Загрузка справочника улиц...')
        sql = 'SELECT s.ID_REC, s.ID_TYPE, s.NAME_STR, s.STR_FULL FROM STREETS s WHERE s.STATUS = 1 ORDER BY s.ID_REC'
        mt = {res['type_code']: res['id'] for res in
              FlexType.objects.filter(type_object_id=OBJ_TYPE_STREET).values('type_code', 'id')}
        results = self.get_custom_data('ref', sql)
        count = 0
        with transaction.atomic():
            for res in results:
                Street.objects.create(code=str(res.ID_REC), model_type_id=mt[str(res.ID_TYPE)],
                                      name_str=res.NAME_STR, name_str_full=res.STR_FULL)
                count += 1
                if count % 100 == 0:
                    print(count)
        print(f'Всего загружно: {count}')

        print('Загрузка справочника зданий...')
        sql = 'SELECT b.ID_REC, b.ID_LOC, b.ID_STR, b.HOUSE FROM BUILDINGS b  INNER JOIN LOCATIONS l ON l.ID_REC = b.ID_LOC AND l.STATUS = 1 INNER JOIN STREETS s ON s.ID_REC = b.ID_STR AND s.STATUS = 1 WHERE b.STATUS = 1 ORDER BY b.ID_REC'
        d_lct = {res['code']: res['id'] for res in Location.objects.values('code', 'id')}
        d_str = {res['code']: res['id'] for res in Street.objects.values('code', 'id')}
        results = self.get_custom_data('ref', sql)
        count = 0
        with transaction.atomic():
            for res in results[:5001]:
                Building.objects.create(code=str(res.ID_REC), name_bld=res.HOUSE,
                                        location_id=d_lct[str(res.ID_LOC)], street_id=d_str[str(res.ID_STR)])
                count += 1
                if count % 100 == 0:
                    print(count)
        with transaction.atomic():
            for res in results[5001:10001]:
                Building.objects.create(code=str(res.ID_REC), name_bld=res.HOUSE,
                                        location_id=d_lct[str(res.ID_LOC)], street_id=d_str[str(res.ID_STR)])
                count += 1
                if count % 100 == 0:
                    print(count)
        with transaction.atomic():
            for res in results[10001:15001]:
                Building.objects.create(code=str(res.ID_REC), name_bld=res.HOUSE,
                                        location_id=d_lct[str(res.ID_LOC)], street_id=d_str[str(res.ID_STR)])
                count += 1
                if count % 100 == 0:
                    print(count)
        with transaction.atomic():
            for res in results[15001:]:
                Building.objects.create(code=str(res.ID_REC), name_bld=res.HOUSE,
                                        location_id=d_lct[str(res.ID_LOC)], street_id=d_str[str(res.ID_STR)])
                count += 1
                if count % 100 == 0:
                    print(count)
        print(f'Всего загружно: {count}')

        print('Загрузка справочника адресов...')
        sql = """SELECT a.ID_REC, a.ID_BUILDING, a.ROOM
                   FROM ADDRESSES a
                  INNER JOIN BUILDINGS b ON b.ID_REC = a.ID_BUILDING AND b.STATUS = 1
                  INNER JOIN LOCATIONS l ON l.ID_REC = b.ID_LOC AND l.STATUS = 1
                  INNER JOIN STREETS s ON s.ID_REC = b.ID_STR AND s.STATUS = 1
                  WHERE a.STATUS = 1 ORDER BY a.ID_REC"""
        d_bld = {res['code']: res['id'] for res in Building.objects.values('code', 'id')}
        results = self.get_custom_data('ref', sql)
        count = 0
        with transaction.atomic():
            for res in results[:5001]:
                Address.objects.create(code=str(res.ID_REC), name_adds=res.ROOM,
                                       building_id=d_bld[str(res.ID_BUILDING)])
                count += 1
                if count % 100 == 0:
                    print(count)
        with transaction.atomic():
            for res in results[5001:10001]:
                Address.objects.create(code=str(res.ID_REC), name_adds=res.ROOM,
                                       building_id=d_bld[str(res.ID_BUILDING)])
                count += 1
                if count % 100 == 0:
                    print(count)
        with transaction.atomic():
            for res in results[10001:15001]:
                Address.objects.create(code=str(res.ID_REC), name_adds=res.ROOM,
                                       building_id=d_bld[str(res.ID_BUILDING)])
                count += 1
                if count % 100 == 0:
                    print(count)
        with transaction.atomic():
            for res in results[15001:20001]:
                Address.objects.create(code=str(res.ID_REC), name_adds=res.ROOM,
                                       building_id=d_bld[str(res.ID_BUILDING)])
                count += 1
                if count % 100 == 0:
                    print(count)
        with transaction.atomic():
            for res in results[20001:]:
                Address.objects.create(code=str(res.ID_REC), name_adds=res.ROOM,
                                       building_id=d_bld[str(res.ID_BUILDING)])
                count += 1
                if count % 100 == 0:
                    print(count)
        print(f'Всего загружно: {count}')


        print('Загрузка справочника подразделений...')
        sql = """ SELECT s.ID_REC, NVL(s.ID_PARENT, -1) AS ID_PARENT, S.NAME_SD_SHORT, S.NAME_SD_FULL, 
                         NVL(S.ID_SD_TYPE,0) AS ID_SD_TYPE, NVL(S.ID_LOCATION, 0) AS ID_LOCATION, 
                         NVL(S.ID_GIT,0) AS ID_GIT, S.STATUS
                   FROM NSI_SUBDIVISION s
                CONNECT BY (s.ID_PARENT = PRIOR s.ID_REC)
                  START WITH s.ID_REC = 0
                  ORDER SIBLINGS BY s.ID_SD_TYPE, s.NAME_SD_SHORT"""
        mt_sd = {res['type_code']: res['id'] for res in FlexType.objects.filter(type_object_id=OBJ_TYPE_SUBDIVISION).values('type_code', 'id')}
        mt_gi = {res['type_code']: res['id'] for res in FlexType.objects.filter(type_object_id=OBJ_TYPE_GEN_IZV).values('type_code', 'id')}

        d_lct = {res['code']: res['id'] for res in Location.objects.values('code', 'id')}
        d_sd = {'-1': None}

        results = self.get_custom_data('nsi', sql)
        count = 0

        with transaction.atomic():
            for res in results:
                cur_sd = Subdivision.objects.create(code=str(res.ID_REC), parent_id=d_sd[str(res.ID_PARENT)],
                                                    name_sd=res.NAME_SD_SHORT, name_sd_full=res.NAME_SD_FULL,
                                                    model_type_id=mt_sd[str(res.ID_SD_TYPE)],
                                                    gi_type_id=mt_gi[str(res.ID_GIT)],
                                                    # location_id=d_lct[str(res.ID_LOCATION)],
                                                    status=res.STATUS)
                d_sd[str(res.ID_REC)] = cur_sd.pk
                count += 1
                if count % 100 == 0:
                    print(count)
        print(f'Всего загружно: {count}')


