class League:
    def __init__(self, league_type, teams):
        self.league_type = league_type
        self.teams = teams  # This stores the list from main.py
        self.year = 1
        
        # System placeholders
        self.draft_class = None
        self.season_simulator = None
        self.trade_engine = None

    def create_draft_class(self, num_prospects=60):
        from draft_class import DraftClass
        # We pass self.teams here so DraftClass can copy it
        self.draft_class = DraftClass(self.league_type, self.teams, num_prospects)

    def create_trade_engine(self):
        from trade_engine import TradeEngine
        self.trade_engine = TradeEngine()

    def create_season_simulator(self):
        from season_simulator import SeasonSimulator
        self.season_simulator = SeasonSimulator(self.teams, self.league_type)

    def start_draft(self):
        if not self.draft_class:
            print("No draft class found!")
            return
        
        print(f"\n--- {self.league_type} Draft Begins ---")
        for team in self.draft_class.draft_order:
            player = self.draft_class.get_best_available()
            if player:
                self.draft_class.draft_player(team, player)
                print(f"{team.name} drafted {player.name} ({player.position})")

    def start_season(self, gemini_client=None):
        if self.season_simulator:
            self.season_simulator.simulate_season()
            self.season_simulator.simulate_playoffs(gemini_client=gemini_client)


    