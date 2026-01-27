import random

class SeasonSimulator:
    def __init__(self, teams, league_type):
        """
        teams: list of Team objects
        league_type: "NBA" or "NFL"
        """
        self.teams = teams
        self.league_type = league_type
        
        # Standings stored as {team_name: wins}
        self.standings = {team.name: 0 for team in teams}

    # ---------------------------------------------------------
    # Simulate a single game
    # ---------------------------------------------------------
    def simulate_game(self, teamA, teamB):
        """
        Returns: winner, loser
        """
        # Base ratings
        ratingA = teamA.team_overall + teamA.offense_rating + teamA.defense_rating + teamA.chemistry
        ratingB = teamB.team_overall + teamB.offense_rating + teamB.defense_rating + teamB.chemistry

        # Add randomness
        ratingA += random.randint(-10, 10)
        ratingB += random.randint(-10, 10)

        if ratingA > ratingB:
            teamA.record_game_result(win=True)
            teamB.record_game_result(win=False)
            return teamA, teamB
        else:
            teamA.record_game_result(win=False)
            teamB.record_game_result(win=True)
            return teamB, teamA

    # ---------------------------------------------------------
    # Generate a schedule
    # ---------------------------------------------------------
    def generate_schedule(self):
        schedule = []
        
        if self.league_type == "NBA":
            # NBA: 82 games (simplified version)
            for teamA in self.teams:
                for teamB in self.teams:
                    if teamA != teamB:
                        schedule.append((teamA, teamB))

        elif self.league_type == "NFL":
            # NFL: 17 games (simplified)
            for team in self.teams:
                opponents = random.sample([t for t in self.teams if t != team], 17)
                for opp in opponents:
                    schedule.append((team, opp))

        return schedule

    # ---------------------------------------------------------
    # Simulate the entire regular season
    # ---------------------------------------------------------
    def simulate_season(self):
        print("\n--- Regular Season Simulation Begins ---\n")

        schedule = self.generate_schedule()

        for game in schedule:
            teamA, teamB = game
            winner, loser = self.simulate_game(teamA, teamB)

            # Update standings
            self.standings[winner.name] += 1

        print("\n--- Regular Season Complete ---\n")
        self.print_standings()

    # ---------------------------------------------------------
    # Print standings
    # ---------------------------------------------------------
    def print_standings(self):
        sorted_standings = sorted(self.standings.items(), key=lambda x: x[1], reverse=True)
        for team_name, wins in sorted_standings:
            print(f"{team_name}: {wins} wins")

    # ---------------------------------------------------------
    # NBA Playoffs (best-of-7)
    # ---------------------------------------------------------
    def simulate_nba_playoffs(self):
        print("\n--- NBA Playoffs Begin ---\n")

        # Top 8 teams
        sorted_teams = sorted(self.teams, key=lambda t: t.wins, reverse=True)
        playoff_teams = sorted_teams[:8]

        # Bracket: 1v8, 2v7, 3v6, 4v5
        matchups = [
            (playoff_teams[0], playoff_teams[7]),
            (playoff_teams[1], playoff_teams[6]),
            (playoff_teams[2], playoff_teams[5]),
            (playoff_teams[3], playoff_teams[4]),
        ]

        winners = []
        for teamA, teamB in matchups:
            winners.append(self.best_of_seven(teamA, teamB))

        # Semifinals
        semi1 = self.best_of_seven(winners[0], winners[3])
        semi2 = self.best_of_seven(winners[1], winners[2])

        # Finals
        champion = self.best_of_seven(semi1, semi2)

        print(f"\n🏆 NBA Champion: {champion.name}\n")
        return champion

    # ---------------------------------------------------------
    # Best-of-7 series
    # ---------------------------------------------------------
    def best_of_seven(self, teamA, teamB):
        winsA = 0
        winsB = 0

        while winsA < 4 and winsB < 4:
            winner, _ = self.simulate_game(teamA, teamB)
            if winner == teamA:
                winsA += 1
            else:
                winsB += 1

        return teamA if winsA == 4 else teamB

    # ---------------------------------------------------------
    # NFL Playoffs (single elimination)
    # ---------------------------------------------------------
    def simulate_nfl_playoffs(self):
        print("\n--- NFL Playoffs Begin ---\n")

        # Top 7 teams
        sorted_teams = sorted(self.teams, key=lambda t: t.wins, reverse=True)
        playoff_teams = sorted_teams[:7]

        # #1 seed gets a bye
        bye_team = playoff_teams[0]
        wildcards = playoff_teams[1:]

        # Wild Card round
        winners = []
        for i in range(0, len(wildcards), 2):
            winner, _ = self.simulate_game(wildcards[i], wildcards[i+1])
            winners.append(winner)

        # Add bye team
        winners.append(bye_team)

        # Divisional round
        if len(winners) == 4:
            semi1, _ = self.simulate_game(winners[0], winners[3])
            semi2, _ = self.simulate_game(winners[1], winners[2])
        else:
            return None

        # Conference Championship
        superbowl_team, _ = self.simulate_game(semi1, semi2)

        print(f"\n🏆 Super Bowl Champion: {superbowl_team.name}\n")
        return superbowl_team

    # ---------------------------------------------------------
    # Simulate playoffs based on league type
    # ---------------------------------------------------------
    def simulate_playoffs(self):
        if self.league_type == "NBA":
            return self.simulate_nba_playoffs()
        else:
            return self.simulate_nfl_playoffs()
