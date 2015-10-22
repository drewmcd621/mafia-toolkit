# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mafia_app', '0007_death_game'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='redditID',
        ),
        migrations.AddField(
            model_name='player',
            name='alignment',
            field=models.CharField(default=b'U', max_length=1, choices=[(b'U', b'Unknown'), (b'M', b'Mafia'), (b'T', b'Town'), (b'O', b'Other')]),
        ),
        migrations.AddField(
            model_name='player',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='player',
            name='role',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
