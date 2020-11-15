from random import randint

class murder_card:
    def __init__(self, name, weapon, location, drop, activation):
        self.name = name
        self.weapon_used = weapon
        self.location = location
        self.drop_number = drop
        self.activation_number = activation

    def print(self):
        print("Name: " + self.name)
        print("Weapon used: " + self.weapon_used)
        print("Location: " + self.location.name)
        print("Drop number: " + str(self.drop_number))
        print("Activation number: " + str(self.activation_number))

class alabi_card:
    def __init__(self, activity, location, drop, activation):
        self.activity = activity
        self.location = location
        self.drop_number = drop
        self.activation_number = activation

class room:
    def __init__(self, name):
        self.name = name
        self.people = []
        self.murder = False

    def print(self):
        print("Name: " + self.name)
        if str(self.people) != "[]":
            print("People: " + str(self.people))
        else:
            print("Empty")

def make_rooms(num_rooms):
    rooms = ["Susquehanna Hall", "D-Hall", "Library", "Erickson Hall", "Patapsco Hall", "Harbor Hall", "Chesapeake Hall", "Harbor Hall", "The Tube"]
    used_rooms = []

    for i in range(num_rooms):
        random_number = randint(0, len(rooms)-1)
        new_room = rooms[random_number]
        used_rooms.append(room(new_room))
        rooms.remove(new_room)

    return used_rooms

def load_cards():
    cards = []
    cards.append(murder_card("Venzah", "Knife", "Emme's room", 1, [3,4]))
    return cards

def rollDice(numRolls):
    rolls = []

    for i in range(numRolls):
        rolls.append(randint(1, 6))

    return rolls

def printRolls(rolls):
    for roll in rolls:
        print("You rolled " + str(roll))

if __name__ == '__main__':
    numPlayers = -1
    while numPlayers < 1:
        numPlayers = input("How many players? ")
        if not numPlayers.isnumeric():
            numPlayers = -1
        else:
            numPlayers = int(numPlayers)

    rooms = make_rooms(numPlayers + 2)
    for room in rooms:
        room.print()



    """
    murder_cards = load_cards()
    for card in murder_cards:
        card.print()
    """

    """
    numRolls = -1
    while numRolls < 1:
        numRolls = input("How many rolls? ")
        if not numRolls.isnumeric():
            numRolls = -1
        else:
            numRolls = int(numRolls)

    rolls = rollDice(3)
    printRolls(rolls)
    """


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
