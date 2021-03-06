# Generated by Django 3.1.4 on 2021-05-15 16:21

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='duration',
        ),
        migrations.AlterField(
            model_name='booking',
            name='booked_at',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='booking',
            name='persons_num',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='количество человек'),
        ),
    ]
