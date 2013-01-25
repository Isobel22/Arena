#Arena - combat turn-based game

from sys import exit
from dies_roll import die6, die10
from characters import heavy, cat, rogue, giant, amazon, two_orc, random_character, p_heavy, p_cat, p_rogue, p_giant, p_amazon, p_two_orc
from weapons import sabre, great_club, sword, rapier, lance
from fight_style import standard, aggressive, defensive, strong, furious, parry, after_parry, after_furious


class Arena(object):

    def __init__(self, player_name):
        self.player_name = player_name

    def menu(self):
        """main options"""
        chosen_menu = '1'
        while chosen_menu not in ('3'):
            print "-------------------------------\n         A*R*E*N*A !!!   \nTurn-based battle game by Misa\n-------------------------------"
            print "1: PLAY THE GAME\n2: GAME RULES\n3: EXIT:"
            chosen_menu = raw_input("> ")
            if chosen_menu == "1":
                self.play()
            elif chosen_menu == "2":
                self.rules()
            elif chosen_menu == "3":
                exit(0)

    def play(self):
        """basic game scheme"""
        print "Game started, %s ! \n" % self.player_name
        print "Now select your character \n"
        self.player = self.choosing_character()  # player chooses his character

        print "You are playing as %s, the %s, fighting with %s." % (self.player.name, self.player.title, self.player.weapon.name)
        print "Hitpoints: %s, Base attack: %s, Defense: %s\n" % (self.player.hp, self.player.attack, self.player.defense)

        print "Now selecting random opponent... \n"
        raw_input(">")
        self.opponent = self.random_opponent()  # random AI opponent is selected
        print "Your opponent: %s, the %s, fighting with %s." % (self.opponent.name, self.opponent.title, self.opponent.weapon.name)
        print "Hitpoints: %s, Base attack: %s, Defense: %s, %s \n" % (self.opponent.hp, self.opponent.attack, self.opponent.defense, self.opponent.description)
        raw_input("Press any key: ")
        self.combat(self.player.hp, self.opponent.hp)  # all combat procedures including game endings

    def choosing_character(self):
        """Choosing predefined player character or create custom character"""
        player_chars = {"1": p_heavy, "2": p_cat, "3": p_rogue, "4": p_giant, "5": p_amazon, "6": p_two_orc}  # pre-built characters
        weapons = {"1": sabre, "2": great_club, "3": sword, "4": rapier, "5": lance}
        print "Choose your warrior:"
        for index, character in sorted(player_chars.iteritems()):  # prints all pre-built characters
            print "%s: %s, %s" % (index, character.name, character.title)
        print "7: Custom character"
        choose = raw_input("> ")
        while choose not in player_chars or choose != "7":
            try:
                return player_chars[choose]
            except KeyError:
                if choose == "7":
                    print "Choose your name:"
                    random_character.name = raw_input("> ")  # custom name
                    print "Select weapon:"  # custom character weapons
                    for index, weapon in sorted(weapons.iteritems()):
                        print "%s: %s, attack %s, damage: %s" % (index, weapon.name, weapon.attack, weapon.damage_string)
                    player_weapon = None
                    while player_weapon not in weapons:
                        player_weapon = raw_input("> ")
                        try:
                            random_character.weapon = weapons[player_weapon]
                        except KeyError:
                            print "Try again"
                    return random_character
                else:
                    print "Try again"

    def random_opponent(self):
        """randomly choosing an opponent"""
        opp_chars = {1: heavy, 2: cat, 3: rogue, 4: giant, 5: amazon, 6: two_orc}  # pre-built characters
        opp_roll = die6()
        return opp_chars[opp_roll]

    def combat(self, player_hp, opponent_hp):
        """ Basic scheme of combat, rounds counting, styles history, win/lose conditions, endings"""
        round = 1
        self.player_last_style = standard
        self.opponent_last_style = standard
        self.player_hp = player_hp
        self.opponent_hp = opponent_hp
        while self.player_hp > 0 and self.opponent_hp > 0:
            print "-------------------------------\nFighting round %s began!\n-------------------------------" % round
            self.combat_round(self.player_last_style, self.opponent_last_style)
            round += 1
        if self.player_hp <= 0 and self.opponent_hp > 0:  # LOSE
            print "-------------------------------\n%s is falling to the ground, heavily wounded.\nYOU LOST THIS MATCH!!!\n------------------------------- " % self.player.name
        elif self.player_hp > 0 and self.opponent_hp <= 0:  # WIN
            print "-------------------------------\nYour foe %s is falling to the ground, heavily wounded.\nYOU WON THIS MATCH!!!\n------------------------------- " % self.opponent.name
        elif self.player_hp <= 0 and self.opponent_hp <= 0:  # DRAW
            print "-------------------------------\nYou brutally hit %s in same moment, as %s hit you. You both are falling to the ground, heavily wounded.\nTHIS WAS A DOUBLE KILL!!!\n------------------------------- " % (self.opponent.name, self.opponent.name)
        raw_input("Press any key:")

    def combat_round(self, player_current_style, opponent_current_style):
        """Player turn"""
        print "You are attacking!!!\n-------------------------------"

        if player_current_style == parry:  # if last action was parry or furious, this round has predefined after-style
            player_current_style = after_parry
        elif player_current_style == furious:
            player_current_style = after_furious
        else:
            player_current_style = self.player_choose_style()  # player chooses his style
        print "You are using %s this round." % player_current_style.name

        player_attack_roll = player_current_style.attack_roll()  # attack roll
        player_total_attack = player_attack_roll + self.player.attack + self.player.weapon.attack + player_current_style.attack_bonus  # players total attack
        opponent_total_defense = self.opponent.defense + opponent_current_style.defense  # opponent total defense
        print "You rolled %s, so %s's total attack this round is %s (%s+%s+%s+%s). \nYour opponent total defense is %s(%s+%s)." % (player_attack_roll, self.player.name, player_total_attack, player_attack_roll, self.player.attack, self.player.weapon.attack, player_current_style.attack_bonus, opponent_total_defense, self.opponent.defense, opponent_current_style.defense)

        if player_total_attack > opponent_total_defense and player_attack_roll != 10:  # succesful hit
            damage = self.player.weapon.damage_dealt() + player_current_style.damage_bonus
            self.opponent_hp -= damage
            print "YOU SUCCESFULY HIT!\n%s %s and hit his foe, dealt %s damage (%s+%s). %s now have %s HPs left." % (self.player.name, player_current_style.attack_desc, damage, damage - player_current_style.damage_bonus, player_current_style.damage_bonus, self.opponent.name, self.opponent_hp)
        elif player_attack_roll == 10:  # critical hit : automaticky hits opponent and deal +2 bonus damage
            damage = self.player.weapon.damage_dealt() + 2 + player_current_style.damage_bonus
            self.opponent_hp -= damage
            print "CRITICAL HIT!\n%s %s and fiercely hit his foe, dealt incredible %s damage(%s+%s+2 for critical). %s now have %s HPs left." % (self.player.name, player_current_style.attack_desc, damage, damage - 2 - player_current_style.damage_bonus, player_current_style.damage_bonus, self.opponent.name, self.opponent_hp)
        else:  # missing opponent
            print "YOU MISSED!\n%s %s, but missed his foe." % (self.player.name, player_current_style.attack_desc)
        raw_input(">")

        """Opponent turn"""
        print "-------------------------------\nNow %s is attacking you!" % self.opponent.name

        if opponent_current_style == parry:  # if last action was parry or furious, this round has predefined after-style
            opponent_current_style = after_parry
        elif opponent_current_style == furious:
            opponent_current_style = after_furious
        else:
            opponent_current_style = self.opponent_choose_style()  # opponent randomly chooses his style
        print "%s is using %s this round." % (self.opponent.name, opponent_current_style.name)

        opponent_attack_roll = opponent_current_style.attack_roll()
        opponent_total_attack = opponent_attack_roll + self.opponent.attack + self.opponent.weapon.attack + opponent_current_style.attack_bonus
        player_total_defense = self.player.defense + player_current_style.defense
        print "%s rolled %s, and has total attack for this round %s(%s+%s+%s+%s).\nYour defense is %s(%s+%s)" % (self.opponent.name, opponent_attack_roll, opponent_total_attack, opponent_attack_roll, self.opponent.attack, self.opponent.weapon.attack, opponent_current_style.attack_bonus, player_total_defense, self.player.defense, player_current_style.defense)

        if opponent_total_attack > player_total_defense and opponent_attack_roll != 10:  # succesful hit
            damage = self.opponent.weapon.damage_dealt() + opponent_current_style.damage_bonus
            self.player_hp -= damage
            print "YOU WERE WOUNDED!\n%s %s and hit you, dealt %s damage (%s+%s). %s now have %s HPs left." % (self.opponent.name, opponent_current_style.attack_desc, damage, damage - opponent_current_style.damage_bonus, opponent_current_style.damage_bonus, self.player.name, self.player_hp)
        elif opponent_attack_roll == 10:  # critical hit
            damage = self.opponent.weapon.damage_dealt() + opponent_current_style.damage_bonus + 2
            self.player_hp -= damage
            print "YOU SUFFERED CRITICAL HIT!\n%s %s and fiercely hit you, dealt incredible %s damage (%s+%s+2 for critical). %s now have %s HPs left." % (self.opponent.name, opponent_current_style.attack_desc, damage, damage - opponent_current_style.damage_bonus - 2, opponent_current_style.damage_bonus, self.player.name, self.player_hp)
        else:
            print "YOU DEFENDED YOURSELF!\n%s %s, but missed you!" % (self.opponent.name, opponent_current_style.attack_desc)
        self.player_last_style = player_current_style
        self.opponent_last_style = opponent_current_style
        raw_input(">")

    def player_choose_style(self):
        """each round, player is selecting new fighting style"""
        styles = {"1": standard, "2": aggressive, "3": defensive, "4": strong, "5": furious, "6": parry}
        chosen_style = None
        while chosen_style not in styles:
            chosen_style = raw_input("Select your style: 1:standard, 2:aggressive, 3:defensive, 4:strong, 5:furious, 6:parry")
            if chosen_style in styles:
                return styles[chosen_style]
            else:
                print "Try again"

    def opponent_choose_style(self):
        """each round, opponent is randomly selecting new fighting style"""
        chosen_style = die10()
        if chosen_style in range(1, 4):
            return standard
        elif chosen_style in range(4, 6):
            return aggressive
        elif chosen_style == 6:
            return defensive
        elif chosen_style in range(7, 9):
            return strong
        elif chosen_style == 9:
            return furious
        elif chosen_style == 10:
            return parry
        else:
            return standard

    def rules(self):
        weapons = [sabre, great_club, sword, rapier, lance]
        styles = [standard, aggressive, defensive, strong, furious, parry]
        game_rules = {"1": "BASIC SYSTEM:\nIn this game, you select your character and you fight in arena against selected foe. Both fighters have HitPoints, Attack and Defense stats. First combanatnt with zero or less HP loses the fight and game ends. ",
                      "2": "FIGHTING ROUND:\n\nEach round both opponent try to hit each other.\nWhen the combatant is attacking, he makes random 1d10 roll (1-10). Then he adds his base attack, and his weapon attack bonus and bonus for his style. If total score is higher than opponent Defense score, the opponent is his. Combatant then rolls his damage roll, which depends on his weapon. Result is substracted from opponents HitPoints.",
                      "3": "FIGHTING STYLES:\nAt the beginning of each round, you can choose your fighting style for the round. Each one can alter your stats in some way:",
                      "4": "WEAPONS:\nThere are different weapons in game, each has its own attack and damage modifier. For example Sword has attack bonus 0, and deal damage of 1d6 + 1, e.g. one roll of six-sided dice plus 0, so the range is between 2 - 7."
                      }
        chosen_rule = None
        while chosen_rule != "5":
            print "GAME RULES:\n1: BASIC SYSTEM\n2: FIGHTING ROUND\n3: FIGHTING STYLES\n4: WEAPONS\n5: BACK TO MAIN MENU"
            chosen_rule = raw_input("> ")
            try:
                print game_rules[chosen_rule]
                if chosen_rule == "3":
                    for style in styles:
                        print "%s: attack %s, defense %s, damage bonus %s. %s" % (style.name, style.attack_bonus, style.defense, style.damage_bonus, style.style_desc)
                if chosen_rule == "4":
                    for weapon in weapons:
                        print "%s: attack %s, damage: %s" % (weapon.name, weapon.attack, weapon.damage_string)
            except KeyError:
                pass


my_game = Arena("Misa")
my_game.menu()
