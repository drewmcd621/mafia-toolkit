# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mafia_app', '0003_auto_20151019_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='gameName',
            field=models.CharField(unique=True, max_length=200),
        ),
    ]
