# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-27 01:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wanzi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 27, 1, 32, 55, 495618, tzinfo=utc)),
        ),
    ]
