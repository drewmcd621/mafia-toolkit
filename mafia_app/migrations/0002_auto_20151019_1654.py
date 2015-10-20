# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mafia_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phase',
            name='number',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='phase',
            name='title',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='timestamp',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='password',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='phase',
            name='redditID',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='redditID',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='username',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='vote',
            name='text',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='vote',
            name='timestamp',
            field=models.DateTimeField(blank=True),
        ),
    ]
