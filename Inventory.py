import random


class Spell:
    def __init__(self, name, cost, dmg, types):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.type = types

    def generate_spell_damage(self):
        low = int(self.dmg) - 5
        high = int(self.dmg) + 5
        return random.randrange(low, high)
