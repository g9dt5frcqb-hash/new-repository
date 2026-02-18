import random

class SeasonSimulator:
    def __init__(self, teams, league_type):
        self.teams = teams
        self.league_type = league_type

    # ---------------------------------------------------------
    # Regular Season Logic
    # ---------------------------------------------------------
    def simulate_season(self):
        print(f"\n--- Simulating {self.league_type} Regular Season ---")

        # Simple approximation: each team plays 82 games
        for _ in range(82):
            for team in self.teams:
                if random.random() > 0.5:
                    team.wins += 1
                else:
                    team.losses += 1

        print("Regular season complete.")
        self.print_standings()

    # ---------------------------------------------------------
    # Standings (Conference + Full NBA)
    # ---------------------------------------------------------
    def print_standings(self):
        print("\n--- FINAL REGULAR SEASON STANDINGS ---")
        self.print_conference_standings()
        self.print_full_nba_standings()

    def print_conference_standings(self):
        # EAST
        print("\n=== EASTERN CONFERENCE STANDINGS ===")
        east = [t for t in self.teams if t.conference == "East"]
        east_sorted = sorted(east, key=lambda t: t.wins, reverse=True)

        for seed, team in enumerate(east_sorted, start=1):
            print(f"{seed}. {team.name:<25} {team.wins}-{team.losses}")

        # WEST
        print("\n=== WESTERN CONFERENCE STANDINGS ===")
        west = [t for t in self.teams if t.conference == "West"]
        west_sorted = sorted(west, key=lambda t: t.wins, reverse=True)

        for seed, team in enumerate(west_sorted, start=1):
            print(f"{seed}. {team.name:<25} {team.wins}-{team.losses}")

    def print_full_nba_standings(self):
        print("\n=== FULL NBA STANDINGS ===\n")
        sorted_teams = sorted(self.teams, key=lambda t: t.wins, reverse=True)

        for seed, team in enumerate(sorted_teams, start=1):
            print(f"{seed}. {team.name:<25} {team.wins}-{team.losses}")

    # ---------------------------------------------------------
    # Simulate a single game
    # ---------------------------------------------------------
    def simulate_game(self, teamA, teamB):
        winner = random.choice([teamA, teamB])
        return winner, (teamB if winner == teamA else teamA)

    # ---------------------------------------------------------
    # Playoff Logic
    # ---------------------------------------------------------
    def simulate_playoffs(self, gemini_client=None):
        if self.league_type == "NBA":
            return self.simulate_nba_playoffs(gemini_client=gemini_client)
        else:
            print("NFL Playoff logic not yet implemented.")
            return None

    def simulate_nba_playoffs(self, gemini_client=None):
        print("\n--- NBA Playoffs Begin ---\n")

        sorted_teams = sorted(self.teams, key=lambda t: t.wins, reverse=True)

        east = [t for t in sorted_teams if t.conference == "East"][:8]
        west = [t for t in sorted_teams if t.conference == "West"][:8]

        if len(east) < 8 or len(west) < 8:
            print("Not enough teams in each conference for playoffs.")
            return None

        if gemini_client:
            self.generate_playoff_hype(east + west, gemini_client)

        # ================= EAST =================
        print("\n=== EASTERN CONFERENCE PLAYOFFS ===\n")

        east_r1 = [
            self.simulate_series(east[0], east[7], "East Round 1"),
            self.simulate_series(east[1], east[6], "East Round 1"),
            self.simulate_series(east[2], east[5], "East Round 1"),
            self.simulate_series(east[3], east[4], "East Round 1"),
        ]

        east_semis = [
            self.simulate_series(east_r1[0], east_r1[3], "East Semifinals"),
            self.simulate_series(east_r1[1], east_r1[2], "East Semifinals"),
        ]

        east_champion = self.simulate_series(
            east_semis[0], east_semis[1], "EASTERN CONFERENCE FINALS"
        )

        # ================= WEST =================
        print("\n=== WESTERN CONFERENCE PLAYOFFS ===\n")

        west_r1 = [
            self.simulate_series(west[0], west[7], "West Round 1"),
            self.simulate_series(west[1], west[6], "West Round 1"),
            self.simulate_series(west[2], west[5], "West Round 1"),
            self.simulate_series(west[3], west[4], "West Round 1"),
        ]

        west_semis = [
            self.simulate_series(west_r1[0], west_r1[3], "West Semifinals"),
            self.simulate_series(west_r1[1], west_r1[2], "West Semifinals"),
        ]

        west_champion = self.simulate_series(
            west_semis[0], west_semis[1], "WESTERN CONFERENCE FINALS"
        )

        # ================= FINALS =================
        print("\n=== NBA FINALS ===\n")
        finals_winner = self.simulate_series(
            east_champion, west_champion, "NBA Finals"
        )

        print(f"\n🏆 {finals_winner.name} are the NBA Champions! 🏆\n")

        if gemini_client:
            self.generate_finals_recap(finals_winner, gemini_client)

        return finals_winner

    # ---------------------------------------------------------
    # Best-of-7 Series
    # ---------------------------------------------------------
    def simulate_series(self, teamA, teamB, round_name):
        winsA = 0
        winsB = 0

        while winsA < 4 and winsB < 4:
            winner, _ = self.simulate_game(teamA, teamB)
            if winner == teamA:
                winsA += 1
            else:
                winsB += 1

        series_winner = teamA if winsA == 4 else teamB
        print(f"{round_name}: {teamA.name} vs {teamB.name} | Winner: {series_winner.name} ({winsA}-{winsB})")
        return series_winner

    # ---------------------------------------------------------
    # Gemini AI Methods
    # ---------------------------------------------------------
    def generate_playoff_hype(self, teams, client):
        print("[Gemini is generating playoff hype...]")

    def generate_finals_recap(self, winner, client):
        print(f"[Gemini is writing a recap for the {winner.name} victory...]")
