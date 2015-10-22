# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mafia_app', '0006_auto_20151021_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='death',
            name='game',
            field=models.ForeignKey(default=0, to='mafia_app.Game'),
            preserve_default=False,
        ),
    ]
