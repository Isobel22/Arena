#Arena - combat turn-based game

from sys import exit
from dies_roll import die6, die10
from characters import heavy, cat, rogue, giant, amazon, two_orc, random_character, p_heavy, p_cat, p_rogue, p_giant, p_amazon, p_two_orc
from weapons import sabre, great_club, sword, rapier, lance, two_sabres
from fight_style import standard, aggressive, defensive, strong, furious, parry, after_parry, after_furious

class Arena(object):
	
	def __init__ (self, player_name):
		self.player_name = player_name  #do I need this???
	
	def menu(self):
		"""main options"""
		chosen_menu = '1'
		while chosen_menu not in ('2', '3'):
			print "-------------------------------\n         A*R*E*N*A !!!   \nTurn-based battle game by Misa\n-------------------------------"
			print "1: PLAY THE GAME\n2: GAME RULES\n3: EXIT:"
			chosen_menu = raw_input("> ")
			if chosen_menu == "1":
				return my_game.play()
			elif chosen_menu == "2":
				return my_game.rules()
	
	def play(self):
		"""basic game scheme"""
		global player   #all player stats will be stocked here
		global opponent	#all opponents stats will be stocked here
		
		print "Game started, %s ! \n" % self.player_name
		print "Now select your character \n"
		player = my_game.choosing_character()  #player chooses his character
		
		print "You are playing as %s, the %s, fighting with %s." % (player.name, player.title, player.weapon.name) 
		print "Hitpoints: %s, Base attack: %s, Defense: %s\n" % (player.hp, player.attack, player.defense)
		
		print "Now selecting random opponent... \n"
		raw_input(">")
		opponent = my_game.random_opponent() #random AI opponent is selected
		print "Your opponent: %s, the %s, fighting with %s." % (opponent.name, opponent.title, opponent.weapon.name) 
		print "Hitpoints: %s, Base attack: %s, Defense: %s, %s \n" % (opponent.hp, opponent.attack, opponent.defense, opponent.description)  
		raw_input("Press any key: ")
		return my_game.combat()	#all combat procedures including game endings
		
	
	def choosing_character(self):
		"""Choosing predefined player character or create custom character"""
		print "Choose your warrior:" 
		print "1: %s, %s" % (p_heavy.name, p_heavy.title)
		print "2: %s, %s" % (p_cat.name, p_cat.title)
		print "3: %s, %s" % (p_rogue.name, p_rogue.title)
		print "4: %s, %s" % (p_giant.name, p_giant.title)
		print "5: %s, %s" % (p_amazon.name, p_amazon.title)
		print "6: %s, %s" % (p_two_orc.name, p_two_orc.title)
		print "7: Custom character"
		choose = raw_input("> ")
		if choose == "1":  #pre-built characters
			return p_heavy
		elif choose == "2":
			return p_cat
		elif choose == "3":
			return p_rogue
		elif choose == "4":
			return p_giant
		elif choose == "5":
			return p_amazon
		elif choose == "6":
			return p_two_orc
		elif choose == "7":
			print "Choose your name:"
			random_character.name = raw_input("> ")  #custom name
			print "Select weapon:"     #custom character weapons
			print "1: %s, attack %s, damage: %s" % (sabre.name, sabre.attack, sabre.damage_string)
			print "2: %s, attack %s, damage: %s" % (great_club.name, great_club.attack, great_club.damage_string)
			print "3: %s, attack %s, damage: %s" % (sword.name, sword.attack, sword.damage_string)
			print "4: %s, attack %s, damage: %s" % (rapier.name, rapier.attack, rapier.damage_string)
			print "5: %s, attack %s, damage: %s" % (lance.name, lance.attack, lance.damage_string)
			player_weapon = raw_input("> ")
			if player_weapon == "1":
				random_character.weapon = sabre
			elif player_weapon == "2":
				random_character.weapon = great_club
			elif player_weapon == "3":
				random_character.weapon = sword
			elif player_weapon == "4":
				random_character.weapon = rapier
			elif player_weapon == "5":
				random_character.weapon = lance
			return random_character
		else:
			print "Try again"
			return my_game.choosing_character()
	
	def random_opponent(self):
		"""randomly choosing an opponent"""
		opp_roll = die6()
		if opp_roll == 1:
			return heavy
		elif opp_roll == 2:
			return cat
		elif opp_roll == 3:
			return rogue
		elif opp_roll == 4:
			return giant
		elif opp_roll == 5:
			return amazon
		elif opp_roll == 6:
			return two_orc
	
	def combat(self):
		""" Basic scheme of combat, rounds counting, styles history, win/lose conditions, endings"""
		round = 1
		global player_last_style  #for styles, affecting 2 od more rounds - parry, furious... 
		global opponent_last_style #for styles, affecting 2 od more rounds - parry, furious...
		player_last_style = standard
		opponent_last_style = standard
		while player.hp > 0 and opponent.hp > 0:
			print "-------------------------------\nFighting round %s began!\n-------------------------------" % round
			my_game.combat_round()
			player_last_style = player_current_style
			opponent_last_style = opponent_current_style
			round +=1
		if player.hp <= 0 and opponent.hp > 0:  #LOSE
			print "-------------------------------\n%s is falling to the ground, heavily wounded.\nYOU LOST THIS MATCH!!!\n------------------------------- " % player.name
		elif player.hp > 0 and opponent.hp <= 0: #WIN
			print "-------------------------------\nYour foe %s is falling to the ground, heavily wounded.\nYOU WON THIS MATCH!!!\n------------------------------- " % opponent.name
		elif player.hp <= 0 and opponent.hp <= 0: #DRAW
			print "-------------------------------\nYou brutally hit %s in same moment, as %s hit you. You both are falling to the ground, heavily wounded.\nTHIS WAS A DOUBLE KILL!!!\n------------------------------- " % (opponent.name,opponent.name)
		raw_input(">")
		return my_game.menu()   #PROBLEM HERE IS, HOW TO RESET HPS AND OTHER STATS DO DEFAULT to be able to play again properly
		
	def combat_round(self):
		global player_current_style
		global opponent_current_style
		
		"""Player turn"""
		print "You are attacking!!!\n-------------------------------"
		
		if player_last_style == parry:   #if last action was parry or furious, this round has predefined after-style
			player_current_style = after_parry
		elif player_last_style == furious:
			player_current_style = after_furious
		else:
			player_current_style = my_game.player_choose_style() #player chooses his style
		print "You are using %s this round." % player_current_style.name
		
		player_attack_roll = player_current_style.attack_roll() #attack roll
		player_total_attack = player_attack_roll + player.attack + player.weapon.attack + player_current_style.attack_bonus #players total attack
		opponent_total_defense = opponent.defense + opponent_last_style.defense #opponent total defense
		print "You rolled %s, so %s's total attack this round is %s (%s+%s+%s+%s). \nYour opponent total defense is %s(%s+%s)." % (player_attack_roll, player.name, player_total_attack, player_attack_roll, player.attack, player.weapon.attack, player_current_style.attack_bonus, opponent_total_defense, opponent.defense, opponent_last_style.defense)   #opravit!!!
		
		if player_total_attack > opponent_total_defense and player_attack_roll != 10: #succesful hit
			damage = player.weapon.damage_dealt() + player_current_style.damage_bonus
			opponent.hp -= damage
			print "YOU SUCCESFULY HIT!\n%s %s and hit his foe, dealt %s damage (%s+%s). %s now have %s HPs left." % (player.name, player_current_style.attack_desc, damage, damage - player_current_style.damage_bonus, player_current_style.damage_bonus, opponent.name, opponent.hp)
		elif player_attack_roll == 10:  #critical hit : automaticky hits opponent and deal +2 bonus damage
			damage = player.weapon.damage_dealt() + 2 + player_current_style.damage_bonus
			opponent.hp -= damage
			print "CRITICAL HIT!\n%s %s and fiercely hit his foe, dealt incredible %s damage(%s+%s+2 for critical). %s now have %s HPs left." % (player.name, player_current_style.attack_desc, damage, damage - 2 - player_current_style.damage_bonus, player_current_style.damage_bonus, opponent.name, opponent.hp)
		else: #missing opponent
			print "YOU MISSED!\n%s %s, but missed his foe."  %(player.name, player_current_style.attack_desc)
		raw_input(">")
		
		"""Opponent turn"""
		print "-------------------------------\nNow %s is attacking you!" % opponent.name
		
		if opponent_last_style == parry: #if last action was parry or furious, this round has predefined after-style
			opponent_current_style = after_parry
		elif opponent_last_style == furious:
			opponent_current_style = after_furious
		else:
			opponent_current_style = my_game.opponent_choose_style() #opponent randomly chooses his style
		print "%s is using %s this round." % (opponent.name, opponent_current_style.name)
		
		opponent_attack_roll = opponent_current_style.attack_roll()
		opponent_total_attack = opponent_attack_roll + opponent.attack + opponent.weapon.attack + opponent_current_style.attack_bonus
		player_total_defense = player.defense + player_current_style.defense
		print "%s rolled %s, and has total attack for this round %s(%s+%s+%s+%s).\nYour defense is %s(%s+%s)" % (opponent.name, opponent_attack_roll, opponent_total_attack, opponent_attack_roll, opponent.attack, opponent.weapon.attack, opponent_current_style.attack_bonus, player_total_defense, player.defense, player_current_style.defense)
		
		if opponent_total_attack > player_total_defense and opponent_attack_roll != 10: #succesful hit
			damage = opponent.weapon.damage_dealt() + opponent_current_style.damage_bonus
			player.hp -= damage
			print "YOU WERE WOUNDED!\n%s %s and hit you, dealt %s damage (%s+%s). %s now have %s HPs left." % (opponent.name, opponent_current_style.attack_desc, damage, damage - opponent_current_style.damage_bonus, opponent_current_style.damage_bonus, player.name, player.hp)
		elif opponent_attack_roll == 10: #critical hit
			damage = opponent.weapon.damage_dealt() + opponent_current_style.damage_bonus + 2
			player.hp -= damage
			print "YOU SUFFERED CRITICAL HIT!\n%s %s and fiercely hit you, dealt incredible %s damage (%s+%s+2 for critical). %s now have %s HPs left." % (opponent.name, opponent_current_style.attack_desc, damage, damage - opponent_current_style.damage_bonus, opponent_current_style.damage_bonus, player.name, player.hp)
		else: 
			print "YOU DEFENDED YOURSELF!\n%s %s, but missed you!" % (opponent.name, opponent_current_style.attack_desc)
		raw_input(">")
		
	def player_choose_style(self):
		"""each round, player is selecting new fighting style"""
		chosen_style = raw_input("Select your style: 1:standard, 2:aggressive, 3:defensive, 4:strong, 5:furious, 6:parry")
		if chosen_style == "1":
			return standard
		elif chosen_style == "2":
			return aggressive
		elif chosen_style == "3":
			return defensive
		elif chosen_style == "4":
			return strong
		elif chosen_style == "5":
			return furious
		elif chosen_style == "6":
			return parry
		else: 
			return my_game.player_choose_style()
	
	def opponent_choose_style(self):
		"""each round, opponent is randomly selecting new fighting style"""
		chosen_style = die10()
		if chosen_style in range(1,4):
			return standard
		elif chosen_style in range(4,6):
			return aggressive
		elif chosen_style == 6:
			return defensive
		elif chosen_style in range(7,9):
			return strong
		elif chosen_style == 9:
			return furious
		elif chosen_style == 10:
			return parry
		else: 
			return my_game.opponent_choose_style()
	
	def rules(self):
		print "GAME RULES:\n1: BASIC SYSTEM\n2: FIGHTING ROUND\n3: FIGHTING STYLES\n4: WEAPONS\n5: BACK TO MAIN MENU"
		chosen_rule = raw_input("> ")
		if chosen_rule == "1":
			print "BASIC SYSTEM:\nIn this game, you select your character and you fight in arena against selected foe. Both fighters have HitPoints, Attack and Defense stats. First combanatnt with zero or less HP loses the fight and game ends. "
			return my_game.rules()
		elif chosen_rule == "2":
			print "FIGHTING ROUND:\n\nEach round both opponent try to hit each other.\nWhen the combatant is attacking, he makes random 1d10 roll (1-10). Then he adds his base attack, and his weapon attack bonus and bonus for his style. If total score is higher than opponent Defense score, the opponent is his. Combatant then rolls his damage roll, which depends on his weapon. Result is substracted from opponents HitPoints."
			return my_game.rules()
		elif chosen_rule == "3":
			print "FIGHTING STYLES:\nAt the beginning of each round, you can choose your fighting style for the round. Each one can alter your stats in some way:"
			print "%s: attack %s, defense %s, damage bonus %s." % (standard.name, standard.attack_bonus, standard.defense, standard.damage_bonus)
			print "%s: attack %s, defense %s, damage bonus %s." % (aggressive.name, aggressive.attack_bonus, aggressive.defense, aggressive.damage_bonus)
			print "%s: attack %s, defense %s, damage bonus %s." % (defensive.name, defensive.attack_bonus, defensive.defense, defensive.damage_bonus)
			print "%s: attack %s, defense %s, damage bonus %s." % (strong.name, strong.attack_bonus, strong.defense, strong.damage_bonus)
			print "%s: attack %s, defense %s, damage bonus %s. \nNext turn, fighter will recovery from this attack, will not be able to choose new style and his attack will be -10" % (furious.name, furious.attack_bonus, furious.defense, furious.damage_bonus)
			print "%s: attack %s, defense %s, damage bonus %s. \nNext turn, fighter will make attack from his parry, with bonus attack +2, damage +2" % (parry.name, parry.attack_bonus, parry.defense, parry.damage_bonus)
			return my_game.rules()
		elif chosen_rule == "4":
			print "WEAPONS\n: There are different weapons in game, each has its own attack and damage modifier. For example Sword has attack bonus 0, and deal damage of 1d6 + 1, e.g. one roll of six-sided dice plus 0, so the range is between 2 - 7."
			print "1: %s, attack %s, damage: %s" % (sabre.name, sabre.attack, sabre.damage_string)
			print "2: %s, attack %s, damage: %s" % (great_club.name, great_club.attack, great_club.damage_string)
			print "3: %s, attack %s, damage: %s" % (sword.name, sword.attack, sword.damage_string)
			print "4: %s, attack %s, damage: %s" % (rapier.name, rapier.attack, rapier.damage_string)
			print "5: %s, attack %s, damage: %s" % (lance.name, lance.attack, lance.damage_string)
			return my_game.rules()
		elif chosen_rule == "5":
			return my_game.menu()
		else: 
			return my_game.rules()
		
	
	def test(self):
		"""for testing purpose"""
		return "Testing..."
		
			

my_game = Arena("Misa")
my_game.menu()