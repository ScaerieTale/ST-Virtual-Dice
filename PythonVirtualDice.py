from random import randint
import sys

gameType = input("""Greetings, player!  Do you want [C]lassic dice where you can choose any dice you want,
or would you like a more guided, [D]20 experience? """).lower()
if gameType == 'c' or 'classic':
	while True:
		dice = input("Roll the dice.  Enter any whole number to get 1D of that type, or Q to exit: ")
		if dice == "q":
			sys.exit("Thanks for playing!")
		else:
			print(f"You have rolled a d{dice}: {randint(1, int(dice))}")
elif gameType == 'd':
	while True:
		choice = input("[A]ttack roll, [D]amage roll, or [S]aving Throw/S[k]]ill check ").lower()
		if choice == 'a' or 'attack' or 'attack roll':
			atp = input("Enter your attack power: ")
			dice = randint(1, 20) + int(atp)
			armck = input(f"You rolled a {dice}!  Roll damage? (y/n): ").lower()
			if armck == 'y':
				diceNum = int(input("How many dice will you throw? "))
				diceType = int(input("What type of dice (D4, D12, etc): D"))
				dmgBonus = int(input("Apply any damage bonus (or type '0' if none): "))
				print(f"{randint(diceNum, (diceNum * diceType)) + dmgBonus} damage!")
		elif choice == 'd' or 'damage' or 'damage roll':
			diceNum = int(input("how many dice? "))
			diceType = int(input("What type? (D8, D12, etc): D "))
			dmgBonus = int(input("Enter any damage bonus(es) or 0 if none): "))
			print(f"{randint(diceNum, (diceNum * diceType)) + dmgBonus} damage!")
		elif choice == 's' or 'save' or 'saving' or 'saving throw' or 'k' or 'skill' or 'skill check':
			savingSkill = int(input("Add your save/skill modifier: "))
			print(f"Your check result is {randint(1, 20) + savingSkill}")
		elif choice == 'q' or 'quit' or 'e' or 'exit':
			sys.exit("Thanks for playing!")
		else:
			print("Invalid command.")
