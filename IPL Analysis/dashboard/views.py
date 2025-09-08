from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
import sqlite3
import json
from .models import Team, Player, Match

def dashboard(request):
    # Connect to the database
    conn = sqlite3.connect('db.sqlite3')
    
    # Read data using pandas
    teams_df = pd.read_sql_query("SELECT * FROM dashboard_team ORDER BY win_percentage DESC", conn)
    players_df = pd.read_sql_query("SELECT * FROM dashboard_player ORDER BY runs DESC LIMIT 10", conn)
    matches_df = pd.read_sql_query("SELECT * FROM dashboard_match ORDER BY date DESC LIMIT 10", conn)
    
    # Perform some analysis
    # Top teams by win percentage
    top_teams = teams_df.head(5).to_dict('records')
    
    # Top run scorers
    top_scorers = players_df[['name', 'runs', 'team']].head(5).to_dict('records')
    
    # Recent matches
    recent_matches = matches_df[['date', 'team1', 'team2', 'winner']].to_dict('records')
    
    # Overall statistics
    total_matches = len(matches_df)
    total_teams = len(teams_df)
    total_players = len(players_df)
    
    # Win percentage distribution
    win_percentage_data = teams_df[['name', 'win_percentage']].to_dict('records')
    
    # Convert to JSON for JavaScript
    win_percentage_json = json.dumps(win_percentage_data)
    
    conn.close()
    
    context = {
        'top_teams': top_teams,
        'top_scorers': top_scorers,
        'recent_matches': recent_matches,
        'total_matches': total_matches,
        'total_teams': total_teams,
        'total_players': total_players,
        'win_percentage_json': win_percentage_json,
    }
    
    return render(request, 'dashboard/index.html', context)

def teams(request):
    # Connect to the database
    conn = sqlite3.connect('db.sqlite3')
    teams_df = pd.read_sql_query("SELECT * FROM dashboard_team ORDER BY wins DESC", conn)
    conn.close()
    
    teams_data = teams_df.to_dict('records')
    
    context = {
        'teams': teams_data
    }
    
    return render(request, 'dashboard/teams.html', context)

def players(request):
    # Connect to the database
    conn = sqlite3.connect('db.sqlite3')
    players_df = pd.read_sql_query("SELECT * FROM dashboard_player ORDER BY runs DESC", conn)
    conn.close()
    
    players_data = players_df.to_dict('records')
    
    context = {
        'players': players_data
    }
    
    return render(request, 'dashboard/players.html', context)

def matches(request):
    # Connect to the database
    conn = sqlite3.connect('db.sqlite3')
    matches_df = pd.read_sql_query("SELECT * FROM dashboard_match ORDER BY date DESC", conn)
    conn.close()
    
    matches_data = matches_df.to_dict('records')
    
    context = {
        'matches': matches_data
    }
    
    return render(request, 'dashboard/matches.html', context)

def statistics(request):
    # Connect to the database
    conn = sqlite3.connect('db.sqlite3')
    
    # Get all data
    teams_df = pd.read_sql_query("SELECT * FROM dashboard_team", conn)
    players_df = pd.read_sql_query("SELECT * FROM dashboard_player", conn)
    matches_df = pd.read_sql_query("SELECT * FROM dashboard_match", conn)
    
    # Calculate statistics
    total_matches = len(matches_df)
    total_teams = len(teams_df)
    total_players = len(players_df)
    
    # Top teams by win percentage
    top_teams = teams_df.nlargest(5, 'win_percentage')[['name', 'win_percentage']].to_dict('records')
    
    # Top run scorers
    top_scorers = players_df.nlargest(5, 'runs')[['name', 'team', 'runs']].to_dict('records')
    
    # Top wicket takers
    top_wicket_takers = players_df.nlargest(5, 'wickets')[['name', 'team', 'wickets']].to_dict('records')
    
    conn.close()
    
    context = {
        'total_matches': total_matches,
        'total_teams': total_teams,
        'total_players': total_players,
        'top_teams': top_teams,
        'top_scorers': top_scorers,
        'top_wicket_takers': top_wicket_takers,
    }
    
    return render(request, 'dashboard/statistics.html', context)

def team_stats(request):
    conn = sqlite3.connect('db.sqlite3')
    teams_df = pd.read_sql_query("SELECT * FROM dashboard_team ORDER BY wins DESC", conn)
    conn.close()
    
    teams_data = teams_df.to_dict('records')
    
    return JsonResponse({'teams': teams_data})

def player_stats(request):
    conn = sqlite3.connect('db.sqlite3')
    players_df = pd.read_sql_query("SELECT * FROM dashboard_player ORDER BY runs DESC", conn)
    conn.close()
    
    players_data = players_df.to_dict('records')
    
    return JsonResponse({'players': players_data})
