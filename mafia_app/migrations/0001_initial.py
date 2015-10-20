# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('timestamp', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gameName', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Phase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phaseType', models.CharField(max_length=1, choices=[(b'D', b'Day'), (b'N', b'Night'), (b'O', b'Other')])),
                ('redditID', models.CharField(max_length=50)),
                ('game', models.ForeignKey(to='mafia_app.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=200)),
                ('redditID', models.CharField(max_length=50)),
                ('game', models.ManyToManyField(to='mafia_app.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('timestamp', models.DateTimeField()),
                ('game', models.ForeignKey(to='mafia_app.Game')),
                ('phase', models.ForeignKey(to='mafia_app.Phase')),
                ('voteAgainst', models.ForeignKey(related_name='voteAgainst', to='mafia_app.Player')),
                ('voter', models.ForeignKey(related_name='voter', to='mafia_app.Player')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='game',
            field=models.ForeignKey(to='mafia_app.Game'),
        ),
        migrations.AddField(
            model_name='comment',
            name='phase',
            field=models.ForeignKey(to='mafia_app.Phase'),
        ),
        migrations.AddField(
            model_name='comment',
            name='player',
            field=models.ForeignKey(to='mafia_app.Player'),
        ),
    ]
