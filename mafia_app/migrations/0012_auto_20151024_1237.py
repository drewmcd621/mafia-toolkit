# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('mafia_app', '0011_comment_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='gamehost',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 24, 12, 37, 8, 517000)),
        ),
    ]
