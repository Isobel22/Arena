from dies_roll import die6, die10
from weapons import sabre, great_club, sword, rapier, lance, two_sabres

class Player(object):
	def __init__ (self, name, title, description, weapon, hp, attack, defense):
		self.name = name
		self.title = title
		self.description = description
		self.weapon = weapon
		self.hp = hp
		self.attack = attack
		self.defense = defense

		
class Opponent(object):
	def __init__ (self, name, title, description, weapon, hp, attack, defense):
		self.name = name
		self.title = title
		self.description = description
		self.weapon = weapon
		self.hp = hp
		self.attack = attack
		self.defense = defense
		
		

""" Predefined opponents """		
heavy = Opponent("Bruno", "heavily-armored knight", "", sword, 15, 4, 12)
cat = Opponent("Leonardo", "agile catling swashbuckler", "", rapier, 11, 7, 11)
rogue = Opponent("Ratty", "dirty fighting rogue", "", sabre, 15, 6, 9)
giant = Opponent("Ka-haak", "giant,slow but strong", "", great_club, 30, 4, 8)
amazon = Opponent("Sheila", "amazon lancer", "", lance, 13, 5, 10)
two_orc = Opponent("Grim and Grum", "two orcish raiders", "They are two, so they attack twice a round.", two_sabres, 16, 4, 9)
""" Predefined players """	
random_character = Player("","newbie adventurer", "", "random_weapon(self)", die6() + 10, die6() // 3 + 4, die6() // 3 + 9)
p_heavy = Player("Desmond", "heavily-armored knight", "", sword, 15, 4, 12)
p_cat = Player("Bubbles", "agile catling swashbuckler", "", rapier, 11, 7, 11)
p_rogue = Player("Louis", "dirty fighting rogue", "", sabre, 15, 6, 9)
p_giant = Player("Tul-duru", "giant,slow but strong", "", great_club, 30, 4, 8)
p_amazon = Player("Noelle", "amazon lancer", "", lance, 13, 5, 10)
p_two_orc = Player("Shargat and Gobrath", "two orcish raiders", "They are two, so they attack twice a round.", two_sabres, 12, 0, 4)

