from random import random


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
        self.name = "Furfrou"

    # base Attack
    def Attack(self, poke):
        print(self.name, "использует обычную атаку")
        hp_before_attack = poke.current_health
        poke.current_health -= self.attack
        print("Нанесено", hp_before_attack - poke.current_health, "урона")


class Furfrou(Pokemon):

    base_health = 25
    base_attack = 8
    base_speed = 4
    cd_rest = 3
    cd_workup = 5
    workup_multi = 1.5

    def __init__(self, level=1):
        super().__init__()
        self.now_cd_rest = 3
        self.now_cd_workup = 5
        self.level = level
        self.health = self.base_health + self.base_health*(level/4)
        self.current_health = self.health
        self.attack = self.base_attack + self.base_attack*(level/4)
        self.norm_attack = self.attack
        self.speed = self.base_speed
        self.norm_speed = self.speed

    def workup(self):
        print("Покемон", self.name, "использовал усиление")
        self.attack = self.attack * self.workup_multi
        self.workUpCountBuffed = 3
        print("Текущее значение атаки:", self.attack)
        self.now_cd_workup = 0

    def rest(self):
        before_heal = self.current_health
        print("Покемон", self.name, "использовал лечение")
        if self.current_health < self.health / 2:
            self.current_health += self.health/2
        else:
            self.current_health = self.health
        print(self.name, "восстановил", self.current_health - before_heal, "здоровья")

    def auto_battle(self, poke):
        attacked = False

        if not attacked:
            if self.now_cd_workup >= self.cd_workup:
                if random() < 0.6:
                    self.workup()
                    attacked = True

        if not attacked:
            if self.now_cd_rest >= self.cd_rest:
                if random() < 0.4:
                    self.rest()
                    attacked = True

        if not attacked:
            self.Attack(poke)





