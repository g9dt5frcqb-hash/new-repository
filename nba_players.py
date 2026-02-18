import json
from nba_player import NBAPlayer

def load_nba_players_from_json(path="players.json"):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    players = []
    for p in data:
        players.append(
            NBAPlayer(
                name=p["name"],
                position=p["position"],
                team=p["team"],
                height=p["height"],
                weight=p["weight"],
                age=p["age"],
                overall=p["overall"],
                potential=p["potential"],
                archetype=p["archetype"],
                badges=p.get("badges", []),
                contract=p.get("contract", {})
            )
        )
    return players

nba_players = load_nba_players_from_json()