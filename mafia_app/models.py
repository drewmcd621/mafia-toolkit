from django.db import models

from datetime import datetime

# Create your models here.
class Game(models.Model):
    gameName = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    gamehost = models.CharField(max_length=200, blank=True)


class Player(models.Model):
    ALIGNMENT = (
        ('U', 'Unknown'),
        ('M', 'Mafia'),
        ('T', 'Town'),
        ('I', 'Independent'),
        ('O', 'Other'),
    )
    game = models.ForeignKey(Game)
    username = models.CharField(max_length=200, blank=True)
    alignment = models.CharField(max_length=1, choices=ALIGNMENT, default='U')
    role = models.CharField(max_length=50, blank=True)
    notes = models.TextField(blank=True)

class Phase(models.Model):
    PHASE_TYPE = (
        ('D', 'Day'),
        ('N', 'Night'),
        ('O', 'Other'),
    )
    game = models.ForeignKey(Game)
    number = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=50, blank=True)
    phaseType =  models.CharField(max_length=1, choices=PHASE_TYPE)
    redditID = models.CharField(max_length=50, blank=True)
    redditLink = models.URLField(max_length=100, blank=True)
    text = models.TextField(blank=True, null=True)

#general game comments
class Comment(models.Model):
    game = models.ForeignKey(Game)
    player = models.ForeignKey(Player)
    phase = models.ForeignKey(Phase)
    redditID = models.CharField(max_length=50, blank=True)
    text = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    editedTime = models.DateTimeField(blank=True, null=True)
    redditLink = models.URLField(max_length=100, blank=True)
    updated = models.DateTimeField(default=datetime.now())

#votes are special comments in the voting thread
class Vote(models.Model):
    game = models.ForeignKey(Game)
    phase = models.ForeignKey(Phase)
    redditID = models.CharField(max_length=50, blank=True, null=True)
    voter = models.ForeignKey(Player, related_name='voter', null=True)
    voteAgainst = models.ForeignKey(Player, related_name='voteAgainst', null=True)
    text = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)


#death logs
class Death(models.Model):
    game = models.ForeignKey(Game)
    player = models.ForeignKey(Player)
    phase = models.ForeignKey(Phase)
    notes = models.TextField(blank=True)
