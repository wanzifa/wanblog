# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-27 07:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wanzi', '0006_auto_20160227_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 27, 7, 16, 58, 613950, tzinfo=utc)),
        ),
    ]
