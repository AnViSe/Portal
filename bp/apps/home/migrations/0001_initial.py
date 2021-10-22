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
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False,
                                           verbose_name='ID')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True,
                                                      on_delete=django.db.models.deletion.SET_NULL,
                                                      related_name='children', to='home.menu',
                                                      verbose_name='Родитель')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('route', models.CharField(blank=True, max_length=100, null=True,
                                           verbose_name='Имя маршрута')),
                ('perm', models.CharField(blank=True, max_length=100, null=True,
                                          verbose_name='Разрешение')),
                ('icon', models.CharField(blank=True, default='far fa-circle', max_length=30,
                                          null=True, verbose_name='Иконка')),
                ('badge', models.CharField(blank=True, max_length=20, null=True,
                                           verbose_name='Метка')),
                ('header', models.BooleanField(default=False, verbose_name='Заголовок')),
                ('status', core.fields.StatusField()),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
            ],
            options={
                'verbose_name': 'пункт меню',
                'verbose_name_plural': 'пункты меню',
            },
        ),
    ]
