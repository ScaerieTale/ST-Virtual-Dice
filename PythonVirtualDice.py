# Day 5 of the 100 Days of Code challenge, following Dr. Angela Yu's
# prescribed course on Udemy.  Course available at: https://www.udemy.com/course/100-days-of-code/

from random import randint


while True:
	dice = input("Roll the dice ")
	if dice == "q":
		break
	else:
		print(f"You have rolled a d{dice}: {randint(1, int(dice))}")

