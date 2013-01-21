from dies_roll import die6, die10
from weapons import sabre, great_club, sword, rapier, lance, two_sabres


class Character(object):
    def __init__(self, name, title, description, weapon, hp, attack, defense):
        self.name = name
        self.title = title
        self.description = description
        self.weapon = weapon
        self.hp = hp
        self.attack = attack
        self.defense = defense


""" Predefined opponents """
heavy = Character("Bruno", "heavily-armored knight", "", sword, 15, 4, 12)
cat = Character("Leonardo", "agile catling swashbuckler", "", rapier, 11, 7, 11)
rogue = Character("Ratty", "dirty fighting rogue", "", sabre, 15, 6, 9)
giant = Character("Ka-haak", "giant,slow but strong", "", great_club, 30, 4, 8)
amazon = Character("Sheila", "amazon lancer", "", lance, 13, 5, 10)
two_orc = Character("Grim and Grum", "two orcish raiders", "They are two, so they attack twice a round.", two_sabres, 16, 4, 9)
""" Predefined players """
random_character = Character("", "newbie adventurer", "", "random_weapon(self)", die6() + 10, die6() // 3 + 4, die6() // 3 + 9)
p_heavy = Character("Desmond", "heavily-armored knight", "", sword, 15, 4, 12)
p_cat = Character("Bubbles", "agile catling swashbuckler", "", rapier, 11, 7, 11)
p_rogue = Character("Louis", "dirty fighting rogue", "", sabre, 15, 6, 9)
p_giant = Character("Tul-duru", "giant,slow but strong", "", great_club, 30, 4, 8)
p_amazon = Character("Noelle", "amazon lancer", "", lance, 13, 5, 10)
p_two_orc = Character("Shargat and Gobrath", "two orcish raiders", "They are two, so they attack twice a round.", two_sabres, 12, 0, 4)
