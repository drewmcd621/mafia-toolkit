# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mafia_app', '0005_auto_20151021_2028'),
    ]

    operations = [
        migrations.CreateModel(
            name='VoteVersion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(blank=True)),
                ('timestamp', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='vote',
            name='text',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='voteAgainst',
        ),
        migrations.AddField(
            model_name='comment',
            name='redditID',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='vote',
            name='redditID',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='voteversion',
            name='vote',
            field=models.ForeignKey(to='mafia_app.Vote'),
        ),
        migrations.AddField(
            model_name='voteversion',
            name='voteAgainst',
            field=models.ForeignKey(related_name='voteAgainst', to='mafia_app.Player'),
        ),
    ]
