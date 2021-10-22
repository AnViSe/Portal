# Generated by Django 3.2.8 on 2021-10-22 12:25

import core.fields
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('code', core.fields.CodeField(unique=True)),
                ('name_cnt', models.CharField(db_index=True, max_length=100,
                                              verbose_name='Наименование')),
                ('alpha2', models.CharField(max_length=2, verbose_name='Код2')),
                ('alpha3', models.CharField(max_length=3, verbose_name='Код3')),
                ('dt_cr', core.fields.CreateDateTimeField()),
                ('dt_up', core.fields.UpdateDateTimeField()),
                ('status', core.fields.StatusField()),
            ],
            options={
                'verbose_name': 'страна',
                'verbose_name_plural': 'страны',
                'db_table': 'ref_country',
                'ordering': ['id'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('code', core.fields.CodeField(unique=True)),
                ('name_dst', models.CharField(db_index=True, max_length=60,
                                              verbose_name='Наименование')),
                ('dt_cr', core.fields.CreateDateTimeField()),
                ('dt_up', core.fields.UpdateDateTimeField()),
                ('status', core.fields.StatusField()),
            ],
            options={
                'verbose_name': 'район',
                'verbose_name_plural': 'районы',
                'db_table': 'ref_district',
                'ordering': ['id'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FlexObject',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False,
                                                   verbose_name='ID')),
                ('object_name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('object_app', models.CharField(max_length=100, verbose_name='Приложение')),
                ('object_model', models.CharField(max_length=100, verbose_name='Модель')),
            ],
            options={
                'verbose_name': 'объект',
                'verbose_name_plural': 'объекты',
                'db_table': 'ref_object',
                'ordering': ['id'],
                'unique_together': {('object_app', 'object_model')},
            },
        ),
        migrations.CreateModel(
            name='FlexType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False,
                                           verbose_name='ID')),
                ('type_code', core.fields.CodeField()),
                ('type_name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('type_name_full', models.CharField(blank=True, max_length=255, null=True,
                                                    verbose_name='Наименование полное')),
                ('type_desc', models.CharField(blank=True, max_length=255, null=True,
                                               verbose_name='Описание')),
                ('type_object', models.ForeignKey(blank=True, null=True,
                                                  on_delete=django.db.models.deletion.SET_NULL,
                                                  to='references.flexobject',
                                                  verbose_name='Имя модели')),
                ('status', core.fields.StatusField()),
            ],
            options={
                'verbose_name': 'тип',
                'verbose_name_plural': 'типы',
                'db_table': 'ref_type',
                'ordering': ['id'],
                'unique_together': {('type_object', 'type_code')},
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True,
                                                verbose_name='Имя')),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True,
                                                 verbose_name='Отчество')),
                ('name_lfm', models.CharField(db_index=True, editable=False, max_length=150,
                                              verbose_name='Фамилия И.О.')),
                ('name_fml', models.CharField(editable=False, max_length=150,
                                              verbose_name='И.О. Фамилия')),
                ('pers_num', models.CharField(blank=True, db_index=True, max_length=14, null=True,
                                              verbose_name='Личный номер')),
                ('birth_date', models.DateField(blank=True, null=True,
                                                verbose_name='Дата рождения')),
                ('gender', core.fields.GenderField()),
                ('dt_cr', core.fields.CreateDateTimeField()),
                ('dt_up', core.fields.UpdateDateTimeField()),
                ('status', core.fields.StatusField()),
            ],
            options={
                'verbose_name': 'персона',
                'verbose_name_plural': 'персоны',
                'db_table': 'ref_person',
                'ordering': ['id'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Subdivision',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True,
                                                      on_delete=django.db.models.deletion.SET_NULL,
                                                      related_name='children',
                                                      to='references.subdivision',
                                                      verbose_name='Родитель')),
                ('name_sd', models.CharField(db_index=True, max_length=50,
                                             verbose_name='Наименование')),
                ('name_sd_full', models.CharField(blank=True, max_length=255, null=True,
                                                  verbose_name='Наименование полное')),
                ('dt_cr', core.fields.CreateDateTimeField()),
                ('dt_up', core.fields.UpdateDateTimeField()),
                ('status', core.fields.StatusField()),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
            ],
            options={
                'verbose_name': 'подразделение',
                'verbose_name_plural': 'подразделения',
                'db_table': 'ref_subdivision',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('code', core.fields.CodeField(unique=True)),
                ('name_rgn', models.CharField(db_index=True, max_length=60,
                                              verbose_name='Наименование')),
                ('country', models.ForeignKey(blank=True, null=True,
                                              on_delete=django.db.models.deletion.SET_NULL,
                                              to='references.country', verbose_name='Страна')),
                ('dt_cr', core.fields.CreateDateTimeField()),
                ('dt_up', core.fields.UpdateDateTimeField()),
                ('status', core.fields.StatusField()),
            ],
            options={
                'verbose_name': 'область',
                'verbose_name_plural': 'области',
                'db_table': 'ref_region',
                'ordering': ['id'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(db_index=True, max_length=15,
                                                  verbose_name='Номер телефона')),
                ('model_type',
                 models.ForeignKey(blank=True, limit_choices_to={'type_object': 0}, null=True,
                                   on_delete=django.db.models.deletion.SET_NULL,
                                   to='references.flextype', verbose_name='Тип')),
                ('dt_cr', core.fields.CreateDateTimeField()),
                ('dt_up', core.fields.UpdateDateTimeField()),
                ('status', core.fields.StatusField()),
            ],
            options={
                'verbose_name': 'телефон',
                'verbose_name_plural': 'телефоны',
                'db_table': 'ref_phone',
                'ordering': ['id'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PersonPhones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False,
                                           verbose_name='ID')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                             to='references.person', verbose_name='Персона')),
                ('phone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                            to='references.phone', verbose_name='Телефон')),
                ('phone_type', models.ForeignKey(blank=True, limit_choices_to=3, null=True,
                                                 on_delete=django.db.models.deletion.SET_NULL,
                                                 to='references.flextype', verbose_name='Тип')),
                ('status', core.fields.StatusField()),
            ],
            options={
                'verbose_name': 'Телефон персоны',
                'verbose_name_plural': 'Телефоны персоны',
                'db_table': 'ref_person_phones',
            },
        ),
        migrations.AddField(
            model_name='person',
            name='phones',
            field=models.ManyToManyField(related_name='persons', through='references.PersonPhones',
                                         to='references.Phone', verbose_name='Телефоны'),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('code', core.fields.CodeField(unique=True)),
                ('soato', models.BigIntegerField(unique=True, verbose_name='СОАТО')),
                ('name_lct', models.CharField(max_length=100, verbose_name='Наименование')),
                ('name_lct_full', models.CharField(db_index=True, editable=False, max_length=150,
                                                   verbose_name='Наименование полное')),
                ('district', models.ForeignKey(blank=True, null=True,
                                               on_delete=django.db.models.deletion.SET_NULL,
                                               to='references.district', verbose_name='район')),
                ('model_type', models.ForeignKey(blank=True, limit_choices_to=1, null=True,
                                                 on_delete=django.db.models.deletion.SET_NULL,
                                                 to='references.flextype', verbose_name='Тип')),
                ('dt_cr', core.fields.CreateDateTimeField()),
                ('dt_up', core.fields.UpdateDateTimeField()),
                ('status', core.fields.StatusField()),
            ],
            options={
                'verbose_name': 'населенный пункт',
                'verbose_name_plural': 'населенные пункты',
                'db_table': 'ref_location',
                'ordering': ['id'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('tab_num', models.PositiveIntegerField(unique=True, verbose_name='Табельный')),
                ('person', models.ForeignKey(blank=True, null=True,
                                             on_delete=django.db.models.deletion.SET_NULL,
                                             to='references.person', verbose_name='Персона')),
                ('subdivision', models.ForeignKey(blank=True, null=True,
                                                  on_delete=django.db.models.deletion.SET_NULL,
                                                  to='references.subdivision',
                                                  verbose_name='Подразделение')),
                ('dt_cr', core.fields.CreateDateTimeField()),
                ('dt_up', core.fields.UpdateDateTimeField()),
                ('status', core.fields.StatusField()),
            ],
            options={
                'verbose_name': 'сотрудник',
                'verbose_name_plural': 'сотрудники',
                'db_table': 'ref_employee',
                'ordering': ['id'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='district',
            name='region',
            field=models.ForeignKey(blank=True, null=True,
                                    on_delete=django.db.models.deletion.SET_NULL,
                                    to='references.region', verbose_name='Область'),
        ),
    ]
