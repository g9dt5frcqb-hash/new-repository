class League:
    def __init__(self, league_type, teams):
        """
        league_type: "NBA" or "NFL"
        teams: list of Team objects
        """
        self.league_type = league_type
        self.teams = teams
        
        # Core systems (initialized later)
        self.draft_class = None
        self.free_agency = None
        self.trade_engine = None
        self.season_simulator = None
        
        # Track league year
        self.year = 1

    # ---------------------------------------------------------
    # Initialize Draft Class
    # ---------------------------------------------------------
    def create_draft_class(self, num_prospects=60):
        from draft_class import DraftClass
        self.draft_class = DraftClass(
            league_type=self.league_type,
            teams=self.teams,
            num_prospects=num_prospects
        )

    # ---------------------------------------------------------
    # Initialize Free Agency
    # ---------------------------------------------------------
    def create_free_agency(self, free_agents):
        from free_agency import FreeAgency
        self.free_agency = FreeAgency(free_agents)

    # ---------------------------------------------------------
    # Initialize Trade Engine
    # ---------------------------------------------------------
    def create_trade_engine(self):
        from trade_engine import TradeEngine
        self.trade_engine = TradeEngine()

    # ---------------------------------------------------------
    # Initialize Season Simulator
    # ---------------------------------------------------------
    def create_season_simulator(self):
        from season_simulator import SeasonSimulator
        self.season_simulator = SeasonSimulator(self.teams, self.league_type)

    # ---------------------------------------------------------
    # Start the draft
    # ---------------------------------------------------------
    def start_draft(self):
        if not self.draft_class:
            print("Draft class not created yet.")
            return
        
        print(f"\n--- {self.league_type} Draft Begins ---\n")
        
        for team in self.draft_class.draft_order:
            best_player = self.draft_class.get_best_available()
            self.draft_class.draft_player(team, best_player)
            print(f"{team.name} selects {best_player.name} ({best_player.position})")

    # ---------------------------------------------------------
    # Start free agency
    # ---------------------------------------------------------
    def start_free_agency(self):
        if not self.free_agency:
            print("Free agency not created yet.")
            return
        
        print(f"\n--- {self.league_type} Free Agency Begins ---\n")
        self.free_agency.run_free_agency(self.teams)

    # ---------------------------------------------------------
    # Start the season
    # ---------------------------------------------------------
    def start_season(self):
        if not self.season_simulator:
            print("Season simulator not created yet.")
            return
        
        print(f"\n--- {self.league_type} Season {self.year} Begins ---\n")
        self.season_simulator.simulate_season()
        self.season_simulator.simulate_playoffs()

    # ---------------------------------------------------------
    # Hire a coach
    # ---------------------------------------------------------
    def hire_coach(self, team, coach):
        team.hire_coach(coach)
        print(f"{team.name} hires {coach.name} ({coach.coaching_style})")

    # ---------------------------------------------------------
    # Fire a coach
    # ---------------------------------------------------------
    def fire_coach(self, team):
        if team.coach:
            print(f"{team.name} fires {team.coach.name}")
            team.fire_coach()
        else:
            print(f"{team.name} has no coach to fire.")

    # ---------------------------------------------------------
    # Save league state (placeholder)
    # ---------------------------------------------------------
    def save_league_state(self):
        """
        You can expand this later to save:
        - rosters
        - standings
        - draft picks
        - coaches
        - free agents
        """
        print("League state saved (placeholder).")

    # ---------------------------------------------------------
    # Summary for menus
    # ---------------------------------------------------------
    def get_league_summary(self):
        return (
            f"{self.league_type} League — Year {self.year}\n"
            f"Teams: {len(self.teams)}\n"
            f"Draft Class Ready: {self.draft_class is not None}\n"
            f"Free Agency Ready: {self.free_agency is not None}\n"
            f"Season Simulator Ready: {self.season_simulator is not None}"
        )
