from django.contrib import admin

# Register your models here.
from .models import Game
from .models import Player
from .models import Phase
from .models import Comment
from .models import Vote

class GameAdmin(admin.ModelAdmin):
    list_display = ['gameName']

class PlayerAdmin(admin.ModelAdmin):
    list_display = ['username']

class PhaseAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(Game, GameAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Phase)
admin.site.register(Comment)
admin.site.register(Vote)
