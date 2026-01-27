class Pick:
    def __init__(self, round_number, pick_number, original_team):
        self.round_number = round_number
        self.pick_number = pick_number
        self.original_team = original_team  # team that originally owned the pick

    # ---------------------------------------------------------
    # Convert pick to a numeric value for trades
    # ---------------------------------------------------------
    def calculate_value(self):
        # Early picks are worth more
        base_value = max(20, 100 - (self.pick_number * 2))

        # Round 1 picks are more valuable
        if self.round_number == 1:
            base_value *= 1.5
        elif self.round_number == 2:
            base_value *= 1.0
        else:
            base_value *= 0.7

        return int(base_value)

    # ---------------------------------------------------------
    # Summary for menus
    # ---------------------------------------------------------
    def get_summary(self):
        return f"Round {self.round_number}, Pick {self.pick_number} (via {self.original_team})"
