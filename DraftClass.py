import random

class DraftClass:
    def __init__(self, league_type, teams, num_prospects=60):
        """
        league_type: "NBA" or "NFL"
        teams: list of Team objects
        num_prospects: how many players to generate
        """
        self.league_type = league_type
        self.teams = teams
        self.num_prospects = num_prospects
        
        self.prospects = []       # list of Player objects
        self.draft_order = []     # randomized list of teams
        
        self.generate_prospects()
        self.randomize_draft_order()

    # ---------------------------------------------------------
    # Position pools for NBA + NFL
    # ---------------------------------------------------------
    def get_position_pool(self):
        if self.league_type == "NBA":
            return ["PG", "SG", "SF", "PF", "C"]
        
        if self.league_type == "NFL":
            return [
                "QB", "RB", "WR", "TE",
                "OT", "OG", "C",
                "DE", "DT", "LB",
                "CB", "S",
                "K", "P"
            ]
        
        return []

    # ---------------------------------------------------------
    # Generate A–F grades
    # ---------------------------------------------------------
    def random_grade(self):
        return random.choice(["A", "B", "C", "D", "F"])

    # ---------------------------------------------------------
    # Generate draft prospects
    # ---------------------------------------------------------
    def generate_prospects(self):
        from player import Player  # You will create this class next
        
        positions = self.get_position_pool()
        
        for _ in range(self.num_prospects):
            name = self.generate_random_name()
            position = random.choice(positions)
            age = random.randint(18, 23)
            
            overall = self.random_grade()
            skill = self.random_grade()
            potential = self.random_grade()
            
            # Create Player object
            p = Player(
                name=name,
                position=position,
                age=age,
                overall_grade=overall,
                skill_grade=skill,
                potential_grade=potential,
                contract_years=4,
                contract_salary=random.randint(3_000_000, 8_000_000)
            )
            
            # Placeholder scouting report (Gemini later)
            p.scouting_report = self.generate_placeholder_report(p)
            
            self.prospects.append(p)

    # ---------------------------------------------------------
    # Random name generator
    # ---------------------------------------------------------
    def generate_random_name(self):
        first_names = ["Malik", "Jordan", "Trey", "Jalen", "Marcus", "Darius", "Elijah", "Tyrese", "Kaden", "Zion"]
        last_names = ["Johnson", "Williams", "Brown", "Davis", "Miller", "Jackson", "Thompson", "Anderson", "Moore", "Harris"]
        return f"{random.choice(first_names)} {random.choice(last_names)}"

    # ---------------------------------------------------------
    # Placeholder scouting report (Gemini later)
    # ---------------------------------------------------------
    def generate_placeholder_report(self, player):
        return (
            f"{player.name} is a {player.position} with {player.overall_grade}-level ability "
            f"and {player.potential_grade} potential. Shows flashes of strong {player.skill_grade}-grade skills."
        )

    # ---------------------------------------------------------
    # Randomize draft order
    # ---------------------------------------------------------
    def randomize_draft_order(self):
        self.draft_order = self.teams.copy()
        random.shuffle(self.draft_order)

    # ---------------------------------------------------------
    # Get best available prospect
    # ---------------------------------------------------------
    def get_best_available(self):
        # Convert A–F to numeric
        grade_map = {"A": 95, "B": 85, "C": 75, "D": 65, "F": 55}
        
        if not self.prospects:
            return None
        
        return max(self.prospects, key=lambda p: grade_map[p.overall_grade])

    # ---------------------------------------------------------
    # Team selects a player
    # ---------------------------------------------------------
    def draft_player(self, team, player):
        if player in self.prospects:
            self.prospects.remove(player)
            team.add_player(player)
            return True
        return False

    # ---------------------------------------------------------
    # Summary for menus
    # ---------------------------------------------------------
    def get_prospect_list(self):
        return [
            f"{p.name} — {p.position}, OVR: {p.overall_grade}, POT: {p.potential_grade}"
            for p in self.prospects
        ]
