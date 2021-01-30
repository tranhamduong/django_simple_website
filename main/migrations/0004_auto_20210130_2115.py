# Generated by Django 3.1.5 on 2021-01-30 14:15

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210130_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='jackpot_keys',
            field=models.CharField(default=main.models.Candidate.get_random_number, max_length=4, unique=True),
        ),
    ]