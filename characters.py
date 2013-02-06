from dies_roll import die6, die10
from weapons import sabre, great_club, sword, rapier, lance, two_sabres
from fight_style import standard, aggressive, defensive, strong, furious, parry, after_parry, after_furious


class Character(object):
    def __init__(self, name, title, description, weapon, hp, attack, defense, current_style):
        self.name = name
        self.title = title
        self.description = description
        self.weapon = weapon
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.current_style = current_style

    def create_instance(self, select):
        pass  # This pass has same meaning as it has in a Poker game. It means "I give up this time" :-)

    def attacking(self, defender, isHumanPlayerAttacking):
        """Attacker (self) is attacking the defender"""
        print "%s is attacking!!!\n-------------------------------" % self.name

        if self.current_style == parry:  # if last action was parry or furious, this round has predefined after-style
            self.current_style = after_parry
        elif self.current_style == furious:
            self.current_style = after_furious
        else:
            self.current_style = self.choose_style(isHumanPlayerAttacking)
        print "%s is using %s this round." % (self.name, self.current_style.name)

        attack_roll = self.current_style.attack_roll()  # attack roll
        total_attack = attack_roll + self.attack + self.weapon.attack + self.current_style.attack_bonus  # attackers total attack
        total_defense = defender.defense + defender.current_style.defense  # opponent total defense
        print "%s rolled %s, total attack this round is %s (%s+%s+%s+%s). \n%s's total defense is %s(%s+%s)." % (self.name, attack_roll, total_attack, attack_roll, self.attack, self.weapon.attack, self.current_style.attack_bonus, defender.name, total_defense, defender.defense, defender.current_style.defense)

        if total_attack > total_defense and attack_roll != 10:  # succesful hit
            damage = self.weapon.damage_dealt() + self.current_style.damage_bonus
            defender.hp -= damage
            print "SUCCESFULL HIT!\n%s %s and hit his foe, dealt %s damage (%s+%s). %s now have %s HPs left." % (self.name, self.current_style.attack_desc, damage, damage - self.current_style.damage_bonus, self.current_style.damage_bonus, defender.name, defender.hp)
        elif attack_roll == 10:  # critical hit : automaticky hits opponent and deal +2 bonus damage
            damage = self.weapon.damage_dealt() + 2 + self.current_style.damage_bonus
            defender.hp -= damage
            print "CRITICAL HIT!\n%s %s and fiercely hit his foe, dealt incredible %s damage(%s+%s+2 for critical). %s now have %s HPs left." % (self.name, self.current_style.attack_desc, damage, damage - self.current_style.damage_bonus - 2, self.current_style.damage_bonus, defender.name, defender.hp)
        else:  # missing opponent
            print "MISSED!\n%s %s, but missed his foe." % (self.name, self.current_style.attack_desc)
        raw_input(">")

    def choose_style(self, isHumanPlayerAttacking):
        """each round, combatants are selecting new fighting style"""
        chosen_style = None
        if isHumanPlayerAttacking:  # for Human Player - he chooses himself
            styles = {"1": standard, "2": aggressive, "3": defensive, "4": strong, "5": furious, "6": parry}
            while chosen_style not in styles:
                chosen_style = raw_input("Select your style: 1:standard, 2:aggressive, 3:defensive, 4:strong, 5:furious, 6:parry")
                if chosen_style in styles:
                    return styles[chosen_style]
                else:
                    print "Try again"
        else:  # for AI Player - program randomly chooses style
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


""" Predefined opponents """
heavy = Character("Bruno", "heavily-armored knight", "", sword, 15, 4, 12, standard)
cat = Character("Leonardo", "agile catling swashbuckler", "", rapier, 11, 7, 11, standard)
rogue = Character("Ratty", "dirty fighting rogue", "", sabre, 15, 6, 9, standard)
giant = Character("Ka-haak", "giant,slow but strong", "", great_club, 30, 4, 8, standard)
amazon = Character("Sheila", "amazon lancer", "", lance, 13, 5, 10, standard)
two_orc = Character("Grim and Grum", "two orcish raiders", "They are two, so they attack twice a round.", two_sabres, 16, 4, 9, standard)
""" Predefined players """
random_character = Character("", "newbie adventurer", "", "random_weapon(self)", die6() + 10, die6() // 3 + 4, die6() // 3 + 9, standard)
p_heavy = Character("Desmond", "heavily-armored knight", "", sword, 15, 4, 12, standard)
p_cat = Character("Bubbles", "agile catling swashbuckler", "", rapier, 11, 7, 11, standard)
p_rogue = Character("Louis", "dirty fighting rogue", "", sabre, 15, 6, 9, standard)
p_giant = Character("Tul-duru", "giant,slow but strong", "", great_club, 30, 4, 8, standard)
p_amazon = Character("Noelle", "amazon lancer", "", lance, 13, 5, 10, standard)
p_two_orc = Character("Shargat and Gobrath", "two orcish raiders", "They are two, so they attack twice a round.", two_sabres, 12, 0, 4, standard)
