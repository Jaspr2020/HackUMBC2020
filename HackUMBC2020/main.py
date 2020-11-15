from random import randint

class Player:
    def __init__(self, name):
        self.name = name
        rolls = rollDice(4)
        total = 0
        for i in rolls:
            total += i
        print()
        print("Your dice rolls are: " + str(rolls) + " and your total is: " + str(total))

        self.stat_dict = {
            "Speed": 0,
            "Weapon Proficiency": 0,
            "Stealth": 0,
            "Survival": 0
        }

        used_points = 0
        print("Here are your skills. Spend your points wisely!")
        for x, y in self.stat_dict.items():
            print(x, ":", y)
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
        print()

        #ToDo: change self.health so that it is in correlation with the player's initital roll
        self.health = 30
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
    def __init__(self, location, drop, activation):
        self.location = location
        self.drop_number = drop
        self.activation_number = activation

class Room:
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
        used_rooms.append(Room(new_room))
        rooms.remove(new_room)

    return used_rooms

def load_cards(rooms):

    weapon_list = ["Knife", "Scissors", "Light Stick", "Baseball Bat", "Heat Gun", "Katana", "Gun", "Hammer", "Bow and Arrow", "Pepper Spray", "Hole"]

    room_list = []
    for i in rooms:
        room_list.append(i)
    cards = []
    for i in range(len(room_list)):
        random_number = randint(0, len(weapon_list)-1)
        weapon_name = weapon_list[random_number]
        cards.append(murder_card(weapon(weapon_name, randint(1, 6)), room_list[randint(0, len(room_list) - 1)], randint(1, 12), [randint(1, 6)]))
        weapon_list.remove(weapon_name)

    for i in range(len(room_list)):
        random_number = randint(0, len(room_list)-1)
        room_name = room_list[random_number]
        cards.append(alabi_card(room_name, randint(1, 12), [randint(1, 6)]))
        room_list.remove(room_name)

    #Note: Use isinstance(object, type) to check if its a murder or alibi card

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
    activated_dict = {}
    for x in player_dic:
        activated_dict[x] = []
        for card in player_dic[x].weapon_cards:
            if card not in activated_dict[x]:
                for i in card.activation_number:
                    if i == roll[0]:
                        activated_dict[x].append(card)
    for x in activated_dict:
        print(x, "it\'s your turn!")
        if(len(activated_dict[x]) == 0):
            print("You activated no cards this round...")
        else:
            has_murder_card = False
            murder_card_count = 0
            has_alibi_card = False
            alibi_card_count = 0
            for card in activated_dict[x]:
                if(isinstance(card, murder_card) == True):
                    murder_card_count += 1
                    has_murder_card = True
                elif(isinstance(card, alabi_card) == True):
                    alibi_card_count += 1
                    has_alibi_card = True

            if(has_murder_card == True and murder_card_count > 1):
                print("Congragulations! You have the chance to murder! Choose wisely.")
                for card in activated_dict[x]:
                    if(isinstance(card, murder_card) == True):
                        print(card.weapon_used.name)
                        print(card.weapon_used.damage)
                        print(card.location.name)
                        print(card.drop_number)
                        print(card.activation_number)
                        print()
                choice = input("Which weapon do you want to use: ")

            elif(has_murder_card == True and murder_card_count == 1):
                for card in activated_dict[x]:
                    if(isinstance(card, murder_card) == True):
                        print("You used a", card.weapon_used.name, "which deals", card.weapon_used.damage, "at", card.location.name)

            elif(has_murder_card == False):
                print("Sorry! You can't murder this round. Maybe next time")
            if(has_alibi_card == True and alibi_card_count > 1):
                print("Congragulations! You have the chance to move! Choose wisely.")
                for card in activated_dict[x]:
                    if(isinstance(card, alabi_card) == True):
                        print(card.location)
                        print(card.drop_number)
                        print(card.activation_number)
            elif(has_alibi_card == True and alibi_card_count == 1):
                for card in activated_dict[x]:
                    if (isinstance(card, murder_card) == True):
                        print("You went to", card.location.name)
            elif(has_alibi_card == False):
                print("Sorry! You have no chance to move. Hope we see you next round!")
            print()
    hello = input("Stop. ")

def create_character(cards):
    name = input("Hello player, what's your name? ")
    player = Player(name)
    for i in range(7):
        random_card = randint(0, len(cards) - 1)
        player.weapon_cards.append(cards[random_card])
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
    cards = load_cards(rooms)

    player_dic = {}
    for i in range(number_of_players):
        player = create_character(cards)
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
