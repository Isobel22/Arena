from dies_roll import die6, die10


class Weapon(object):
    def __init__(self, name, attack, damage_string, damage_roll, damage_bonus):
        self.name = name
        self.attack = attack
        self.damage_string = damage_string
        self.damage_roll = damage_roll
        self.damage_bonus = damage_bonus

    def damage_dealt(self):
        """Return randomly rolled damage of weapon"""
        return self.damage_roll() + self.damage_bonus

""" Predefined weapons """
sabre = Weapon("Sabre", 1, "1d6 (1-6)", die6, 0)
great_club = Weapon("Great club", -1, "1d10 + 2 (3-12)", die10, 2)
sword = Weapon("Sword", 0, "1d6 + 1 (2-7)", die6, 1)
rapier = Weapon("Rapier", 2, "1d6 - 1 (0-5)", die6, -1)
lance = Weapon("Lance", 0, "1d10 - 1 (0-9)", die10, -1)
two_sabres = Weapon("Two sabres", 1, "1d6 + 1d6 (2-12)", die6, 0)  # still not working properly
