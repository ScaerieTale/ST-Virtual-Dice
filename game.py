from dice import Dice
from sys import exit

class Game:
    def game():
        print("Welcome to ScaerieTale's Virtual Game Assistant!")
        while True:
            roll_type = input("[A]ttack roll, [D]amage roll, or [S]ave/Skill check? ").lower()
            if roll_type is 'a':
                result = Dice.d20(int(input("Enter any attack bonus, or 0 if none: ")))
                roll_for_dam = input(f"{result}!  Roll for damage? ")
                if roll_for_dam is 'yes':
                    dam_num = int(input("How many dice? (1, 2, 3, etc): "))
                    dam_type = int(input(f"What type? {dam_num}d"))
                    bonus = int(input("Add bonus damage, or 0 if none: "))
                    result = Dice.attack(dam_num, dam_type, bonus)
                    print(f"{dam_num}d{dam_type}+{bonus} = {result}")
                elif roll_type is 'd':
                    dam_type = int(input("How many dice? (1, 2, etc.): "))
                    dam_num = int(input(f"What type? {dam_num}d"))
                    bonus = int(input("Enter damage bonus if any, or 0: "))
                    print(f"{dam_num}d{dam_type} + {bonus} = {result}!")

                elif roll_type is 's':
                    bonus = int(input(" Enter any saving throw/skill bonus, or 0 if none: "))
                    result = Dice.d20(bonus)
                    print(f"1d20+{bonus} = {result}!")
                elif roll_type is 'q':
                    exit()
                else:
                    print("Invalid input.")