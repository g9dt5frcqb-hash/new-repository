class NBAPlayer:
    def __init__(
        self,
        name,
        position,
        team,
        height,
        weight,
        age,
        overall,
        potential,
        archetype,
        badges=None,
        contract=None
    ):
        self.name = name
        self.position = position
        self.team = team
        self.height = height
        self.weight = weight
        self.age = age
        self.overall = overall
        self.potential = potential
        self.archetype = archetype
        self.badges = badges if badges else []
        self.contract = contract if contract else {}
