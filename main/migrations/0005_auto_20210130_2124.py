# Generated by Django 3.1.5 on 2021-01-30 14:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210130_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='phone_number',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(code='invalid_phone_number', message='Sai định dạng số điện thoại', regex='\\+?(0|84)\\d{9}')]),
        ),
    ]