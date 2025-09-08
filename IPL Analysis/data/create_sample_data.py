import sqlite3
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Create a connection to the SQLite database
conn = sqlite3.connect('db.sqlite3')

# Create sample IPL data
# Teams
teams = [
    'Mumbai Indians', 'Chennai Super Kings', 'Royal Challengers Bangalore',
    'Kolkata Knight Riders', 'Delhi Capitals', 'Punjab Kings',
    'Rajasthan Royals', 'Sunrisers Hyderabad', 'Gujarat Titans',
    'Lucknow Super Giants'
]

# Players
players = [
    'Virat Kohli', 'Rohit Sharma', 'MS Dhoni', 'David Warner', 'Steve Smith',
    'AB de Villiers', 'Chris Gayle', 'Andre Russell', 'Jasprit Bumrah', 'Ravindra Jadeja',
    'Hardik Pandya', 'Kieron Pollard', 'Shikhar Dhawan', 'KL Rahul', 'Jos Buttler',
    'Ben Stokes', 'Pat Cummins', 'Jofra Archer', 'Trent Boult', 'Rashid Khan'
]

# Create matches table
matches_data = []
for i in range(100):
    match_date = datetime(2023, 3, 31) + timedelta(days=np.random.randint(0, 180))
    team1 = np.random.choice(teams)
    team2 = np.random.choice([team for team in teams if team != team1])
    winner = np.random.choice([team1, team2])
    margin = np.random.randint(1, 20)
    
    matches_data.append({
        'id': i+1,
        'date': match_date.strftime('%Y-%m-%d'),
        'team1': team1,
        'team2': team2,
        'winner': winner,
        'margin': margin,
        'venue': f'Stadium {np.random.randint(1, 21)}'
    })

matches_df = pd.DataFrame(matches_data)
matches_df.to_sql('dashboard_match', conn, if_exists='replace', index=False)

# Create players table
players_data = []
for i, player in enumerate(players):
    team = np.random.choice(teams)
    matches_played = np.random.randint(10, 50)
    runs = np.random.randint(200, 1000)
    wickets = np.random.randint(0, 30)
    
    players_data.append({
        'id': i+1,
        'name': player,
        'team': team,
        'matches_played': matches_played,
        'runs': runs,
        'wickets': wickets,
        'average': round(runs/max(1, matches_played), 2)
    })

players_df = pd.DataFrame(players_data)
players_df.to_sql('dashboard_player', conn, if_exists='replace', index=False)

# Create teams table
teams_data = []
for i, team in enumerate(teams):
    matches_played = np.random.randint(10, 20)
    wins = np.random.randint(5, matches_played)
    losses = matches_played - wins
    
    teams_data.append({
        'id': i+1,
        'name': team,
        'matches_played': matches_played,
        'wins': wins,
        'losses': losses,
        'win_percentage': round((wins/matches_played)*100, 2)
    })

teams_df = pd.DataFrame(teams_data)
teams_df.to_sql('dashboard_team', conn, if_exists='replace', index=False)

# Close the connection
conn.close()

print("Sample IPL data created successfully!")
