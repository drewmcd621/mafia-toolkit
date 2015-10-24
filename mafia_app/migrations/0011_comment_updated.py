# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('mafia_app', '0010_auto_20151023_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 23, 20, 15, 46, 139000)),
        ),
    ]
