######################################
# File Name: GameEngine.py
# Author(s): Devan Lucas
# Description: This program contains the 'Map' and 'Territories' class and game logic for the game.
# History:
# 2025-06-04 Created initial player input
# 2025-06-05 Added the 'Territoty' class
# 2025-06-09 Added picking territory logic
# 2025-06-11 Created the game map
# 2025-06-12 Fixed 'Territory' class, added 'Map' class, and fixed logic and errors in code.
######################################
import random
import os
class Map:
    def __init__(self, textmap):
        self.map = self.get_world_from_text_map(textmap)

    def get_world_from_text_map(self, textmap):
        textmap = textmap.strip().split('\n')
        worldWidth = len(textmap[0])
        worldHeight = len(textmap)
        world = []
        for i in range(worldWidth):
            world.append([''] * worldHeight)
        for x in range(worldWidth):
            for y in range(worldHeight):
                world[x][y] = textmap[y][x]
        return world

    def print_map(self):
        def print_row(y):
            if y >= len(self.map[0]):
                return
            def print_col(x):
                if x >= len(self.map):
                    print()
                    return
                print(self.map[x][y], end="")
                print_col(x + 1)
            print_col(0)
            print_row(y + 1)
        print_row(0)


class Territories:
    def __init__(self, map_obj, territory_coords):
        self.map = map_obj.map
        self.territory_coords = territory_coords

    def territory_claim(self, x, y, oldChar, newChar):
        mapWidth = len(self.map)
        mapHeight = len(self.map[0])
        if oldChar is None:
            oldChar = self.map[x][y]
        if self.map[x][y] != oldChar:
            return
        self.map[x][y] = newChar
        if x > 0:
            self.territory_claim(x - 1, y, oldChar, newChar)
        if y > 0:
            self.territory_claim(x, y - 1, oldChar, newChar)
        if x < mapWidth - 1:
            self.territory_claim(x + 1, y, oldChar, newChar)
        if y < mapHeight - 1:
            self.territory_claim(x, y + 1, oldChar, newChar)

    def is_adjacent(self, xCoor, yCoor):
        mapWidth = len(self.map)
        mapHeight = len(self.map[0])
        for idx in range(-2, 3):
            for idx2 in range(-2, 3):
                if 0 <= xCoor + idx < mapWidth and 0 <= yCoor + idx2 < mapHeight:
                    if self.map[xCoor + idx][yCoor + idx2] == "-":
                        return True
        return False

    def can_steal_territory(self):
        mapWidth = len(self.map)
        mapHeight = len(self.map[0])
        for x in range(mapWidth):
            for y in range(mapHeight):
                if self.map[x][y] == "+":
                    if self.is_adjacent(x, y):
                        return True
        return False

    def territory_steal(self, xHave, yHave, xTake, yTake):
        taked = self.map[xHave][yHave]
        taker = self.map[xTake][yTake]
        self.territory_claim(xHave, yHave, None, '+')
        self.territory_claim(xTake, yTake, None, '-')
        canTake = self.can_steal_territory()
        self.territory_claim(xTake, yTake, None, taker)
        self.territory_claim(xHave, yHave, None, taked)
        return canTake

    def is_take_valid(self, char, territoryChose):
        x, y = self.territory_coords[territoryChose - 1]
        return self.map[x][y] == char

    def attacking_turn(self, playerInUse, playerAssignments, plyrTerrClm, persTurn, plyrAssm, plyrAmount):
        validStealTerritory = False
        validAttackerTerritory = False

        while not validAttackerTerritory:
            territoryAttacker = input("Attack from which territory %s (player %s)?: " % (playerInUse, playerAssignments[persTurn]))
            try:
                territoryAttacker = int(territoryAttacker)
            except:
                print("Invalid input!")
            else:
                if not (territoryAttacker in plyrTerrClm[persTurn]):
                    print("You do not own this territory!")
                else:
                    validAttackerTerritory = True

        while not validStealTerritory:
            territorySteal = input("Attack which territory %s (player %s)?: " % (playerInUse, playerAssignments[persTurn]))
            try:
                territorySteal = int(territorySteal)
            except:
                print("Invalid input!")
            else:
                if self.is_take_valid(plyrAssm[persTurn], territorySteal):
                    print("You can not take your own territory!")
                else:
                    if not self.territory_steal(*self.territory_coords[territoryAttacker - 1], *self.territory_coords[territorySteal - 1]):
                        print("Can not reach territory!")
                    else:
                        validStealTerritory = True

        for idx in range(plyrAmount):
            if territorySteal in plyrTerrClm[idx]:
                playerBeingAttackedNumber = idx

        self.territory_claim(*self.territory_coords[territorySteal - 1], None, playerAssignments[persTurn])
        map_printer = Map("")  # create a dupelicate Map object just for printing
        map_printer.map = self.map
        map_printer.print_map()
        plyrTerrClm[playerBeingAttackedNumber].remove(territorySteal)
        plyrTerrClm[persTurn].append(territorySteal)
TERRITORY_COORDS = [
    [7, 2], [23, 2], [37, 2], [12, 7], [23, 9], [35, 9],
    [8, 15], [14, 14], [24, 14], [8, 20], [14, 20], [34, 19]
]

textMap = """
███████████████████████████████████████████████
█████???????????███????███████████???????██████
████??????1???????█??????????██?????????????███
███???????????????█?????2?????██?????3?????████
██????█████████████????????????█?????????██████
████████??????????██████████████?????██████████
█████???????????????█??????????██??███???██████
████?????????4??????█????5?????█████??????█████
██████████??????????█????????███???????████████
█████████████████████????????█?????????????████
████??████??????????██████████████????6?????███
████????███?????????█????????????██??????????██
█████????███????8???█??????9??????████████???██
██████?????█????????█????????????██?????███??██
██████??7??█????????█???????????██?????████████
█████??????██████████??????██????█??????███████
████??????██???????██???????█████████????██████
████??????█?????????█????????████████??????████
███████████????11???██????███████████??????████
███???????█?????????███████??█??????█???????███
███???????███????????????????██????????????████
███???10????██████????????????█???12????????███
██???????????????████???????████???????████████
███████████████████████████████████████████████
"""
game_map = Map(textMap)
territories = Territories(game_map, TERRITORY_COORDS)

# === PLAYER SETUP ===
while True:
    try:
        playerCount = int(input("How many players? (2-4): "))
        if 2 <= playerCount <= 4:
            break
        print("Invalid number.")
    except:
        print("Invalid input.")

TERRITORYAMOUNT = 12
assignments = "ABCD"
players = [input("Name for player %s: " % (i+1)) for i in range(playerCount)]
playerTerritories = [[] for n in range(playerCount)]

random.shuffle(players)
print("Turn order:")
for idx in range(playerCount):
    print("player %s: %s" % (assignments[idx], players[idx]))

input("Press Enter to begin...")

#pick territories
pick = 0
gameComplete = False
pickTerritory = 0
allTerritoriesPicked = False
while not allTerritoriesPicked:
    isPickValid = False
    current = pick % playerCount
    while not isPickValid:
        # Show the map before each pick
        game_map.print_map()
        try:
            choice = int(input("%s (player %s), pick an unclaimed territory (1-12): " % (players[current],assignments[current])) )
        except:
            print("Invalid input!")
        else:
            if 1 <= choice <= 12 and territories.is_take_valid("?", choice):
                # Ask for confirmation
                confirm = input("You selected territory %d. Confirm selection? (y/n): " % choice).strip().lower()
                if confirm == 'y':
                    isPickValid = True
                else:
                    print("Selection cancelled. Please pick again.")
            else:
                print("Territory %s is not avaliable!" % choice)
    x, y = TERRITORY_COORDS[choice - 1]
    territories.territory_claim(x, y, None, assignments[current])
    playerTerritories[current].append(choice)
    if pick > 10:
        game_map.print_map()
    pick += 1
    allTerritoriesPicked = True
    for i in range(TERRITORYAMOUNT):
         if territories.is_take_valid("?", i+1):
             allTerritoriesPicked = False
             break
    # Clear the screen for the next player
    os.system('cls')

# === MAIN GAME LOOP ===
turn = 0
while not gameComplete:
    current = turn % playerCount
    print("%s's (player %s) Turn" % ((players[current], assignments[current])))

    ##if decide attack and win 
    territories.attacking_turn(players[current], assignments, playerTerritories, current, assignments, playerCount)
    for i in range(playerCount):
        if len(playerTerritories[i]) == 12:
            print("%s (Player %s) is the winner!" % (players[i], assignments[i]))
            gameComplete = True
    turn += 1
