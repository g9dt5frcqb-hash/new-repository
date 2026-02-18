class Game:
    def __init__(self, teamA, teamB, winner, loser, scoreA=None, scoreB=None):
        self.teamA = teamA
        self.teamB = teamB
        self.winner = winner
        self.loser = loser
        self.scoreA = scoreA
        self.scoreB = scoreB

        # Gemini-ready summary placeholder
        self.summary = self.generate_placeholder_summary()


    def generate_placeholder_summary(self):
        return (
            f"{self.winner.name} defeated {self.loser.name}. "
            f"Strong performance from the winning side."
        )


    def get_summary(self):
        if self.scoreA is not None and self.scoreB is not None:
            return (
                f"{self.teamA.name} {self.scoreA} - "
                f"{self.teamB.name} {self.scoreB} | Winner: {self.winner.name}"
            )
        return f"{self.winner.name} defeated {self.loser.name}"
