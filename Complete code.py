import random
import time, sys
import os 

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
    def main_Menu():
        def typewriter_txt(msg):
            for char in msg:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.02)

        TITLE = "Conquest: A Territory Strategy Game"
        load_game = "\nLaunching Game...\n"
        typewriter_txt(load_game)
        time.sleep(1)
        loaded_game = f"Successfully Loaded '{TITLE}'\n"
        typewriter_txt(loaded_game)

        def print_header():
            os.system('cls')
            header_width = 80
            print("\n" + "=" * header_width)
            print(f"Welcome To {TITLE}!".center(header_width))
            print("Version 1.0".center(header_width))
            print("=" * header_width + "\n")

        def show_instructions():
            os.system('cls')
            header_width = 80
            print("-" * header_width)
            print("Instructions on How to Play Conquest!".center(header_width))
            print("-" * header_width)
            print()
            instructions = [
                "1. Each player takes turns to conquer territories.",
                "2. Attack adjacent territories to expand your control.",
                "3. The last player remaining wins the game."
            ]
            for line in instructions:
                print(line)
            print()
            input("Press Enter to return to the main menu...")

        def main_Menu_logic():
            while True:
                print_header()
                print("MAIN MENU".center(80, "-"))
                print("1. See Instructions")
                print("2. Start Game")
                print("3. Exit")
                choice = input("\nEnter your choice (1-3): ").strip()
                if choice == "1":
                    show_instructions()
                elif choice == "2":
                    print("\nStarting the game...\n")
                    time.sleep(1)
                    return True
                elif choice == "3":
                    print("\nExiting the game. Goodbye!\n")
                    sys.exit()
                else:
                    print("Enter a valid input (1-3).")
                    time.sleep(1)

        main_Menu_logic()

# ===== MAIN PROGRAM =====
def clear_screen():
    os.system('cls')

validInputPlayerCount = False
intro.main_Menu()

while not validInputPlayerCount:
    clear_screen()
    print("=" * 80)
    print("PLAYER SETUP".center(80))
    print("=" * 80)
    playerCount = input("How many players will be playing? (2-4): ")
    try:
        playerCount = int(playerCount)
    except:
        print("Invalid player count, try again!")
        time.sleep(1)
    else:
        if playerCount > 4 or playerCount < 2:
            print("Invalid player count, try again!")
            time.sleep(1)
        else:
            validInputPlayerCount = True

player = [None] * playerCount
order = list(range(playerCount))
playerAssignments = "ABCD"

clear_screen()
print("=" * 80)
print("PLAYER NAMES".center(80))
print("=" * 80)
for idx in range(playerCount):
    player[idx] = input(f"Enter the name of player {idx + 1}: ")

random.shuffle(order)
clear_screen()
print("=" * 80)
print("ORDER OF PLAY".center(80))
print("=" * 80)
for idx in range(playerCount):
    print(f"Player {playerAssignments[idx]}: {player[order[idx]]}")
input("\nPress Enter to begin the game...")

turn = 0
gameComplete = False

# Placeholder values for map size and winner check
worldWidth = 10
worldHeight = 10
winner = False

while not gameComplete:
    clear_screen()
    print("=" * 80)
    print(f"TURN {turn + 1}".center(80))
    print("=" * 80)
    personsTurn = turn % playerCount
    playerInUse = player[personsTurn]
    print(f"It's {playerInUse}'s turn.\n")
    # ...game logic for the player's turn goes here...
    input("Press Enter to end your turn...")
    turn += 1
