from django.shortcuts import render
from django.http import Http404

from mafia_app.models import Game

def index(request):
    return  render(request, 'index.html', {})


#game pages
def game(request, game):
    try:
        gameI = Game.objects.get(gameName=game)
    except Game.DoesNotExist:
        raise Http404('you didn\'t say the magic word')
    return render(request, 'game/index.html',
    {
    'game':gameI,
    })

def players(request, game):
    try:
        gameI = Game.objects.get(gameName=game)
    except Game.DoesNotExist:
        raise Http404('you didn\'t say the magic word')
    return render(request, 'game/players.html',
    {
    'game':gameI,
    })

def comments(request, game):
    try:
        gameI = Game.objects.get(gameName=game)
    except Game.DoesNotExist:
        raise Http404('you didn\'t say the magic word')
    return render(request, 'game/comments.html',
    {
    'game':gameI,
    })

def phases(request, game):
    try:
        gameI = Game.objects.get(gameName=game)
    except Game.DoesNotExist:
        raise Http404('you didn\'t say the magic word')
    return render(request, 'game/phases.html',
    {
    'game':gameI,
    })
