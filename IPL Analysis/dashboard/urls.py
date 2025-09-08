from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('teams/', views.teams, name='teams'),
    path('players/', views.players, name='players'),
    path('matches/', views.matches, name='matches'),
    path('statistics/', views.statistics, name='statistics'),
    path('team-stats/', views.team_stats, name='team_stats'),
    path('player-stats/', views.player_stats, name='player_stats'),
]
