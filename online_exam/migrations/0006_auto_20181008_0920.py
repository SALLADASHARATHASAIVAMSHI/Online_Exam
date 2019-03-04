# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-08 09:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('online_exam', '0005_auto_20181008_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 8, 9, 20, 24, 462124, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='course',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 8, 9, 20, 24, 462158, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 8, 9, 20, 24, 462958, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 8, 9, 20, 24, 462986, tzinfo=utc)),
        ),
    ]