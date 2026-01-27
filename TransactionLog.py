class TransactionLog:
    def __init__(self):
        self.entries = []

    # ---------------------------------------------------------
    # Add a log entry
    # ---------------------------------------------------------
    def add_entry(self, text):
        self.entries.append(text)

    # ---------------------------------------------------------
    # Log a trade
    # ---------------------------------------------------------
    def log_trade(self, teamA, teamB, assetsA, assetsB):
        entry = (
            f"TRADE: {teamA.name} traded {', '.join(a.name if hasattr(a, 'name') else a.get_summary() for a in assetsA)} "
            f"to {teamB.name} for "
            f"{', '.join(b.name if hasattr(b, 'name') else b.get_summary() for b in assetsB)}."
        )
        self.add_entry(entry)

    # ---------------------------------------------------------
    # Log a signing
    # ---------------------------------------------------------
    def log_signing(self, team, player, salary):
        entry = f"SIGNING: {team.name} signed {player.name} for ${salary:,}."
        self.add_entry(entry)

    # ---------------------------------------------------------
    # Log a release
    # ---------------------------------------------------------
    def log_release(self, team, player):
        entry = f"RELEASE: {team.name} released {player.name}."
        self.add_entry(entry)

    # ---------------------------------------------------------
    # Log a draft pick
    # ---------------------------------------------------------
    def log_draft_pick(self, team, player, pick):
        entry = (
            f"DRAFT: {team.name} selected {player.name} "
            f"with {pick.get_summary()}."
        )
        self.add_entry(entry)

    # ---------------------------------------------------------
    # Log a coaching change
    # ---------------------------------------------------------
    def log_coach_change(self, team, coach, action):
        entry = f"COACH: {team.name} {action} {coach.name} ({coach.coaching_style})."
        self.add_entry(entry)

    # ---------------------------------------------------------
    # Log a game result
    # ---------------------------------------------------------
    def log_game(self, game):
        entry = f"GAME: {game.get_summary()}"
        self.add_entry(entry)

    # ---------------------------------------------------------
    # Print all logs
    # ---------------------------------------------------------
    def print_log(self):
        print("\n--- TRANSACTION LOG ---\n")
        for entry in self.entries:
            print(entry)
