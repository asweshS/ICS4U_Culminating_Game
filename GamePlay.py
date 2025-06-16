import random
import os
import saveFile

class Player:
    investment = 0

    def __init__(self, name,troops = 100, money =0,territories=[]):
        
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
        self.money+=1000
    def balance(self):
        print(f"New balance: ${self.money}")
    def trp(self):
        print(f"New troop count: ${self.money}")
    def buy_troops(self, amountOfTroops):
        self.troops += amountOfTroops
        self.money -= 100 * amountOfTroops
        print(f"{self.name} has bought {amountOfTroops} troops.")
        self.balance()


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

# force is from the perspective of the attacker
class Force:
    units = 0
    strength = 0
    territory = []
    assignments = "ABCD"
    
    # which player this class belongs to
    playNum = 0
    def __init__(self, unit, terr, playerNum, assgnmnts ):
        self.units = int(unit)
        self.territory = terr
        self.playNum = playerNum
        print("%s's units: %s" %(assgnmnts[playerNum], self.units))

    # roll dice and see who wins, defense is p2
    def Attack(self, p2, terr, player1, player2, selfTroops, p2Troops):

        # when attacker doesn't have enough units
        if (self.units <= 1):
            print("You cannot attack, you dont have enough units")
            return

        # attacker dice
        dice1 = random.randint(1, 6) * selfTroops
        # defense dice
        dice2 = random.randint(1, 6) * p2Troops

        # attacker dice is higher
        if (dice1 > dice2):
            p2.units -= 100
            print("%s wins!" % player1)
            print("%s: %s units left, %s: %s units left)" % (player1, self.units, player2, p2.units))
            return True
        # defender dice is higher or dice are even
        if (dice2 > dice1 or dice1 == dice2):
            self.units -= 100#(50 - terr.defense) + self.strength
            print("%s wins!" % player2)
            print("%s: %s units left, %s: %s units left)" % (player1, self.units, player2, p2.units))
            return False            
        # if defender is out of units, then give land to attacker
        if (p2.units == 0): 
            return True

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
            territorySteal = input("Attack which territory %s (player %s)?: " % (playerInUse, plyrAssm[persTurn]))
            try:
                territorySteal = int(territorySteal)
            except:
                print("Invalid input!")
            else:
                if territorySteal<=1 or territorySteal>12: 
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
        if frcPlyr[persTurn].Attack(frcPlyr[playerBeingAttackedNumber], self.territory_coords[territorySteal - 1],playerInUse, playerList[playerBeingAttackedNumber], playerClassInstance[persTurn].troops, playerClassInstance[playerBeingAttackedNumber].troops):
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
        
    print("These are the saves:")

    for i in range(3):
        if saveFile.doesFileHaveData(i+1):
            print("Load Save %d" % (i + 1))
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
        player_instance = saveFile.loadSave(whichSave)
        playerCount = len(player_instance)
        forcePlayer = [None] * playerCount
        for idx in range(playerCount):
            print("player %s: %s" % (assignments[idx], player_instance[idx]))
            playerTerritories.append(player_instance[idx].territories)
            playerNames.append(str(player_instance[idx].name))
            playerTroops.append(str(player_instance[idx].troops))
        for plyr in range(playerCount):
            forcePlayer[plyr] = Force(playerTroops[plyr], playerTerritories[plyr], plyr, assignments)
        input("Press Enter to continue...")
        
    else:
        firstSave = True
        print("Starting a new game on save %d..." % whichSave)
        
    

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
            forcePlayer[plyr] = Force(troopsForPlay[plyr], playerTerritories[plyr], plyr, assignments)
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
            print("Balance: %s" % player_instance[current].money)
            print("Troops: %s" % player_instance[current].troops)
            terrPrint = ""
            for i in range(len(playerTerritories[current])):
                terrPrint += str(playerTerritories[current][i])
                terrPrint += " " 
            print("Territories: %s" % terrPrint)
            for turnChoice in range(2):
                print()
                validInputTurnChoice = False
                while not validInputTurnChoice:
                    validInputTurnChoice = True 
                    print("What will you do for your %s turn?" % picksForEach[turnChoice])
                    print("1. Invest")
                    print("2. Purchase troops")
                    print("3. Attack")
                    decision = input("Enter (1,2, or 3) : ")
                if decision =="1":
                    player_instance[current].invest()
                    print("%s has invested $1000!" % player_instance[current].name)
                elif decision =="2":
                    validTroopsBuy = False
                    while not validTroopsBuy:
                        numberOfTroopsBuy = input("How many troops would you like to buy? ($100 each): ")
                        try:
                            numberOfTroopsBuy = int(numberOfTroopsBuy)
                        except:
                            print("Invalid input!")
                        else:
                            if numberOfTroopsBuy < 0:
                                print("You can not buy negative troops!")
                            elif numberOfTroopsBuy * 100 > player_instance[current].money:
                                print("You do not have enough money to buy that many troops!")
                            else:
                                validTroopsBuy = True
                    player_instance[current].buy_troops(numberOfTroopsBuy)
                elif decision == "3":
                    territories.attacking_turn(player_instance, playerTerritories, current, assignments, playerCount, forcePlayer, player_instance)
                for i in range(playerCount):
                    if len(playerTerritories[i]) == 12:
                        print("%s (Player %s) is the winner!" % (player_instance[i].name, assignments[i]))
                        gameComplete = True
                        break
            player_instance[current].balance()
            player_instance[current].trp()
            if (turn+1) % playerCount == 0:
                print("All players have had a turn, $500 + $100 per territory owned added to each players balance")
                print("Continuing to round %s" % ((turn+1)//4 + 1))

                saveFileAtEndOfRound = input("Would you like to save the game and leave? (y/n): ").strip().lower()
                if saveFileAtEndOfRound == 'y':
                    saveFile.savingFile(whichSave,player_instance, playerCount)
                    print("Game saved!")
                    break

            input("Click enter to advance to %s's turn!" % player_instance[(current+1)%playerCount].name)
            turn += 1
