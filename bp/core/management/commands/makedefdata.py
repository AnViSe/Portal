from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand

from apps.home.models import Menu
from apps.references.models.country import Country
from apps.references.models.district import District
from apps.references.models.location import Location
from apps.references.models.region import Region

from config import settings


class Command(BaseCommand):
    help = 'Заполнение таблиц дефолтными данными'

    def handle(self, *args, **kwargs):
        # site_mode = Site.objects.get(pk=1)
        # site_mode.name = settings.PROJECT_NAME
        # site_mode.domain = settings.PROJECT_DOMAIN
        # site_mode.save()
        # self.stdout.write(
        #     self.style.SUCCESS(
        #         f'Проект: "{settings.PROJECT_NAME}" по адресу: "{settings.PROJECT_DOMAIN}"'))
        #
        # Menu.objects.all().delete()
        # Menu.objects.create(name='Главная', route='home', icon='fas fa-home')
        # parent_menu = Menu.objects.create(name='Справочники',
        #                                   route='refs', icon='fas fa-th-list')
        # Menu.objects.create(name='Страны', parent=parent_menu,
        #                     perm='references.view_country', route='countries',
        #                     icon='fas fa-globe')
        # Menu.objects.create(name='Области', parent=parent_menu,
        #                     perm='references.view_region', route='regions',
        #                     icon='fas fa-map')
        # Menu.objects.create(name='Районы', parent=parent_menu,
        #                     perm='references.view_district', route='districts',
        #                     icon='fas fa-map-location-dot')
        # Menu.objects.create(name='Населенные пункты', parent=parent_menu,
        #                     perm='references.view_location', route='locations',
        #                     icon='fas fa-city')
        # Menu.objects.create(name='Улицы', parent=parent_menu,
        #                     perm='references.view_street', route='streets',
        #                     icon='fas fa-road',
        #                     status=0)
        # Menu.objects.create(name='Здания', parent=parent_menu,
        #                     perm='references.view_building', route='buildings',
        #                     icon='fas fa-building',
        #                     status=0)
        #
        # Menu.objects.create(name='Персоны', parent=parent_menu,
        #                     perm='references.view_person', route='persons',
        #                     icon='fas fa-person')
        # Menu.objects.create(name='Сотрудники', parent=parent_menu,
        #                     perm='references.view_employee', route='employees',
        #                     icon='fas fa-user-tie')
        #
        # Menu.objects.create(name='Подразделения', parent=parent_menu,
        #                     perm='references.view_subdivision', route='subdivisions',
        #                     icon='fas fa-house-laptop')

        # _count = Menu.objects.all().count()
        # self.stdout.write(self.style.SUCCESS(f"Пунктов меню: {_count}"))

        Country.objects.all().delete()
        Country.objects.create(code='112', name_cnt='Беларусь', alpha2='BY', alpha3='BLR')
        Country.objects.create(code='643', name_cnt='Россия', alpha2='RU', alpha3='RUS')

        _count = Country.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f"Стран: {_count}"))

        blr = Country.objects.get(code='112')
        Region.objects.all().delete()
        Region.objects.create(country=blr, code='100', name_rgn='Брестская')
        Region.objects.create(country=blr, code='200', name_rgn='Витебская')
        Region.objects.create(country=blr, code='300', name_rgn='Гомельская')
        Region.objects.create(country=blr, code='400', name_rgn='Гродненская')
        Region.objects.create(country=blr, code='500', name_rgn='Минская')
        Region.objects.create(country=blr, code='600', name_rgn='Могилёвская')
        Region.objects.create(country=blr, code='700', name_rgn='г. Минск')

        _count = Region.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f"Областей: {_count}"))

        District.objects.all().delete()
        rgn100 = Region.objects.get(code='100')
        District.objects.create(code='101', region=rgn100, name_dst='г. Брест')
        District.objects.create(code='102', region=rgn100, name_dst='Барановичский')
        District.objects.create(code='103', region=rgn100, name_dst='Березовский')
        District.objects.create(code='104', region=rgn100, name_dst='Брестский')
        District.objects.create(code='105', region=rgn100, name_dst='Ганцевичский')
        District.objects.create(code='106', region=rgn100, name_dst='Дрогичинский')
        District.objects.create(code='107', region=rgn100, name_dst='Жабинковский')
        District.objects.create(code='108', region=rgn100, name_dst='Ивановский')
        District.objects.create(code='109', region=rgn100, name_dst='Ивацевичский')
        District.objects.create(code='110', region=rgn100, name_dst='Каменецкий')
        District.objects.create(code='111', region=rgn100, name_dst='Кобринский')
        District.objects.create(code='112', region=rgn100, name_dst='Лунинецкий')
        District.objects.create(code='113', region=rgn100, name_dst='Ляховичский')
        District.objects.create(code='114', region=rgn100, name_dst='Малоритский')
        District.objects.create(code='115', region=rgn100, name_dst='Пинский')
        District.objects.create(code='116', region=rgn100, name_dst='Пружанский')
        District.objects.create(code='117', region=rgn100, name_dst='Столинский')

        rgn200 = Region.objects.get(code='200')
        District.objects.create(code='201', region=rgn200, name_dst='г. Витебск')
        District.objects.create(code='202', region=rgn200, name_dst='Бешенковичский')
        District.objects.create(code='203', region=rgn200, name_dst='Браславский')
        District.objects.create(code='204', region=rgn200, name_dst='Верхнедвинский')
        District.objects.create(code='205', region=rgn200, name_dst='Витебский')
        District.objects.create(code='206', region=rgn200, name_dst='г. Новополоцк')
        District.objects.create(code='207', region=rgn200, name_dst='Глубокский')
        District.objects.create(code='208', region=rgn200, name_dst='Городокский')
        District.objects.create(code='209', region=rgn200, name_dst='Докшицкий')
        District.objects.create(code='210', region=rgn200, name_dst='Дубровенский')
        District.objects.create(code='211', region=rgn200, name_dst='Лепельский')
        District.objects.create(code='212', region=rgn200, name_dst='Лиозненский')
        District.objects.create(code='213', region=rgn200, name_dst='Миорский')
        District.objects.create(code='214', region=rgn200, name_dst='Оршанский')
        District.objects.create(code='215', region=rgn200, name_dst='Полоцкий')
        District.objects.create(code='216', region=rgn200, name_dst='Поставский')
        District.objects.create(code='217', region=rgn200, name_dst='Россонский')
        District.objects.create(code='218', region=rgn200, name_dst='Сенненский')
        District.objects.create(code='219', region=rgn200, name_dst='Толочинский')
        District.objects.create(code='220', region=rgn200, name_dst='Ушачский')
        District.objects.create(code='221', region=rgn200, name_dst='Чашникский')
        District.objects.create(code='222', region=rgn200, name_dst='Шарковщинский')
        District.objects.create(code='223', region=rgn200, name_dst='Шумилинский')

        rgn300 = Region.objects.get(code='300')
        District.objects.create(code='301', region=rgn300, name_dst='г. Гомель')
        District.objects.create(code='302', region=rgn300, name_dst='Брагинский')
        District.objects.create(code='303', region=rgn300, name_dst='Буда-Кошелевский')
        District.objects.create(code='304', region=rgn300, name_dst='Ветковский')
        District.objects.create(code='305', region=rgn300, name_dst='Гомельский')
        District.objects.create(code='306', region=rgn300, name_dst='Добрушский')
        District.objects.create(code='307', region=rgn300, name_dst='Ельский')
        District.objects.create(code='308', region=rgn300, name_dst='Житковичский')
        District.objects.create(code='309', region=rgn300, name_dst='Жлобинский')
        District.objects.create(code='310', region=rgn300, name_dst='Калинковичский')
        District.objects.create(code='311', region=rgn300, name_dst='Кормянский')
        District.objects.create(code='312', region=rgn300, name_dst='Лельчицкий')
        District.objects.create(code='313', region=rgn300, name_dst='Лоевский')
        District.objects.create(code='314', region=rgn300, name_dst='Мозырский')
        District.objects.create(code='315', region=rgn300, name_dst='Наровлянский')
        District.objects.create(code='316', region=rgn300, name_dst='Октябрьский')
        District.objects.create(code='317', region=rgn300, name_dst='Петриковский')
        District.objects.create(code='318', region=rgn300, name_dst='Речицкий')
        District.objects.create(code='319', region=rgn300, name_dst='Рогачевский')
        District.objects.create(code='320', region=rgn300, name_dst='Светлогорский')
        District.objects.create(code='321', region=rgn300, name_dst='Хойникский')
        District.objects.create(code='322', region=rgn300, name_dst='Чечерский')

        rgn400 = Region.objects.get(code='400')
        District.objects.create(code='401', region=rgn400, name_dst='г. Гродно')
        District.objects.create(code='402', region=rgn400, name_dst='Берестовицкий')
        District.objects.create(code='403', region=rgn400, name_dst='Волковысский')
        District.objects.create(code='404', region=rgn400, name_dst='Вороновский')
        District.objects.create(code='405', region=rgn400, name_dst='Гродненский')
        District.objects.create(code='406', region=rgn400, name_dst='Дятловский')
        District.objects.create(code='407', region=rgn400, name_dst='Зельвенский')
        District.objects.create(code='408', region=rgn400, name_dst='Ивьевский')
        District.objects.create(code='409', region=rgn400, name_dst='Кореличский')
        District.objects.create(code='410', region=rgn400, name_dst='Лидский')
        District.objects.create(code='411', region=rgn400, name_dst='Мостовский')
        District.objects.create(code='412', region=rgn400, name_dst='Новогрудский')
        District.objects.create(code='413', region=rgn400, name_dst='Островецкий')
        District.objects.create(code='414', region=rgn400, name_dst='Ошмянский')
        District.objects.create(code='415', region=rgn400, name_dst='Свислочский')
        District.objects.create(code='416', region=rgn400, name_dst='Слонимский')
        District.objects.create(code='417', region=rgn400, name_dst='Сморгонский')
        District.objects.create(code='418', region=rgn400, name_dst='Щучинский')

        rgn500 = Region.objects.get(code='500')
        District.objects.create(code='501', region=rgn500, name_dst='Березинский')
        District.objects.create(code='502', region=rgn500, name_dst='Борисовский')
        District.objects.create(code='503', region=rgn500, name_dst='Вилейский')
        District.objects.create(code='504', region=rgn500, name_dst='Воложинский')
        District.objects.create(code='505', region=rgn500, name_dst='г. Жодино')
        District.objects.create(code='506', region=rgn500, name_dst='Дзержинский')
        District.objects.create(code='507', region=rgn500, name_dst='Клецкий')
        District.objects.create(code='508', region=rgn500, name_dst='Копыльский')
        District.objects.create(code='509', region=rgn500, name_dst='Крупский')
        District.objects.create(code='510', region=rgn500, name_dst='Логойский')
        District.objects.create(code='511', region=rgn500, name_dst='Любанский')
        District.objects.create(code='512', region=rgn500, name_dst='Минский')
        District.objects.create(code='513', region=rgn500, name_dst='Молодечненский')
        District.objects.create(code='514', region=rgn500, name_dst='Мядельский')
        District.objects.create(code='515', region=rgn500, name_dst='Несвижский')
        District.objects.create(code='516', region=rgn500, name_dst='Пуховичский')
        District.objects.create(code='517', region=rgn500, name_dst='Слуцкий')
        District.objects.create(code='518', region=rgn500, name_dst='Смолевичский')
        District.objects.create(code='519', region=rgn500, name_dst='Солигорский')
        District.objects.create(code='520', region=rgn500, name_dst='Стародорожский')
        District.objects.create(code='521', region=rgn500, name_dst='Столбцовский')
        District.objects.create(code='522', region=rgn500, name_dst='Узденский')
        District.objects.create(code='523', region=rgn500, name_dst='Червенский')
        District.objects.create(code='524', region=rgn500, name_dst='Жодинский')

        rgn600 = Region.objects.get(code='600')
        District.objects.create(code='601', region=rgn600, name_dst='г. Могилёв')
        District.objects.create(code='602', region=rgn600, name_dst='Белыничский')
        District.objects.create(code='603', region=rgn600, name_dst='Бобруйский')
        District.objects.create(code='604', region=rgn600, name_dst='Быховский')
        District.objects.create(code='605', region=rgn600, name_dst='Глусский')
        District.objects.create(code='606', region=rgn600, name_dst='Горецкий')
        District.objects.create(code='607', region=rgn600, name_dst='Дрибинский')
        District.objects.create(code='608', region=rgn600, name_dst='Кировский')
        District.objects.create(code='609', region=rgn600, name_dst='Климовичский')
        District.objects.create(code='610', region=rgn600, name_dst='Кличевский')
        District.objects.create(code='611', region=rgn600, name_dst='Костюковичский')
        District.objects.create(code='612', region=rgn600, name_dst='Краснопольский')
        District.objects.create(code='613', region=rgn600, name_dst='Кричевский')
        District.objects.create(code='614', region=rgn600, name_dst='Круглянский')
        District.objects.create(code='615', region=rgn600, name_dst='Могилёвский')
        District.objects.create(code='616', region=rgn600, name_dst='Мстиславский')
        District.objects.create(code='617', region=rgn600, name_dst='Осиповичский')
        District.objects.create(code='618', region=rgn600, name_dst='Славгородский')
        District.objects.create(code='619', region=rgn600, name_dst='Хотимский')
        District.objects.create(code='620', region=rgn600, name_dst='Чаусский')
        District.objects.create(code='621', region=rgn600, name_dst='Чериковский')
        District.objects.create(code='622', region=rgn600, name_dst='Шкловский')

        rgn700 = Region.objects.get(code='700')
        District.objects.create(code='701', region=rgn700, name_dst='г. Минск')

        _count = District.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f"Районов: {_count}"))

        # Location.objects.all().delete()
        # Location.objects.create(code='', district=None, model_type=None, soato=0, name_lct='')


        # Subdivision.objects.all().delete()
        # belpost = Subdivision.objects.create(name='Белпочта')
        # Subdivision.objects.create(parent=belpost, name='Брестский филиал')
        # Subdivision.objects.create(parent=belpost, name='Витебский филиал')
        # Subdivision.objects.create(parent=belpost, name='Гомельский филиал')
        # Subdivision.objects.create(parent=belpost, name='Гродненский филиал')
        # Subdivision.objects.create(parent=belpost, name='Минский филиал')
        # Subdivision.objects.create(parent=belpost, name='Могилевский филиал')
        # Subdivision.objects.create(parent=belpost, name='Минск - город')
        #
        # _count = Subdivision.objects.all().count()
        # self.stdout.write(self.style.SUCCESS(f"Подразделений: {_count}"))



        # phone = Phone.objects.create(phone_number='375447661664')
        # phone = Phone.objects.get(phone_number='375447661664')
        # print(phone.flex_type.name)
        # print(phone)
        # phone_type = ContentType.objects.get_for_model(FlexType)
        # print(phone_type)
        # t = FlexType(content_object=phone, name='Тип телефончика')
        # t.save()
        # print(t.content_object)
        # print(phone.flex_type.name)
        # FlexType.objects.create(content_object=phone, name='Городской')
        # f_type = FlexType.objects.create(content_object=phone, name='Мобильный')
        # FlexType.objects.create(name='Мобильный')
        # print(f_type)

        # ft = FlexType.objects.get(pk=3)
        # print(ft.content_object.phone_number)
