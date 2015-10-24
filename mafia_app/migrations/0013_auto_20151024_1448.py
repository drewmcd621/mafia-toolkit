# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('mafia_app', '0012_auto_20151024_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='redditLink',
            field=models.URLField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='phase',
            name='redditLink',
            field=models.URLField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 24, 14, 48, 9, 173000)),
        ),
    ]
