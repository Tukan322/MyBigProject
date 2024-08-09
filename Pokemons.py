class Pokemon:

    # Construct
    def __init__(self):
        self.base_speed = 0
        self.health = 0
        self.current_health = 0
        self.attack = 0
        self.normAttack = 0
        self.speed = 0
        self.level = 0
        self.workUpCountBuffed = 0

    # base Attack
    def Attack(self, poke):
        poke.current_health -= self.attack






