# Generated by Django 3.2.8 on 2021-11-08 07:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('references', '0003_related'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flextype',
            name='type_value',
            field=models.CharField(blank=True, db_index=True, max_length=15, null=True,
                                   verbose_name='Значение'),
        ),
    ]