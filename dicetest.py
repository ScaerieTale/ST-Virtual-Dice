from random import randint
while True:
    diceNum = int(input("how many dice? "))
    diceType = int(input("What type? (D8, D12, etc): D"))
    dmgBonus = int(input("Enter any damage bonus(es) or 0 if none): "))
    print(f"{randint(diceNum, (diceNum * diceType)) + dmgBonus} damage!")
