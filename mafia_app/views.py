from django.shortcuts import render
from django.shortcuts import redirect
from django.http import Http404

from mafia_app.models import *
from mafia_app.forms import *
from mafia_app.reddit import *

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
    players = Player.objects.filter(game = gameO.id)
    r = render(request, 'game/players.html',
    {
    'game':gameO,
    'players':players
    })
    return checkAuth(request, gameO, r)

def player(request, game, player):
    gameO = getGame(request, game)
    if not gameO:
        return redirect('index')
    try:
        playerO = Player.objects.get(username = player, game = gameO.id)
    except Player.DoesNotExist:
        return redirect('game', game = gameO.gameName )
    r = render(request, 'game/player.html',{
        'game':gameO,
        'player':playerO,
    })
    return checkAuth(request, gameO, r)


def comments(request, game):
    gameO = getGame(request, game)
    if not gameO:
        return redirect('index')
    phaseO = Phase.objects.first()
    parse_comments(gameO)
    r = render(request, 'game/comments.html',
    {
    'game':gameO,
    })
    return checkAuth(request, gameO, r)

def phases(request, game):
    gameO = getGame(request, game)

    if not gameO:
        return redirect('index')
    #If we get a post
    post = None
    if request.method == 'POST':
        form = addPhaseForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['reddit_url']
            post = get_post_info(url)
            title = post.title
            rID = post.id
            text = post.selftext
            phaseType = form.cleaned_data['phase_type']
            phaseNumber = form.cleaned_data['phase_number']
            #TODO: duplicate checking
            p = Phase(game=gameO, number=phaseNumber, title=title, phaseType=phaseType, redditID=rID, text=text)
            p.save()

    phases = Phase.objects.filter(game = gameO.id)
    r = render(request, 'game/phases.html',
    {
    'game':gameO,
    'phases':phases,
    })
    return checkAuth(request, gameO, r)

def addphase(request, game):
    gameO = getGame(request, game)
    if not gameO:
        return redirect('index')
    f = addPhaseForm()
    r = render(request, 'game/phases-add.html',
    {
    'game':gameO,
    'form':f,
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
