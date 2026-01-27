class Team:
    def __init__(self, name, conference, division, salary_cap=120_000_000):
        self.name = name
        self.conference = conference
        self.division = division
        
        # Roster + Coach
        self.roster = []          # list of Player objects
        self.coach = None         # Coach object
        
        # Salary cap
        self.salary_cap = salary_cap
        self.cap_space = salary_cap
        
        # Team performance attributes
        self.offense_rating = 50
        self.defense_rating = 50
        self.player_development = 50
        self.chemistry = 50
        
        # Season performance
        self.wins = 0
        self.losses = 0
        
        # Draft picks (list of integers or Pick objects)
        self.draft_picks = []
        
        # Team status (affects FA interest + trade logic)
        self.status = "Unknown"   # Contender, Playoff Team, Mid, Rebuild, Tank
    
    # ---------------------------------------------------------
    # Add a player to the roster
    # ---------------------------------------------------------
    def add_player(self, player):
        self.roster.append(player)
        player.team = self.name
        self.update_cap_space()
        self.calculate_team_overall()
        self.update_chemistry()
    
    # ---------------------------------------------------------
    # Remove a player from the roster
    # ---------------------------------------------------------
    def remove_player(self, player):
        if player in self.roster:
            self.roster.remove(player)
            player.team = None
            self.update_cap_space()
            self.calculate_team_overall()
            self.update_chemistry()
    
    # ---------------------------------------------------------
    # Update salary cap space
    # ---------------------------------------------------------
    def update_cap_space(self):
        total_salary = sum([p.contract_salary for p in self.roster])
        self.cap_space = self.salary_cap - total_salary
    
    # ---------------------------------------------------------
    # Calculate team overall rating
    # ---------------------------------------------------------
    def calculate_team_overall(self):
        if not self.roster:
            self.team_overall = 0
            return
        
        # Convert A–F grades to numbers
        grade_map = {"A": 95, "B": 85, "C": 75, "D": 65, "F": 55}
        
        ratings = []
        for player in self.roster:
            ratings.append(grade_map.get(player.overall_grade, 70))
        
        # Average rating
        self.team_overall = sum(ratings) // len(ratings)
    
    # ---------------------------------------------------------
    # Update chemistry based on roster stability + coach
    # ---------------------------------------------------------
    def update_chemistry(self):
        base = 50
        
        # More players = more chaos
        base -= max(0, len(self.roster) - 12)
        
        # Good coach boosts chemistry
        if self.coach:
            base += self.coach.chemistry_boost
        
        # Clamp between 0–100
        self.chemistry = max(0, min(100, base))
    
    # ---------------------------------------------------------
    # Assign a coach to the team
    # ---------------------------------------------------------
    def hire_coach(self, coach):
        self.coach = coach
        coach.apply_coach_effects(self)
    
    # ---------------------------------------------------------
    # Fire the current coach
    # ---------------------------------------------------------
    def fire_coach(self):
        self.coach = None
        # Reset boosts
        self.offense_rating = 50
        self.defense_rating = 50
        self.player_development = 50
        self.chemistry = 50
    
    # ---------------------------------------------------------
    # Update team status (affects FA interest + trades)
    # ---------------------------------------------------------
    def update_team_status(self):
        if self.team_overall >= 90:
            self.status = "Contender"
        elif self.team_overall >= 80:
            self.status = "Playoff Team"
        elif self.team_overall >= 70:
            self.status = "Mid"
        elif self.team_overall >= 60:
            self.status = "Rebuild"
        else:
            self.status = "Tank"
    
    # ---------------------------------------------------------
    # Record a win or loss
    # ---------------------------------------------------------
    def record_game_result(self, win=True):
        if win:
            self.wins += 1
        else:
            self.losses += 1
    
    # ---------------------------------------------------------
    # Reset record for new season
    # ---------------------------------------------------------
    def reset_record(self):
        self.wins = 0
        self.losses = 0
    
    # ---------------------------------------------------------
    # Summary for menus
    # ---------------------------------------------------------
    def get_summary(self):
        return (
            f"{self.name} — {self.wins}-{self.losses}, "
            f"Overall: {self.team_overall}, "
            f"Chemistry: {self.chemistry}, "
            f"Status: {self.status}"
        )
