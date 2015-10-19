from django.db import models

# Create your models here.
class Games(models.Model):
    gameName = model.CharField(max_length=200)
    password = model.CharField(max_length=100, null=True)


class Players(models.Model):
    game = models.ManyToManyField(Games)
    username = models.CharField(max_length=200)
    redditID = models.CharField(max_length=50)

class Phases(models.Model):
    PHASE_TYPE = (
        ('D', 'Day'),
        ('N', 'Night'),
        ('O', 'Other'),
    )
    game = models.ForeignKey(Games)
    phaseType =  models.CharField(max_length=1, choices=PHASE_TYPE)
    redditID = models.CharField(max_length=50)

#general game comments
class Comments(models.Model):
    game = models.ForeignKey(Games)
    player = models.ForeignKey(Players)
    phase = models.ForeignKey(Phases)
    text = models.TextField()
    timestamp = models.DateTimeField()

#votes are special comments in the voting thread
class Votes(models.Model):
    game = models.ForeignKey(Games)
    phase = models.ForeignKey(Phases)
    voter = models.ForeignKey(Players)
    voteAgainst = models.ForeignKey(Players)
    text = models.TextField()
    timestamp = models.DateTimeField()
