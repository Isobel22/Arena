from dies_roll import die6, die10


class Fight_style(object):
    def __init__(self, name, attack_roll, attack_bonus, defense, damage_bonus, attack_desc, style_desc):
        self.name = name
        self.attack_roll = attack_roll
        self.attack_bonus = attack_bonus
        self.defense = defense
        self.damage_bonus = damage_bonus
        self.attack_desc = attack_desc
        self.style_desc = style_desc

    def attacking(self):
        return self.attack_roll() + self.attack_bonus


standard = Fight_style("Standard attack", die10, 0, 0, 0, "made a standard attack", "")
aggressive = Fight_style("Aggressive attack", die10, 2, -2, 0, "attacked aggressively", "")
defensive = Fight_style("Defensive attack", die10, -2, 2, 0, "attacked from defensive stance", "")
strong = Fight_style("Strong attack", die10, -1, -1, 3, "attacked with great strenght", "")
furious = Fight_style("Furious attack", die10, 3, 0, 4, "made a furious, devastating charge", "\nNext turn, fighter will recovery from this attack, will not be able to choose new style and his attack will be -10")
parry = Fight_style("Parry", die6, -10, 4, 0, "only parried, preparing for next round attack", "\nNext turn, fighter will make attack from his parry, with bonus attack +2, damage +2")
after_parry = Fight_style("Attack from Parry", die10, 2, 0, 2, "suddenly counter-attacked from parry", "")
after_furious = Fight_style("Recovery from Furious attack", die6, -10, 0, 0, "were taking breath from last furious attack", "")
