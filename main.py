import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()  # loads GEMINI_API_KEY from .env

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
gemini_client = genai.GenerativeModel("gemini-pro")


from Team import Team
from Coach import Coach
from League import League
from Player import Player


team1 = Team("Boston Celtics", "East", "Atlantic")
team2 = Team("Brooklyn Nets", "East", "Atlantic")
team3 = Team("New York Knicks", "East", "Atlantic")
team4 = Team("Philadelphia 76ers", "East", "Atlantic")
team5 = Team("Toronto Raptors", "East", "Atlantic")

team6 = Team("Chicago Bulls", "East", "Central")
team7 = Team("Cleveland Cavaliers", "East", "Central")
team8 = Team("Detroit Pistons", "East", "Central")
team9 = Team("Indiana Pacers", "East", "Central")
team10 = Team("Milwaukee Bucks", "East", "Central")

team11 = Team("Atlanta Hawks", "East", "Southeast")
team12 = Team("Charlotte Hornets", "East", "Southeast")
team13 = Team("Miami Heat", "East", "Southeast")
team14 = Team("Orlando Magic", "East", "Southeast")
team15 = Team("Washington Wizards", "East", "Southeast")

team16 = Team("Denver Nuggets", "West", "Northwest")
team17 = Team("Minnesota Timberwolves", "West", "Northwest")
team18 = Team("Oklahoma City Thunder", "West", "Northwest")
team19 = Team("Portland Trail Blazers", "West", "Northwest")
team20 = Team("Utah Jazz", "West", "Northwest")

team21 = Team("Golden State Warriors", "West", "Pacific")
team22 = Team("LA Clippers", "West", "Pacific")
team23 = Team("Los Angeles Lakers", "West", "Pacific")
team24 = Team("Phoenix Suns", "West", "Pacific")
team25 = Team("Sacramento Kings", "West", "Pacific")

team26 = Team("Dallas Mavericks", "West", "Southwest")
team27 = Team("Houston Rockets", "West", "Southwest")
team28 = Team("Memphis Grizzlies", "West", "Southwest")
team29 = Team("New Orleans Pelicans", "West", "Southwest")
team30 = Team("San Antonio Spurs", "West", "Southwest")

teams = [
    team1, team2, team3, team4, team5,
    team6, team7, team8, team9, team10,
    team11, team12, team13, team14, team15,
    team16, team17, team18, team19, team20,
    team21, team22, team23, team24, team25,
    team26, team27, team28, team29, team30
]


league = League("NBA", teams)
league.create_draft_class()
league.create_trade_engine()
league.create_season_simulator()


league.start_draft()
league.start_season(gemini_client=gemini_client)
