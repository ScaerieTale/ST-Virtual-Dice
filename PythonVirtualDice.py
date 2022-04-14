from random import randint
from sys import exit
from dice import Dice
from game import Game

game_type = input("""'Classic' is for the old 'choose any die type'.  
'New' is for a slightly more guided D&D/D20 expperience: """).lower()

if game_type is 'classic':
	while True:
		dice_type = int(input("Enter a die type (such as 6, 20, etc): 1d"))
		dice_amount = int(input("How many? "))
		dice_result = randint(dice_amount, dice_type)
		print(f"{dice_amount}d{dice_type}: {dice_result}")
		continue_rolling = input("Roll again? (yes/no) ").lower()
		if continue_rolling is 'no':
			exit()
elif game_type is "new":
	Game()
else:
	print("Invalid input.")