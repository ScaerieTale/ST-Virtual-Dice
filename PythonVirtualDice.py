from random import randint


while True:
	dice = input("Roll the dice ")
	if dice == "q":
		break
	else:
		print(f"You have rolled a d{dice}: {randint(1, int(dice))}")

