# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mafia_app', '0002_auto_20151019_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='is_dead',
            field=models.BooleanField(default=0),
        ),
        migrations.RemoveField(
            model_name='player',
            name='game',
        ),
        migrations.AddField(
            model_name='player',
            name='game',
            field=models.ForeignKey(default=0, to='mafia_app.Game'),
            preserve_default=False,
        ),
    ]
