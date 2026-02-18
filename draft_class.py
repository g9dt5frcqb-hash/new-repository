import random

class DraftClass:
    def __init__(self, league_type, teams, num_prospects=60):
        self.league_type = league_type
        self.teams = teams
        self.num_prospects = num_prospects
        self.prospects = []
        self.draft_order = []
        
        # Order matters: check teams first, then generate players
        self.randomize_draft_order()
        self.generate_prospects()

    def randomize_draft_order(self):
        if self.teams is not None:
            self.draft_order = self.teams.copy()
            random.shuffle(self.draft_order)
        else:
            print("Error: DraftClass received no teams!")
            self.draft_order = []

    def get_position_pool(self):
        l_type = str(self.league_type).upper()
        if l_type == "NBA":
            return ["PG", "SG", "SF", "PF", "C"]
        return ["ATH"]

    def generate_prospects(self):
        from Player import Player
        positions = self.get_position_pool()
        for _ in range(self.num_prospects):
            p = Player(
                name=f"{random.choice(['Malik', 'Trey', 'Zion'])} {random.choice(['Smith', 'West', 'Hill'])}",
                position=random.choice(positions),
                age=random.randint(18, 22),
                overall_grade=random.choice(["A", "B", "C"]),
                skill_grade="B",
                potential_grade="A",
                contract_years=4,
                contract_salary=random.randint(2000000, 5000000)
            )
            self.prospects.append(p)

    def get_best_available(self):
        if not self.prospects: return None
        grade_map = {"A": 3, "B": 2, "C": 1}
        return max(self.prospects, key=lambda p: grade_map.get(p.overall_grade, 0))

    def draft_player(self, team, player):
        if player in self.prospects:
            self.prospects.remove(player)
            team.add_player(player)
            return True
        return False