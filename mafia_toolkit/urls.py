from django.conf.urls import include, url
from django.contrib import admin

from mafia_app import views

urlpatterns = [

    #Admin
    url(r'^admin/', include(admin.site.urls)),

    #Show game create screen
    url(r'^$', views.index, name='index'),

    #game login
    url(r'^g/(?P<game>[^\s\/]+)/login/$', views.password, name='password'),

    #Main game dashboard
    url(r'^g/(?P<game>[^\s\/]+)/$', views.game, name='game'),

    #List players in game
    url(r'^g/(?P<game>[^\s\/]+)/players/$', views.players, name='players'),

    #single player
    url(r'^g/(?P<game>[^\s\/]+)/players/(?P<player>[^\s\/]+)$', views.player, name='player'),

    #list phases in a game
    url(r'^g/(?P<game>[^\s\/]+)/phases/$', views.phases, name='phases'),

    #add a phase
    url(r'^g/(?P<game>[^\s\/]+)/phases/add$', views.addphase, name='phases-add'),

    #List comments in a game
    url(r'^g/(?P<game>[^\s\/]+)/comments/$', views.comments, name='comments'),

]
