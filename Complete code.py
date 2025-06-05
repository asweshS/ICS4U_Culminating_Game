from pynput.keyboard import Key, Controller
import random

class Force:
    units = 0

    def __init__(self, unit):
        self.units = unit
        print("units: ", self.units)

    def Attack(self, p2):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        if dice1 == dice2:
            return self.Attack(p2)

        if dice1 > dice2:
            p2.units -= 1
            print("player 1 wins (p1: %s units left, p2: %s units left)" % (self.units, p2.units))
        else:
            self.units -= 1
            print("player 2 wins (p1: %s units left, p2: %s units left)" % (self.units, p2.units))

class Territories:
    territoryCord = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

    @staticmethod
    def territory_claim(gameMap, x, y, oldChar, newChar):
        mapWidth = len(gameMap)
        mapHeight = len(gameMap[0])

        if oldChar is None:
            oldChar = gameMap[x][y]

        if gameMap[x][y] != oldChar:
            return
        gameMap[x][y] = newChar

        if x > 0:
            Territories.territory_claim(gameMap, x - 1, y, oldChar, newChar)
        if y > 0:
            Territories.territory_claim(gameMap, x, y - 1, oldChar, newChar)
        if x < mapWidth - 1:
            Territories.territory_claim(gameMap, x + 1, y, oldChar, newChar)
        if y < mapHeight - 1:
            Territories.territory_claim(gameMap, x, y + 1, oldChar, newChar)

    @staticmethod
    def is_adjacent(gameMap, xCoor, yCoor):
        for idx in range(-2, 3):
            for idx2 in range(-2, 3):
                nx, ny = xCoor + idx, yCoor + idx2
                if 0 <= nx < len(gameMap) and 0 <= ny < len(gameMap[0]):
                    if gameMap[nx][ny] == "-":
                        return True
        return False

    @staticmethod
    def can_steal_territory(gameMap):
        for x in range(worldWidth):
            for y in range(worldHeight):
                if gameMap[x][y] == "+":
                    if Territories.is_adjacent(gameMap, x, y):
                        return True
        return False

    @staticmethod
    def territory_steal(gameMap, xHave, yHave, xTake, yTake):
        taked = gameMap[xHave][yHave]
        taker = gameMap[xTake][yTake]
        Territories.territory_claim(gameMap, xHave, yHave, None, '+')
        Territories.territory_claim(gameMap, xTake, yTake, None, '-')
        if Territories.can_steal_territory(gameMap):
            Territories.territory_claim(gameMap, xTake, yTake, None, taker)
            Territories.territory_claim(gameMap, xHave, yHave, None, taker)
        else:
            Territories.territory_claim(gameMap, xTake, yTake, None, taked)
            Territories.territory_claim(gameMap, xHave, yHave, None, taker)

class intro:
    @staticmethod
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

    @staticmethod
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

    @staticmethod
    def main_Menu():
        validInput = False
        while not validInput:
            choice = input("Would you like to see the instructions? (yes/no): ").strip()
            if choice.lower() in ["yes", "y"]:
                intro.show_instructions()
                validInput = True
            elif choice.lower() in ["no", "n"]:
                print("\nAlright, let's proceed to the game!\n")
                validInput = True
            else:
                print("Enter a valid input.")

def checkWinner(plyrs):
    for idx in range(len(plyrs)):
        if winner:
            return True, plyrs[idx]
    return False, None

# ===== MAIN PROGRAM =====
validInputPlayerCount = False
intro.main_Menu_Header()
intro.main_Menu()

while not validInputPlayerCount:
    playerCount = input("How many players will be playing? (2-4): ")
    try:
        playerCount = int(playerCount)
    except:
        print("Invalid player count, try again!")
    else:
        if playerCount > 4 or playerCount < 2:
            print("Invalid player count, try again!")
        else:
            validInputPlayerCount = True

player = [None] * playerCount
order = list(range(playerCount))
playerAssignments = "ABCD"

for idx in range(playerCount):
    player[idx] = input("What is the name of player %d?: " % (idx + 1))

random.shuffle(order)
print("The order of play will be:")
for idx in range(playerCount):
    print("player %s: %s" % (playerAssignments[idx], player[order[idx]]))

input("Click enter to play")
turn = 0
gameComplete = False

# Placeholder values for map size and winner check
worldWidth = 10
worldHeight = 10
winner = False

while not gameComplete:
    personsTurn = turn % playerCount
    playerInUse = player[personsTurn]
    print("It's", playerInUse + "'s turn.")
    turn += 1


player = [None] * playerCount
order = list(range(0, playerCount))
for idx in range(playerCount):
    player[idx] = input ("What is the name of player %d?: " % (idx+1))
random.shuffle(player)
print ("The order of play will be:")
for idx in range (playerCount):
    print(player[order[idx]])
keyboard = Controller()
play = input("click enter to play ")
if play == keyboard.press(Key.enter):
    turn = 0
    gameComplete = False
    while not gameComplete:
        checkWinner(player)
        playerInUse = player[turn%playerCount]
        print("It is %s's turn" % playerInUse)
else: 
    print("Try Pressing Enter to Play!")
