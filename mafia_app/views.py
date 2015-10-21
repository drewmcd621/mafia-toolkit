from django.shortcuts import render
from django.shortcuts import redirect
from django.http import Http404

from mafia_app.models import Game

def index(request):
    return  render(request, 'index.html', {})


#game pages
def game(request, game):
    gameI = getGame(request, game)
    return render(request, 'game/index.html',
    {
    'game':gameI,
    })

def password(request, game):
    return  render(request, 'index.html', {})

def players(request, game):
    gameI = getGame(request, game)
    return render(request, 'game/players.html',
    {
    'game':gameI,
    })

def comments(request, game):
    gameI = getGame(request, game)
    return render(request, 'game/comments.html',
    {
    'game':gameI,
    })

def phases(request, game):
    gameI = getGame(request, game)
    return render(request, 'game/phases.html',
    {
    'game':gameI,
    })


#common functions

def getGame(request, gameName, render):
    try:
        gameI = Game.objects.get(gameName=gameName)
    except Game.DoesNotExist:
        return null
    return gameI

def checkAuth(request, game, render):
    if game.password:
        if 'auth_' + game.gameName in request.session:
            return render
        else:
            return redirect('password', game=game.gameName)
    else:
        return render
