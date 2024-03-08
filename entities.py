from dice import die
from functools import total_ordering

initiative_dice = 20

@total_ordering
class Creature:

    def __init__(self, name, init_mod):
        self.init_mod = init_mod
        self.name = name
        self.initiative = 0

    def __repr__(self):
        return f"Name:{self.name} Init:{self.initiative}"

    @staticmethod
    def _is_creature(other):
        return hasattr(other, 'initiative')

    def __lt__(self, other):
        if not self._is_creature(other):
            return NotImplemented
        mine = self.initiative + (self.init_mod / 100)
        theirs = other.initiative + (other.init_mod / 100)
        return mine < theirs

    def __eq__(self, other):
        if not self._is_creature(other):
            return NotImplemented
        mine = self.initiative + (self.init_mod / 100)
        theirs = other.initiative + (other.init_mod / 100)
        return mine == theirs


class Player(Creature):

    def __init__(self, name, init_mod, initiative):
        super().__init__(name, init_mod)
        self.initiative = initiative
        print(self)

    def __repr__(self):
        return f'Name: {self.name}\nMod: {self.init_mod}\nInitiative: {self.initiative}'


class Monster(Creature):

    def __init__(self, name, init_mod, hit_points):
        super().__init__(name, init_mod)
        self.current_hit_points = hit_points
        self.max_hit_points = hit_points
        self.temp_hit_points = 0

    def damage(self, amount):
        # deals damage to the creature, few cases to consider

        if self.temp_hit_points >= amount:  # 1, temp HP covers all damage
            self.temp_hit_points -= amount

        elif self.temp_hit_points:  # 2 temp HP covers some of the damage, and is removed
            amount -= self.temp_hit_points
            self.temp_hit_points = 0

        self.current_hit_points -= amount

    def heal(self, amount):
        # restores health to the creature, does not exceed HP max
        self.current_hit_points += amount
        if self.current_hit_points > self.max_hit_points:
            self.current_hit_points = self.max_hit_points

    def add_temp(self, amount):
        # Adds temp HP to creature, does nothing if new amount does not exceed current value
        if amount > self.temp_hit_points:
            self.temp_hit_points = amount

    def __repr__(self):
        return f"Name: {self.name}\nInit: {self.initiative}\nHP: {self.current_hit_points}/{self.max_hit_points}"

    def roll_initiative(self):
        self.initiative = die(initiative_dice) + self.init_mod
