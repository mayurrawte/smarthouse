# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-10 07:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartpanel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devicelog',
            name='fan',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='devicelog',
            name='heater',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='devicelog',
            name='humidity',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='devicelog',
            name='moisture',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='devicelog',
            name='temperature',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='devicelog',
            name='waterpump',
            field=models.SmallIntegerField(default=0),
        ),
    ]