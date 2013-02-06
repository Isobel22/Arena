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
        self.combat()  # all combat procedures including game endings

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

    def combat(self):
        """ Basic scheme of combat, rounds counting, styles history, win/lose conditions, endings"""
        round = 1
        while self.player.hp > 0 and self.opponent.hp > 0:
            print "-------------------------------\nFighting round %s began!\n-------------------------------" % round
            self.player.attacking(self.opponent, True)
            self.opponent.attacking(self.player, False)
            round += 1
        if self.player.hp <= 0 and self.opponent.hp > 0:  # LOSE
            print "-------------------------------\n%s is falling to the ground, heavily wounded.\nYOU LOST THIS MATCH!!!\n------------------------------- " % self.player.name
        elif self.player.hp > 0 and self.opponent.hp <= 0:  # WIN
            print "-------------------------------\nYour foe %s is falling to the ground, heavily wounded.\nYOU WON THIS MATCH!!!\n------------------------------- " % self.opponent.name
        elif self.player.hp <= 0 and self.opponent.hp <= 0:  # DRAW
            print "-------------------------------\nYou brutally hit %s in same moment, as %s hit you. You both are falling to the ground, heavily wounded.\nTHIS WAS A DOUBLE KILL!!!\n------------------------------- " % (self.opponent.name, self.opponent.name)
        raw_input("Press any key:")

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
