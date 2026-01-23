class TradeEngine:
    def __init__(self):
        pass

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
    # Calculate value of a single asset (player or pick)
    # ---------------------------------------------------------
    def calculate_asset_value(self, asset):
        # If it's a Player object
        if hasattr(asset, "overall_grade"):
            base = self.grade_to_value(asset.overall_grade)
            potential = self.grade_to_value(asset.potential_grade)
            age_factor = max(0.5, (35 - asset.age) / 35)  # younger = more value
            return int((base * 0.7 + potential * 0.3) * age_factor)

        # If it's a draft pick (represented as an integer)
        if isinstance(asset, int):
            # Lower pick number = more valuable
            return max(20, 100 - (asset * 2))

        return 0

    # ---------------------------------------------------------
    # Evaluate a trade between two teams
    # ---------------------------------------------------------
    def evaluate_trade(self, teamA_assets, teamB_assets, teamA, teamB):
        """
        teamA_assets = what Team A is offering
        teamB_assets = what Team B is offering
        """

        # Calculate total value for each side
        value_A = sum([self.calculate_asset_value(a) for a in teamA_assets])
        value_B = sum([self.calculate_asset_value(b) for b in teamB_assets])

        # Adjust based on team status
        status_modifiers = {
            "Contender": 1.1,
            "Playoff Team": 1.0,
            "Mid": 0.95,
            "Rebuild": 0.9,
            "Tank": 0.85
        }

        value_A *= status_modifiers.get(teamA.status, 1.0)
        value_B *= status_modifiers.get(teamB.status, 1.0)

        # Coach effect (Personnel Developer makes trades easier)
        if teamB.coach and teamB.coach.coaching_style == "Personnel Developer":
            value_A *= 1.05  # Team B is more willing to accept

        # Ratio determines trade bar
        ratio = value_A / value_B if value_B > 0 else 0

        if ratio >= 1.1:
            bar_color = "GREEN"
        elif 0.8 <= ratio < 1.1:
            bar_color = "YELLOW"
        else:
            bar_color = "RED"

        explanation = self.generate_trade_dialogue(bar_color, teamA, teamB, ratio)

        return {
            "teamA_value": value_A,
            "teamB_value": value_B,
            "ratio": ratio,
            "bar_color": bar_color,
            "explanation": explanation
        }

    # ---------------------------------------------------------
    # Madden-style trade dialogue
    # ---------------------------------------------------------
    def generate_trade_dialogue(self, bar_color, teamA, teamB, ratio):
        if bar_color == "GREEN":
            return (
                f"{teamB.name} front office: 'This deal works great for us. "
                f"We’re ready to accept immediately.'"
            )

        elif bar_color == "YELLOW":
            return (
                f"{teamB.name} GM: 'We’re close, but not quite there. "
                f"Sweeten the offer just a bit and we can make this happen.'"
            )

        else:  # RED
            return (
                f"{teamB.name} GM: 'We can’t justify this trade. "
                f"The value just isn’t close enough for us to consider it.'"
            )
