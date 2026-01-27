from Team import Team
from Coach import Coach
from League import League
from Player import Player

# Create teams
team1 = Team("Houston Rockets", "West", "Southwest")
team2 = Team("LA Lakers", "West", "Pacific")
teams = [team1, team2]

# Create league
league = League("NBA", teams)

# Create draft class
league.create_draft_class()

# Create trade engine
league.create_trade_engine()

# Create season simulator
league.create_season_simulator()

# Start draft
league.start_draft()

# Start season
league.start_season()
