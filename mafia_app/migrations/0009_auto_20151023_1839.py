# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mafia_app', '0008_auto_20151021_2042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentversion',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='voteversion',
            name='vote',
        ),
        migrations.RemoveField(
            model_name='voteversion',
            name='voteAgainst',
        ),
        migrations.AddField(
            model_name='comment',
            name='editedTS',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='timestamp',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='vote',
            name='text',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='vote',
            name='timestamp',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='vote',
            name='voteAgainst',
            field=models.ForeignKey(related_name='voteAgainst', to='mafia_app.Player', null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='alignment',
            field=models.CharField(default=b'U', max_length=1, choices=[(b'U', b'Unknown'), (b'M', b'Mafia'), (b'T', b'Town'), (b'I', b'Independent'), (b'O', b'Other')]),
        ),
        migrations.AlterField(
            model_name='vote',
            name='redditID',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='vote',
            name='voter',
            field=models.ForeignKey(related_name='voter', to='mafia_app.Player', null=True),
        ),
        migrations.DeleteModel(
            name='CommentVersion',
        ),
        migrations.DeleteModel(
            name='VoteVersion',
        ),
    ]
