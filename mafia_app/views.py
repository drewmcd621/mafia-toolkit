from django.shortcuts import render
from django.http import Http404

from mafia_app.models import Game

def index(request):
    return  render(request, 'index.html', {})

def game(request, game):
    try:
        game = Game.objects.get(gameName=game)
    except Game.DoesNotExist:
        raise Http404('you didn\'t say the magic word')
    return render(request, 'game/index.html',
    {
    'game':game,
    })
