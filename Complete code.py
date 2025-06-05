from pynput.keyboard import Key, Controller
import random
class Force:
    units = 0
    def __init__(self, unit):
        self.units = unit
        print("units: ", self.units)

    # roll dice and see who wins
    def Attack(self, p2):
        dice1 = random.randint(1 ,6)
        dice2 = random.randint(1, 6)

        if (dice1 == dice2):
            return self.Attack(p2)

        # player 1 dice is higher
        if (dice1 > dice2):
            p2.units -= 1
            print("player 1 wins (p1: %s units left, p2: %s units left)" % (self.units, p2.units))

        # player 2 dice is higher
        if (dice2 > dice1):
            self.units -= 1
            print("player 2 wins (p1: %s units left, p2: %s units left)" % (self.units, p2.units))

def main_Menu_Header():
    program_name = "Welcome To Conquest: A Territory Strategy Game!"
    version = "1.0"
    header_text = f"{program_name} - Version {version}"
    header_width = 100
    print()
    print("=" * header_width)
    print(header_text.center(header_width))
    print("=" * header_width)
    print()

    def show_instructions():
        program_name = "Instructions on How to Play Conquest!"
        header_text = f"{program_name}"
        header_width = 100
        print()
        print("=" * header_width)
        print(header_text.center(header_width))
        print("=" * header_width)
        print()
        instructions = ["1. Rule 1", "2. Rule 2", "3. Rule 3"]
        print("Instructions:")
        for line in instructions:
            print(line)
        print()

    def main_Menu():
        choice = input("Would you like to see the instructions? (yes/no): ").strip()
        if choice == "yes" or choice == "Yes" or choice == "Y" or choice == "y":
            show_instructions()
        elif choice == "no" or choice == "No" or choice == "N" or choice == "n":
            print("\nAlright, let's proceed to the game!\n")
        
        else: 
            print("Enter a valid input.")

    main_Menu()

main_Menu_Header()

def checkWinner (plyrs):
    for idx in range(len(plyrs)):
        if winner:
            return True, player[idx]
    return False, None

#MAIN PGM
validInputPlayerCount = 0
while not validInputPlayerCount:
    playerCount = input("How many players will be playing? (2-4): ")
    try:
        playerCount = int(playerCount)
    except:
        print("Invalid player count, try again!")
    else:
        if playerCount >4 or playerCount <2:
            print("Invalid player count, try again!")
        else:
            validInputPlayerCount = True
player = [None] * playerCount
order = list(range(0, playerCount))
for idx in range(playerCount):
    player[idx] = input ("What is the name of player %d?: " % (idx+1))
random.shuffle(player)
print ("The order of play will be:")
for idx in range (playerCount):
    print(player[order[idx]])
keyboard = Controller()
play = input("click enter to play")
if play == keyboard.press(Key.enter):
    turn = 0
    gameComplete = False
    while not gameComplete:
        checkWinner(player)
        playerInUse = player[turn%playerCount]
        print("It is %s's turn" % playerInUse)
