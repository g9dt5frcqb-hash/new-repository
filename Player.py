import random

class Player:
    def __init__(
        self,
        name,
        position,
        age,
        overall_grade,
        skill_grade,
        potential_grade,
        contract_years=1,
        contract_salary=1_000_000,
        interest_level="Medium"
    ):
        self.name = name
        self.position = position
        self.age = age
        
        # Grades (A–F)
        self.overall_grade = overall_grade
        self.skill_grade = skill_grade
        self.potential_grade = potential_grade
        
        # Contract
        self.contract_years = contract_years
        self.contract_salary = contract_salary
        
        # Free agency interest
        self.interest_level = interest_level  # High / Medium / Low
        
        # Team assignment
        self.team = None
        
        # Scouting report (Gemini later)
        self.scouting_report = "No scouting report yet."
        
        # Hidden development curve (0.5–1.5)
        self.development_curve = round(random.uniform(0.5, 1.5), 2)

    # ---------------------------------------------------------
    # Convert A–F grades to numeric values
    # ---------------------------------------------------------
    def grade_to_value(self, grade):
        mapping = {
            "A": 95,
            "B": 85,
            "C": 75,
            "D": 65,
            "F": 55
        }
        return mapping.get(grade, 70)

    # ---------------------------------------------------------
    # Calculate trade value
    # ---------------------------------------------------------
    def calculate_value(self):
        base = self.grade_to_value(self.overall_grade)
        potential = self.grade_to_value(self.potential_grade)
        
        # Younger players are more valuable
        age_factor = max(0.5, (35 - self.age) / 35)
        
        return int((base * 0.7 + potential * 0.3) * age_factor)

    # ---------------------------------------------------------
    # Player development after a season
    # ---------------------------------------------------------
    def develop(self, team_development_rating):
        """
        team_development_rating: from Team.player_development (0–100)
        """
        # Convert A–F to numeric
        current = self.grade_to_value(self.overall_grade)
        potential = self.grade_to_value(self.potential_grade)
        
        # Growth amount depends on:
        # - potential
        # - team development
        # - hidden development curve
        growth_chance = (potential / 100) * (team_development_rating / 100) * self.development_curve
        
        # Growth range: 0–5 points
        growth = int(growth_chance * random.randint(0, 5))
        
        new_rating = min(99, current + growth)
        
        # Convert back to A–F
        self.overall_grade = self.numeric_to_grade(new_rating)

    # ---------------------------------------------------------
    # Convert numeric rating back to A–F
    # ---------------------------------------------------------
    def numeric_to_grade(self, rating):
        if rating >= 90:
            return "A"
        if rating >= 80:
            return "B"
        if rating >= 70:
            return "C"
        if rating >= 60:
            return "D"
        return "F"

    # ---------------------------------------------------------
    # Update free agency interest based on team status
    # ---------------------------------------------------------
    def update_interest(self, team_status):
        if team_status == "Contender":
            self.interest_level = "High"
        elif team_status == "Playoff Team":
            self.interest_level = "Medium"
        else:
            self.interest_level = "Low"

    # ---------------------------------------------------------
    # Gemini-ready scouting report placeholder
    # ---------------------------------------------------------
    def generate_placeholder_report(self):
        self.scouting_report = (
            f"{self.name} is a {self.position} with {self.overall_grade}-level ability "
            f"and {self.potential_grade} potential. Shows flashes of {self.skill_grade}-grade skills."
        )

    # ---------------------------------------------------------
    # Summary for menus
    # ---------------------------------------------------------
    def get_summary(self):
        return (
            f"{self.name} — {self.position}, OVR: {self.overall_grade}, "
            f"Skill: {self.skill_grade}, POT: {self.potential_grade}, "
            f"Age: {self.age}, Team: {self.team}"
        )
