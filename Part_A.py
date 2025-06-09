import random
class Territories:
    territoryCord = [[x,y], [x,y], [x,y], [x,y], [x,y], [x,y], [x,y]]
    def territory_claim(gameMap, x, y, oldChar, newChar):
        mapWidth = len(gameMap)
        mapHeight = len(gameMap[0])

        if oldChar == None:
            oldChar = gameMap[x][y]

        if gameMap[x][y] != oldChar:
            return
        gameMap[x][y] = newChar
        if x > 0: # left
            floodFill(gameMap, x-1, y, oldChar, newChar)

        if y > 0: # up
            floodFill(gameMap, x, y-1, oldChar, newChar)

        if x < mapWidth-1: # right
            floodFill(gameMap, x+1, y, oldChar, newChar)

        if y < mapHeight-1: # down
            floodFill(gameMap, x, y+1, oldChar, newChar)
     def is_adjacent(gameMap, xCoor,yCoor):
         for idx in range(-2,3):
             for idx2 in range(-2,3):
                 if gameMap[xCoor+idx][yCoor+idx2] == "-":
                     return True
         return False
     def can_steal_territory(gameMap):
         for x in range(worldWidth):
             for y in range(worldHeight):
                 if gameMap[x][y] = "+":
                     if is_adjacent(gameMap, x, y):
                         return True
         return False
             
     def territory_steal(gameMap, xHave, yHave, xTake, yTake):
         taked = gameMap[xHave, yHave]
         taker = gameMap[xTake, yTake]
         territory_claim(gameMap, xHave, yHave, None, '+')
         territory_claim(gameMap, xTake, yTake, None, '-')
         if can_steal_territory(gameMap):
             territory_claim(gameMap, xTake, yTake, None, taker)
             territory_claim(gameMap, xHave, yHave, None, taker)
         else:
             territory_claim(gameMap, xTake, yTake, None, taked)
             territory_claim(gameMap, xHave, yHave, None, taker)
         

validInputPlayerCount = 0
print("hello")
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
playerAssignments = "ABCD"
for idx in range(playerCount):
    player[idx] = input ("What is the name of player %d?: " % (idx+1))
random.shuffle(player)
print ("The order of play will be:")
for idx in range (playerCount):
    print("player %s: %s"% (playerAssignments[idx], player[order[idx]]))
          
input("click enter to play")
turn = 0
gameComplete = False
while not gameComplete:
    personsTurn = turn%playerCount
    playerInUse = player[personsTurn]
    print(playerInUse)
    turn+=1
    
territory_claim(WorldMap, territoryCord[PICKED][0], territoryCord[PICKED][1], None, playerAssignments[personsTurn])    

