from random import randint

class Player:
    def __init__(self, name):
        self.name = name
        rolls = rollDice(4)
        total = 0
        for i in rolls:
            total += i
        print("Your dice rolls are: " + str(rolls) + " and your total is: " + str(total))

        self.stat_dict = {
            "Speed": 0,
            "Weapon Proficiency": 0,
            "Stealth": 0,
            "Survival": 0
        }

        used_points = 0
        for i in range(4):
            if used_points < total:
                stat = -1
                while stat < 0 or stat > 6:
                    # String to hold proper stat
                    ability = self.stat_name(i)
                    print("Points remaining: ", total - used_points)
                    stat = input("How many points would you like to put into " + ability + "? (0-6) ")
                    if not stat.isnumeric() or int(stat) < 0 or int(stat) > 6:
                        stat = -1
                        print("That is not a valid input.")
                    else:
                        stat = int(stat)
                        used_points += stat
                        if used_points < total:
                            self.stat_dict[ability] = stat
                        else:
                            self.stat_dict[ability] = stat - (used_points - total)

        for x, y in self.stat_dict.items():
            print(x, ":", y)

        self.speed = rolls[0]
        self.weapon_proficiency = rolls[1]
        self.stealth = rolls[2]
        self.survival = rolls[3]
        self.weapon_cards = []
        self.winner = False

    def print(self):
        print('\n' + ''"Name: " + self.name)
        print("Speed: " + str(self.speed))
        print("Weapon Proficiency: " + str(self.weapon_proficiency))
        print("Stealth: " + str(self.stealth))
        print("Survival: " + str(self.survival))

        if len(self.weapon_cards) > 0:
            for card in self.weapon_cards:
                card.print()

    def add_weapon(self, card):
        self.weapon_cards.append(card)

    def stat_name(self, num):
        if num == 0:
            return "Speed"
        elif num == 1:
            return "Weapon Proficiency"
        elif num == 2:
            return "Stealth"
        else:
            return "Survival"

class murder_card:
    def __init__(self, weapon, location, drop, activation):
        # Should hold a weapon object
        self.weapon_used = weapon
        # Should hold a room object
        self.location = location
        # Should hold an int or int list
        self.drop_number = drop
        # Should hold an int or int list
        self.activation_number = activation

    def print(self):
        print('\n' + "Weapon: " + self.weapon_used.name)
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
        # Print "Name: [NAME], (if not empty) People: LIST_OF_PEOPLE (if empty) No one is here"
        print("Name: " + self.name + ", " + ("People: " + str(self.people) if self.people == "[]" else "No one is here"))

class weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

def make_rooms(num_rooms):
    rooms = ["Susquehanna Hall", "D-Hall", "Library", "Erickson Hall", "Patapsco Hall", "Harbor Hall", "Chesapeake Hall", "Harbor Hall", "The Tube", "The Commons", "Event Center"]
    used_rooms = []

    for i in range(num_rooms):
        random_number = randint(0, len(rooms)-1)
        new_room = rooms[random_number]
        used_rooms.append(room(new_room))
        rooms.remove(new_room)

    return used_rooms

def load_cards(room):
    cards = []
    cards.append(murder_card("Knife", room[randint(0, len(room) - 1)], 1, [3,4]))
    cards.append(murder_card("Scissors", room[randint(0, len(room) - 1)], 1, [3,4]))
    cards.append(murder_card("Light stick", room[randint(0, len(room) - 1)], 1, [3,4]))
    return cards

def rollDice(numRolls):
    rolls = []

    for i in range(numRolls):
        rolls.append(randint(1, 6))

    return rolls

def printRolls(rolls):
    for roll in rolls:
        print("You rolled " + str(roll))

def take_turn(player_dic, player):
    roll = rollDice(1)
    print(roll)
    for x in player_dic:
        for card in player_dic[x].weapon_cards:
            for i in card.activation_number:
                if i == roll[0]:
                    print("It worked i guess")
    hello = input("Stop. ")

def create_character(rooms):
    name = input("Hello player, what's your name? ")
    player = Player(name)
    murder = weapon("Knife", 1)
    # player.add_weapon(murder)
    activation = []
    for i in range(1, 7):
        activation.append(i)
    room = rooms[randint(0, len(rooms) - 1)]
    card = murder_card(murder, room, 1, activation)
    player.add_weapon(card)
    return player

def play_game():
    print("Welcome to UMBC!")
    """
    number_of_players = -1
    while number_of_players < 5 or number_of_players > 8:
        number_of_players = input("Now, how many of you are playing? (5-8) ")
        if not number_of_players.isnumeric():
            number_of_players = -1
        else:
            number_of_players = int(number_of_players)
    """
    # For testing (faster to make players)
    number_of_players = int(input("Now, how many of you are playing? "))

    rooms = make_rooms(number_of_players + 3)

    player_dic = {}
    for i in range(number_of_players):
        player = create_character(rooms)
        player_dic["player{0}".format(i)] = player

    turn = 0
    end_game = False
    while(not end_game):
        for i in range(number_of_players):
            print(player_dic["player{0}".format(i)].name, "'s turn!")
            take_turn(player_dic, i)
        for i in range(number_of_players):
            if (player_dic["player{0}".format(i)].winner == True):
                end_game = True
        turn += 1




if __name__ == '__main__':
    play_game()
    # p1 = player("Venzah")
    # p1.print()

    """
    numPlayers = -1
    while numPlayers < 5 or numPlayers > 8:
        numPlayers = input("How many players? (5-8) ")
        if not numPlayers.isnumeric():
            numPlayers = -1
        else:
            numPlayers = int(numPlayers)

    rooms = make_rooms(numPlayers + 3)
    for room in rooms:
        room.print()

    players = []
    for i in range(numPlayers):
        players.append(player("Venzah"))

    murder_cards = load_cards(rooms)
    for i in range(len(murder_cards)):
        players[i].add_weapon(murder_cards[i])
        players[i].print()
        # card[i].print()
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
