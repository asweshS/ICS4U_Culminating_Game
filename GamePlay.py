
######################################
# File Name: GamePlay.py
# Author(s): Devan Lucas and Andrew Urquhart
# Description: This program contains the GameEngine and Player files into one program
# and makes them usable with the game.
# History:
# 2025-06-13 Creation
# 2025-06-14 added usability with other files
# 2025-06-15 Bug fixes
# 2025-06-16 Bug Fixes
# 2025-06-17 Took out Force class and changed logic
######################################
import random
import os
import saveFile
import sys
import time
import ForceCode
class Player:
    investment = 0

    def __init__(self, name,troops, money,territories=[]):
        
        self.name = name
        self.troops = int(troops)
        self.money = int(money)
        self.territories = []
        for i in range(len(territories)):
            self.territories.append(territories[i])
            
    def income(self):
        self.daily_income = 500 + (len(self.territories) * 100)
        self.money += self.daily_income

    def invest(self):
        investment = random.randint(600, 1200)
        self.money+=investment
        return investment

    def buy_troops(self, amountOfTroops, forcePlay):
        self.troops += amountOfTroops
        self.money -= 10 * amountOfTroops
        print(f"{self.name} has bought {amountOfTroops} troops!")


    def __str__(self):
        name = self.name
        return str(name)

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
        os.system('cls')
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

    def attacking_turn(self, playerList, plyrTerrClm, persTurn, plyrAssm, plyrAmount, frcPlyr, playerClassInstance):
        playerInUse = playerList[persTurn] 
        validStealTerritory = False
        validAttackerTerritory = False

        while not validAttackerTerritory:
            territoryAttacker = input("Attack from which territory %s (player %s)?: " % (playerInUse, plyrAssm[persTurn]))
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
            territorySteal = input("Attack which territory %s (player %s) *(Input 'c' to cancel attack)?: " % (playerInUse, plyrAssm[persTurn]))
            if territorySteal.lower() == 'c':
                print("Attack cancelled.")
                return
            try:
                territorySteal = int(territorySteal)
            except:
                print("Invalid input!")
            else:
                if territorySteal<1 or territorySteal>12: 
                    print("Invalid input!") 
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
        if frcPlyr[persTurn].Attack(frcPlyr[playerBeingAttackedNumber],playerInUse, playerList[playerBeingAttackedNumber], playerClassInstance[persTurn].troops, playerClassInstance[playerBeingAttackedNumber].troops):
            self.territory_claim(*self.territory_coords[territorySteal - 1], None, plyrAssm[persTurn])
            plyrTerrClm[playerBeingAttackedNumber].remove(territorySteal)
            plyrTerrClm[persTurn].append(territorySteal)
        map_printer = Map("")  # create a dupelicate Map object just for printing
        map_printer.map = self.map
def gamePlay():
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
    picksForEach = ["1st", "2nd"]
    territories = Territories(game_map, TERRITORY_COORDS)
    # === PLAYER SETUP ===
    assignments = "ABCD"
    TERRITORYAMOUNT = 12
    player_instance = [None]*4
    gameComplete = False
    validSave = False
    wasThree = False
    while not validSave:    
        print("These are the saves:")
        numberToLoad = 0 
        for i in range(3):
            if saveFile.doesFileHaveData(i+1):
                print("Load Save %d" % (i + 1))
                numberToLoad += 1
            else:
                print("Create New Save on %d " % (i + 1))
        if numberToLoad == 3:
            wasThree = True
            shouldDelete = input("Would you like to delete a save? (y/n): ").strip().lower()
            if shouldDelete == 'y':
                while True:
                    try:
                        deleteSave = int(input("Which save would you like to delete? (1-3): "))
                    except:
                        print("Invalid input.")
                    else:
                        if deleteSave == 1 :
                            saveFile.clearingFileOne()
                            print("Save %d cleared." % deleteSave)
                            validSave = True
                            break
                        elif deleteSave == 2:
                            saveFile.clearingFileTwo()
                            print("Save %d cleared." % deleteSave)
                            validSave = True
                            break
                        elif deleteSave == 3:
                            saveFile.clearingFileThree()
                            print("Save %d cleared." % deleteSave)
                            validSave = True
                            break
                        else:
                            print("Invalid number.") 
            elif shouldDelete == 'n':
                print("No saves deleted.")
                validSave = True
        else: 
            validSave = True 
    if wasThree:
        print("These are the updated saves:")
        numberToLoad = 0 
        for i in range(3):
            if saveFile.doesFileHaveData(i+1):
                print("Load Save %d" % (i + 1))
                numberToLoad += 1
            else:
                print("Create New Save on %d " % (i + 1))

    while True:
        try:
            whichSave = int(input("Which save would you like to use? (1-3): "))
            if 1 <= whichSave <= 3:
                break
            print("Invalid number.")
        except ValueError:
            print("Invalid input.")

    if saveFile.doesFileHaveData(whichSave):
        firstSave = False
        playerTerritories = []
        playerNames = []
        playerTroops = []
        print("Loading save %d..." % whichSave)
        forcePlayer, player_instance = saveFile.loadSave(whichSave)
#######################################################
        playerCount = len(player_instance)
        for idx in range(playerCount):
            print("player %s: %s" % (assignments[idx], player_instance[idx]))
            playerTerritories.append(player_instance[idx].territories)
            playerNames.append(str(player_instance[idx].name))
            playerTroops.append(str(player_instance[idx].troops))
        input("Press Enter to continue...")
        
    else:
        firstSave = True
        print("Starting a new game on save %d..." % whichSave)
        time.sleep(1)
        os.system('cls')
    

    while firstSave:
        try:
            playerCount = int(input("How many players? (2-4): "))
            if 2 <= playerCount <= 4:
                break
            print("Invalid number.")
        except:
            print("Invalid input.")
    

    if firstSave:
        playerNames = [input("Name for player %s: " % (i+1)) for i in range(playerCount)]
        playerTerritories = [[] for n in range(playerCount)]
        player_instance = [None] * playerCount
    
        random.shuffle(player_instance)

    print("Turn order:")
    for idx in range(playerCount):
        print("player %s: %s" % (assignments[idx], playerNames[idx]))
    input("Press Enter to begin...")

    #pick territories
    if firstSave:
        pick = 0
        allTerritoriesPicked = False
        while not allTerritoriesPicked:
            isPickValid = False
            current = pick % playerCount
            while not isPickValid:
                # Show the map before each pick
                game_map.print_map()
                for idx in range(playerCount):
                    print("player %s: %s" % (assignments[idx], playerNames[idx]))
                try:
                    choice = int(input("%s (player %s), pick an unclaimed territory (1-12): " % (playerNames[current],assignments[current])) )
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
                if not isPickValid: input("Click enter for reinput!")
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
                        
        
        troopsForPlay = []
        forcePlayer = [None]*playerCount
        
        for plyr in range (playerCount): 
            troopsForPlay.append(100* len(playerTerritories[plyr])) 
            forcePlayer[plyr] = ForceCode.Force(troopsForPlay[plyr], playerTerritories[plyr], plyr, assignments)
            player_instance[plyr] = Player(playerNames[plyr], troopsForPlay[plyr], 0, playerTerritories[plyr])
    if not firstSave:
        for idx in range(playerCount):
            tempTerriories = player_instance[idx].territories 
            idx3=0
            for i in (tempTerriories):
                i = int (i)
                tempTerriories[idx3] = i
                idx3 += 1
                x, y =(territories.territory_coords[i-1])
                territories.territory_claim(x, y, None, assignments[idx])
    # === MAIN GAME LOOP ===
    turn = 0
    while not gameComplete:
        current = turn % playerCount
        if not turn<4:
            player_instance[current].income()
        game_map.print_map()
        if len(playerTerritories[current]) == 0:
            print("You do not own any territories!")
        else:
            for idx in range(playerCount):
                print("player %s: %s" % (assignments[idx], (player_instance[idx].name)))
            print()
            print("%s's (player %s) Turn" % ((player_instance[current].name, assignments[current])))
            for turnChoice in range(2):
                print(f"Money: ${player_instance[current].money}")
                print(f"Troop count: {player_instance[current].troops}")
                print(f"Strength: {forcePlayer[current].strength}")
                print(f"Defense: {forcePlayer[current].defense}")
                terrPrint = ""
                for i in range(len(playerTerritories[current])):
                    terrPrint += str(playerTerritories[current][i])
                    terrPrint += " " 
                print("Territories: %s" % terrPrint)
                print()
                validInputTurnChoice = False
                while not validInputTurnChoice:
                    validInputTurnChoice = True 
                    print("What will you do for your %s turn?" % picksForEach[turnChoice])
                    print("1. Invest")
                    print("2. Purchase troops")
                    print("3. Upgrade Strength/Defense")
                    print("4. Attack")

                    decision = input("Enter (1 ,2, 3, or 4): ")

                    # invest
                    if decision =="1":
                        investment = player_instance[current].invest()
                        print("%s has invested $%s!" % (player_instance[current].name, investment ))

                    # buy troops
                    elif decision =="2":
                        validTroopsBuy = False
                        while not validTroopsBuy:
                            numberOfTroopsBuy = input("How many troops would you like to buy? ($10 each): ")
                            try:
                                numberOfTroopsBuy = int(numberOfTroopsBuy)
                            except:
                                print("Invalid input!")
                            else:
                                if numberOfTroopsBuy < 0:
                                    print("You can not buy negative troops!")
                                elif numberOfTroopsBuy * 10 > player_instance[current].money:
                                    print("You do not have enough money to buy that many troops!")
                                else:
                                    validTroopsBuy = True
                        player_instance[current].buy_troops(numberOfTroopsBuy, forcePlayer[current])
                    
                    # upgrade territories
                    elif decision == "3":
                        while True:
                            des = input("Do you want to upgrade army strength or territory defense? (1 or 2)?: ")
                            if (des == "1"):
                                # upgrade units in the 
                                forcePlayer[current].buyStrength(player_instance[current])
                                break
                            if (des == "2"):
                                forcePlayer[current].buyDefense(player_instance[current])
                                break
                            else: 
                                print("Invalid input, try again")

                    # attack
                    elif decision == "4":
                        territories.attacking_turn(player_instance, playerTerritories, current, assignments, playerCount, forcePlayer, player_instance)
                    else: 
                        print("Invalid input, try again\n\n")
                        validInputTurnChoice = False
                for i in range(playerCount):
                    if len(playerTerritories[i]) == 12:
                        print("%s (Player %s) is the winner!" % (player_instance[i].name, assignments[i]))
                        gameComplete = True
                        break
            if (turn+1) % playerCount == 0:
                print("All players have had a turn, $500 + $100 per territory owned added to each players balance")
                for idx in range(playerCount):
                    player_instance[idx].income()
                print("Continuing to round %s" % ((turn+1)//4 + 1))

                saveFileAtEndOfRound = input("Would you like to save the game and leave? (y/n): ").strip().lower()
                if saveFileAtEndOfRound == 'y':
                    saveFile.savingFile(whichSave,player_instance, forcePlayer)
                    print("Game saved!")
                    break

            input("Click enter to advance to %s's turn!" % player_instance[(current+1)%playerCount].name)
            turn += 1
gamePlay()
