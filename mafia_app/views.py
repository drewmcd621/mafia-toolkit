from django.shortcuts import render
from django.shortcuts import redirect
from django.http import Http404

from mafia_app.models import Game
from mafia_app.models import Players

def index(request):
    return  render(request, 'index.html', {})


#game pages
def game(request, game):
    gameO = getGame(request, game)
    if not gameO:
        return redirect('index')

    if request.method == 'POST':
        password = request.POST.get('password')
        if password == gameO.password:
            request.session['auth_' + gameO.gameName] = True
    r = render(request, 'game/index.html',
    {
    'game':gameO,
    })
    return checkAuth(request, gameO, r)

def password(request, game):
    gameO = getGame(request, game)
    if not gameO:
        return redirect('index')
    return  render(request, 'game/password.html',
    {
        'game':gameO,
    })

def players(request, game):
    gameO = getGame(request, game)
    if not gameO:
        return redirect('index')
    playersO =


    r = render(request, 'game/players.html',
    {
    'game':gameO,
    })
    return checkAuth(request, gameO, r)

def comments(request, game):
    gameO = getGame(request, game)
    if not gameO:
        return redirect('index')
    r = render(request, 'game/comments.html',
    {
    'game':gameO,
    })
    return checkAuth(request, gameO, r)

def phases(request, game):
    gameO = getGame(request, game)
    if not gameO:
        return redirect('index')
    r = render(request, 'game/phases.html',
    {
    'game':gameO,
    })
    return checkAuth(request, gameO, r)


#common functions

def getGame(request, gameName):
    try:
        gameO = Game.objects.get(gameName=gameName)
    except Game.DoesNotExist:
        return null
    return gameO

def checkAuth(request, game, render):
    if game.password:
        if 'auth_' + game.gameName in request.session:
            return render
        else:
            return redirect('password', game=game.gameName)
    else:
        return render
