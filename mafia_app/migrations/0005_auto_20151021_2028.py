# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mafia_app', '0004_auto_20151020_2004'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentVersion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(blank=True)),
                ('timestamp', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Death',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('notes', models.TextField(blank=True)),
                ('phase', models.ForeignKey(to='mafia_app.Phase')),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='text',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='player',
            name='is_dead',
        ),
        migrations.AddField(
            model_name='death',
            name='player',
            field=models.ForeignKey(to='mafia_app.Player'),
        ),
        migrations.AddField(
            model_name='commentversion',
            name='comment',
            field=models.ForeignKey(to='mafia_app.Comment'),
        ),
    ]
