import random

class FreeAgency:
    def __init__(self, free_agents):
        """
        free_agents: list of Player objects
        """
        self.free_agents = free_agents

    # ---------------------------------------------------------
    # Adjust offer needed based on interest level
    # ---------------------------------------------------------
    def calculate_offer_needed(self, player, team):
        base_value = player.calculate_value() * 100_000  # convert to salary

        # Team status affects interest
        player.update_interest(team.status)

        if player.interest_level == "High":
            return int(base_value * 0.9)   # cheaper
        elif player.interest_level == "Medium":
            return int(base_value * 1.0)   # normal
        else:
            return int(base_value * 1.2)   # expensive

    # ---------------------------------------------------------
    # Attempt to sign a player
    # ---------------------------------------------------------
    def attempt_sign(self, player, team, offer_amount):
        required = self.calculate_offer_needed(player, team)

        if offer_amount >= required:
            # Successful signing
            team.add_player(player)
            self.free_agents.remove(player)
            return True, self.generate_negotiation_dialogue(player, True)
        else:
            # Failed signing
            return False, self.generate_negotiation_dialogue(player, False)

    # ---------------------------------------------------------
    # Gemini-ready negotiation dialogue
    # ---------------------------------------------------------
    def generate_negotiation_dialogue(self, player, success):
        if success:
            return (
                f"{player.name}: 'I like the direction your team is going. "
                f"I'm excited to sign this deal and get to work.'"
            )
        else:
            return (
                f"{player.name}: 'I appreciate the offer, but it's not enough "
                f"to convince me to join your team right now.'"
            )

    # ---------------------------------------------------------
    # Run free agency for all teams (simple version)
    # ---------------------------------------------------------
    def run_free_agency(self, teams):
        """
        Simple version:
        - Each team tries to sign 1–2 players
        - You can expand this later for full control
        """
        print("\n--- Free Agency Simulation ---\n")

        for team in teams:
            if not self.free_agents:
                break

            # Each team tries to sign 1 random free agent
            target = random.choice(self.free_agents)
            offer = self.calculate_offer_needed(target, team)

            success, dialogue = self.attempt_sign(target, team, offer)

            if success:
                print(f"{team.name} signs {target.name} for ${offer:,}")
            else:
                print(f"{team.name} failed to sign {target.name}")

            print(dialogue)
            print()
