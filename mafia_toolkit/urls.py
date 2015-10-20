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
]
