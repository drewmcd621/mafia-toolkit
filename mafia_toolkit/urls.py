from django.conf.urls import include, url
from django.contrib import admin

from mafia_app import views

urlpatterns = [

    #Admin
    url(r'^admin/', include(admin.site.urls)),

    #Show game create screen
    url(r'^$', views.index, name='index'),

    #Main game dashboard
    url(r'^g/(?P<game>\S+)/', views.game, name='game'),

    #List players in game
    url(r'^g/(?P<game>\S+)/players', views.players, name='players'),

    #list phases in a game
    url(r'^g/(?P<game>\S+)/phases', views.phases, name='phases'),

    #List comments in a game
    url(r'^g/(?P<game>\S+)/phases', views.comments, name='comments'),

]
