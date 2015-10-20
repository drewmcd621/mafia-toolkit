from django.db import models

# Create your models here.
class Game(models.Model):
    gameName = models.CharField(max_length=200)
    password = models.CharField(max_length=100, null=True, blank=True)


class Player(models.Model):
    game = models.ForeignKey(Game)
    username = models.CharField(max_length=200, blank=True)
    redditID = models.CharField(max_length=50, blank=True)
    is_dead = models.BooleanField(default=0);

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

#general game comments
class Comment(models.Model):
    game = models.ForeignKey(Game)
    player = models.ForeignKey(Player)
    phase = models.ForeignKey(Phase)
    text = models.TextField(blank=True)
    timestamp = models.DateTimeField(blank=True)

#votes are special comments in the voting thread
class Vote(models.Model):
    game = models.ForeignKey(Game)
    phase = models.ForeignKey(Phase)
    voter = models.ForeignKey(Player, related_name='voter')
    voteAgainst = models.ForeignKey(Player, related_name='voteAgainst')
    text = models.TextField(blank=True)
    timestamp = models.DateTimeField(blank=True)
