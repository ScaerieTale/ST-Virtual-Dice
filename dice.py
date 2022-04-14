from random import randint
class Dice:
    def d20(bonus):
        return randint(1, 20) + bonus

    def attack(d_num, d_type, bonus):
        return randint(d_num, d_type) + bonus
