import random

def rollDice(numRolls):
    rolls = []

    for i in range(numRolls):
        rolls.append(random.randrange(1, 6))

    return rolls

def printRolls(rolls):
    for roll in rolls:
        print("You rolled " + str(roll))

if __name__ == '__main__':
    numRolls = -1
    while numRolls < 1:
        numRolls = input("How many rolls? ")
        if not numRolls.isnumeric():
            numRolls = -1
        else:
            numRolls = int(numRolls)

    rolls = rollDice(3)
    printRolls(rolls)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
