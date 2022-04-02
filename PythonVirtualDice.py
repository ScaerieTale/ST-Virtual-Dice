from random import randint
import sys
#
# while True:
#		dice = input("Roll the dice ")
#	if dice == "q":
#		break
#	else:
#		print(f"You have rolled a d{dice}: {randint(1, int(dice))}")

while True:

	choice = input("[A]ttack roll, [D]amage roll, [S]aving Throw, or S[k]]ill check ").lower
	if choice == ('a' or 'attack'):
		atp = input("Enter your attack power: ")
		dice = randint(1, 20) + int(atp)
		armck = input(f"You rolled a {dice}!  Roll damage? (y/n): ")
		if armck == 'y':
			diceNum = int(input("How many dice will you throw? "))
			diceType = int(input("What type of dice (D4, D12, etc): D"))
		print(f"{randint({diceNum}, {diceType})}")
	elif choice == 'd' or 'damage':
		diceNum = int(input("how many dice? "))
		diceType = int(input("What type? (D8, D12, etc): D "))
		dmgBonus = int(input("Enter any damage bonus(es) or 0 if none: 1"))
		print(f"You rolled a {randint(diceNum, diceType) + dmgBonus}")
	elif choice == 's' or 'save' or 'saving throw':
		saving = int(input("Add your save modifier: "))
		print(f"Your save is {randint(1, 20) + saving}")
	elif choice == 'k' or 'skill' or 'skill check':
		skill = int(input("Enter your skill level: "))
		print(f"Your skill check roll was: {randint(1, 20) + skill}")
	elif choice == 'Quit' or 'quit' or 'Q' or 'q' or 'Exit' or 'exit':
		sys.exit("Thanks for playing!")
