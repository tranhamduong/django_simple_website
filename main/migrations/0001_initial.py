# Generated by Django 3.1.5 on 2021-01-30 13:47

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=200)),
                ('phone_number', models.IntegerField(max_length=10)),
                ('image', stdimage.models.StdImageField(upload_to='image')),
            ],
        ),
    ]