import random

class Territories:
    territoryCord = [[7,2], [23,2], [37,2], [12,7], [23,9], [35,9], [8,15], [14,14], [24,14],[8,20], [14,20], [34,19]]
    
    def territory_claim(gameMap, x, y, oldChar, newChar):
        mapWidth = len(gameMap)
        mapHeight = len(gameMap[0])

        if oldChar is None:
            oldChar = gameMap[x][y]

        if gameMap[x][y] != oldChar:
            return
        gameMap[x][y] = newChar
        if x > 0: # left
            Territories.territory_claim(gameMap, x-1, y, oldChar, newChar)

        if y > 0: # up
            Territories.territory_claim(gameMap, x, y-1, oldChar, newChar)

        if x < mapWidth-1: # right
            Territories.territory_claim(gameMap, x+1, y, oldChar, newChar)

        if y < mapHeight-1: # down
            Territories.territory_claim(gameMap, x, y+1, oldChar, newChar)
    def is_adjacent(gameMap, xCoor, yCoor):
        mapWidth = len(gameMap)
        mapHeight = len(gameMap[0])
        
        for idx in range(-2,3):
            for idx2 in range(-2,3):
                if 0 <= xCoor+idx < mapWidth and 0 <= yCoor+idx2 < mapHeight:
                    if gameMap[xCoor+idx][yCoor+idx2] == "-":
                        return True
        return False
    
    def can_steal_territory(gameMap):
        mapWidth = len(gameMap)
        mapHeight = len(gameMap[0])
        
        for x in range(mapWidth):
            for y in range(mapHeight):
                if gameMap[x][y] == "+":
                    if Territories.is_adjacent(gameMap, x, y):
                        return True
        return False
    
    def mapPrint(mapForPrint):
        for y in range(len(mapForPrint[0])):
            for x in range(len(mapForPrint)):
                print(mapForPrint[x][y], end="")
            print()
                
    def territory_steal(gameMap, xHave, yHave, xTake, yTake):
        taked = gameMap[xHave][yHave]
        taker = gameMap[xTake][yTake]
        Territories.territory_claim(gameMap, xTake, yTake, None, taker)
        Territories.territory_claim(gameMap, xHave, yHave, None, taker)
    def territory_pre_steal(gameMap, xHave, yHave, xTake, yTake):
        taked = gameMap[xHave][yHave]
        taker = gameMap[xTake][yTake]
        Territories.territory_claim(gameMap, xHave, yHave, None, '+')
        Territories.territory_claim(gameMap, xTake, yTake, None, '-')
        canTake = Territories.can_steal_territory(gameMap)
        Territories.territory_claim(gameMap, xTake, yTake, None, taked)
        Territories.territory_claim(gameMap, xHave, yHave, None, taker)
        return canTake
    
    def getWorldFromTextMap(textmap):
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
    def isTakeValid(gameMap, char, territoryChose):
        return (gameMap [Territories.territoryCord[territoryChose-1][0]][Territories.territoryCord[territoryChose-1][1]] == char)

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
worldMap = Territories.getWorldFromTextMap(textMap)
#for i in range(len(Territories.territoryCord)):
    #print(worldMap[Territories.territoryCord[i][0]][Territories.territoryCord[i][1]])

validInputPlayerCount = False
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

TERRITORYAMOUNT = 12
player = [None] * playerCount
order = list(range(0, playerCount))
playerAssignments = "ABCD"
for idx in range(playerCount):
    player[idx] = input("What is the name of player %d?: " % (idx+1))
    
random.shuffle(player)
print("The order of play will be:")
for idx in range(playerCount):
    print("player %s: %s" % (playerAssignments[idx], player[order[idx]]))
          
input("click enter to play")
turn = 0
gameComplete = False
pickTerritory = 0
allTerritoriesPicked = False
while not allTerritoriesPicked:
    pickIsValid = False
    while not pickIsValid:
        territoryChosen = input("which territory would %s like to choose (input in format # ex '1')?: " % player[pickTerritory % playerCount])
        try: 
            territoryChosen = int(territoryChosen)
        except: 
            print("invalid Input")
        else:
            if territoryChosen > 0 and territoryChosen <= TERRITORYAMOUNT:
                if Territories.isTakeValid(worldMap, "?", territoryChosen):  
                    pickIsValid = True
                else:
                    print("That territory can not be taken")
            else: 
                print("invalid Input")
            
    Territories.territory_claim(worldMap, Territories.territoryCord[territoryChosen-1][0], Territories.territoryCord[territoryChosen-1][1], None, playerAssignments[pickTerritory % playerCount])
    if pickTerritory>10: Territories.mapPrint(worldMap)
    pickTerritory +=1
    allTerritoriesPicked = True
    for i in range(TERRITORYAMOUNT):
         if Territories.isTakeValid(worldMap, "?", i+1):
             allTerritoriesPicked = False
             break
while not gameComplete:
    validStealTerritory = False
    validAttackerTerritory = False
    personsTurn = turn % playerCount
    playerInUse = player[personsTurn]
    territoryAttacker = input("which territory would %s like to attack from(input in format # ex '1')?: " % player[personsTurn])
    try:
        territoryAttacker = int(territoryAttacker)
    except:
        print("invalid input")
    else:
        print("hi")
    #IFHASTERRITORY
    while not validStealTerritory:
        territorySteal = input("which territory would %s like to attack(input in format # ex '1')?: " % player[personsTurn])
        try:
            territorySteal = int(territorySteal)
        except:
            print("invalid input")
        else:
            if Territories.isTakeValid(worldMap, playerAssignments[personsTurn], territorySteal):
                print("you can not take your own territory")
            else:
                if not Territories.territory_pre_steal(worldMap, Territories.territoryCord[territoryAttacker-1][0],Territories.territoryCord[territoryAttacker-1][1], Territories.territoryCord[territorySteal-1][0],Territories.territoryCord[territorySteal-1][1]):
                    print("Can not reach territory")
                else:
                    validStealTerritory = True
                
        
    
    Territories.territory_steal(worldMap, Territories.territoryCord[territoryAttacker-1][0],Territories.territoryCord[territoryAttacker-1][1], Territories.territoryCord[territorySteal-1][0],Territories.territoryCord[territorySteal-1][1])
    print(playerInUse)
    turn += 1
