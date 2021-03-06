# Generated by Django 3.2.8 on 2021-11-09 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('references', '0004_flextype'),
        ('delivery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='address',
            field=models.ForeignKey(blank=True, null=True,
                                    on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='mails+', to='references.address',
                                    verbose_name='Адрес доставки'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='notice_number',
            field=models.PositiveIntegerField(blank=True, editable=False, null=True,
                                              verbose_name='№ извещения'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='person',
            field=models.ForeignKey(blank=True, null=True,
                                    on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='mails', to='references.person',
                                    verbose_name='Получатель'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='phone',
            field=models.ForeignKey(blank=True, null=True,
                                    on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='mails+', to='references.phone',
                                    verbose_name='Телефон получателя'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='subdivision',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='mails', to='references.subdivision',
                                    verbose_name='Подразделение'),
        ),
        migrations.AddField(
            model_name='mailing',
            name='status',
            field=models.PositiveSmallIntegerField(default=1, editable=False,
                                                   verbose_name='Статус'),
        ),
    ]
