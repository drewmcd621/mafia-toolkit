# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mafia_app', '0009_auto_20151023_1839'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='editedTS',
            new_name='editedTime',
        ),
        migrations.AddField(
            model_name='phase',
            name='text',
            field=models.TextField(null=True, blank=True),
        ),
    ]
