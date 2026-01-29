import random

class Coach:
    def __init__(self, name, age, years_experience, coaching_style,
                 past_teams=None, past_records=None,
                 contract_years=3, contract_salary=5_000_000):
        
        self.name = name
        self.age = age
        self.years_experience = years_experience
        
        # Coaching history
        self.past_teams = past_teams if past_teams else []
        self.past_records = past_records if past_records else []
        self.career_wins = sum([record[0] for record in self.past_records])
        self.career_losses = sum([record[1] for record in self.past_records])
        
        # Style
        self.coaching_style = coaching_style
        
        # Impact ratings (generated based on style)
        self.offense_boost = 0
        self.defense_boost = 0
        self.development_boost = 0
        self.chemistry_boost = 0
        self._assign_style_boosts()
        
        # Contract
        self.contract_years = contract_years
        self.contract_salary = contract_salary
        
        # Gemini-generated bio (placeholder)
        self.bio = "Bio not generated yet."
    
    # ---------------------------------------------------------
    # Assign boosts based on coaching style
    # ---------------------------------------------------------
    def _assign_style_boosts(self):
        if self.coaching_style == "Offensive Mastermind":
            self.offense_boost = random.randint(5, 10)
            self.defense_boost = random.randint(0, 4)
            self.development_boost = random.randint(1, 5)
            self.chemistry_boost = random.randint(1, 5)

        elif self.coaching_style == "Defensive Mastermind":
            self.offense_boost = random.randint(0, 4)
            self.defense_boost = random.randint(5, 10)
            self.development_boost = random.randint(1, 5)
            self.chemistry_boost = random.randint(1, 5)

        elif self.coaching_style == "Player Developer":
            self.offense_boost = random.randint(1, 5)
            self.defense_boost = random.randint(1, 5)
            self.development_boost = random.randint(6, 10)
            self.chemistry_boost = random.randint(3, 7)

        elif self.coaching_style == "Personnel Developer":
            self.offense_boost = random.randint(1, 5)
            self.defense_boost = random.randint(1, 5)
            self.development_boost = random.randint(1, 5)
            self.chemistry_boost = random.randint(6, 10)

    # ---------------------------------------------------------
    # Apply coach effects to a team
    # ---------------------------------------------------------
    def apply_coach_effects(self, team):
        team.offense_rating += self.offense_boost
        team.defense_rating += self.defense_boost
        team.player_development += self.development_boost
        team.chemistry += self.chemistry_boost

    # ---------------------------------------------------------
    # Generate a Gemini bio (placeholder)
    # ---------------------------------------------------------
    def generate_bio(self, gemini_client=None):
        if gemini_client is None:
            self.bio= ""
            return
        
        prompt = f"Write a short coaching bio for a {self.coaching_style} coach named {self.name}."
        response = gemini_client.generate_content(prompt)
        self.bio = response.text
    # ---------------------------------------------------------
    # Calculate coach value (used for hiring/firing logic)
    # ---------------------------------------------------------
    def calculate_coach_value(self):
        style_score = (
            self.offense_boost +
            self.defense_boost +
            self.development_boost +
            self.chemistry_boost
        )
        experience_score = self.years_experience * 2
        record_score = self.career_wins - self.career_losses
        
        return style_score + experience_score + record_score

    # ---------------------------------------------------------
    # Update experience after a season
    # ---------------------------------------------------------
    def update_experience(self):
        self.years_experience += 1
        self.age += 1

    # ---------------------------------------------------------
    # Record a season result
    # ---------------------------------------------------------
    def record_season_result(self, team_name, wins, losses):
        self.past_teams.append(team_name)
        self.past_records.append((wins, losses))
        self.career_wins += wins
        self.career_losses += losses

    # ---------------------------------------------------------
    # Summary for menus
    # ---------------------------------------------------------
    def get_summary(self):
        return (
            f"{self.name} — {self.years_experience} years exp, "
            f"{self.coaching_style}, Career Record: "
            f"{self.career_wins}-{self.career_losses}"
        )
