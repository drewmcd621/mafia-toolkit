from django.db import models

# Create your models here.
class Game(models.Model):
    gameName = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=100, null=True, blank=True)


class Player(models.Model):
    game = models.ForeignKey(Game)
    username = models.CharField(max_length=200, blank=True)
    redditID = models.CharField(max_length=50, blank=True)

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
    redditID = models.CharField(max_length=50, blank=True)

class CommentVersion(models.Model):
    comment = models.ForeignKey(Comment)
    text = models.TextField(blank=True)
    timestamp = models.DateTimeField(blank=True)


#votes are special comments in the voting thread
class Vote(models.Model):
    game = models.ForeignKey(Game)
    phase = models.ForeignKey(Phase)
    voter = models.ForeignKey(Player, related_name='voter')
    redditID = models.CharField(max_length=50, blank=True)

class VoteVersion(models.Model):
    vote = models.ForeignKey(Vote)
    voteAgainst = models.ForeignKey(Player, related_name='voteAgainst')
    text = models.TextField(blank=True)
    timestamp = models.DateTimeField(blank=True)

#death logs
class Death(models.Model):
    game = models.ForeignKey(Game)
    player = models.ForeignKey(Player)
    phase = models.ForeignKey(Phase)
    notes = models.TextField(blank=True)
