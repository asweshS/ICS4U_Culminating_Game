import random
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
for idx in range(playerCount):
    player[idx] = input ("What is the name of player %d?: " % (idx+1))
random.shuffle(player)
print ("The order of play will be:")
for idx in range (playerCount):
    print(player[order[idx]])
          
input("click enter to play")
turn = 0
gameComplete = False
while not gameComplete:
    playerInUse = player[turn%playerCount]
    print("It is %s's turn" % playerInUse)
    

