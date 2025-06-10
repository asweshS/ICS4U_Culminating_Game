# Name:Andrew Urquhart
# course: ICS4U
# file urquhart_andrew_Culmanating.py
# description:
#   
# INPUTS:

# OUTPUTS:

# ALGORITHM
#   1. Create a Player class with attributes for name, money, resources, territories, forces, and factory count.
#   2. Implement a method to assign daily income.
# HISTORY
#   2025.06.02- created player class with attributes and methods for a basic resources game
#   2025.06.09- created basic save mechanics


class Player:
    daysGoneBy = 0

    def __init__(self, name,troops = 100, money =0,territories = 5):
        self.name = name
        self.troops = troops
        self.territories = 5
        self.money = money


    def income(self,invest):
        self.daily_income = 1000 + (self.territories * 100)
        if invest == 1:
            self.daily_income += 500
        elif invest == 2:
            self.daily_income += 1000
        self.money += self.daily_income

    def buy_troops(self, amountOfTroops):
        self.troops += amountOfTroops
        self.money -= 10 * amountOfTroops



    def __str__(self):  
        return f"Player {self.name} has {self.money} money, {self.troops} soldiers, and controls {self.territories} territories"
    



try:
    saveOneRead = open("One.txt", "r")
except:
    print("File not found.")
else:

    #READING FROM FILE/ LOADING SAVE
    lines = saveOneRead.readlines()
    players =[]
    playerObj = []
    
    for line in lines:
        players.append(line)

    if (len(players) == 0):
        firstSave = True
    else:
        firstSave = False
        for i in range(len(players)):
            players[i] = players[i].split()
    #       for index in range(len(players[i])):
            nameForThisPlayer = players[i][0]
            troopsForThisPlayer = players[i][1]
            moneyForThisPlayer = players[i][2]
                         
            playerObj.append( Player(nameForThisPlayer,troopsForThisPlayer,\
                                  moneyForThisPlayer))
            
            print(playerObj[i])
        
    saveOneRead.close()


#WRITNG TO FILE/ NEW SAVE
try:
    saveOneWrite = open("One.txt", "w")
except:
    print("File not found.")
else:
    numberOfPlayers = 4
    if firstSave == True:
        for i in range(numberOfPlayers):
            playerName = str(input("WHAT IS YOUR BOMBOCLAT NAME: "))
            saveOneWrite.write(playerName+" ")
            saveOneWrite.write("100 ")
            saveOneWrite.write("0 ")
            saveOneWrite.write("5\n")

    else:
        for i in range(len(playerObj)):        
            saveOneWrite.write(str(playerObj[i].name)+" ")
            saveOneWrite.write(str(playerObj[i].troops)+" ")
            saveOneWrite.write(str(playerObj[i].money)+" ")
            saveOneWrite.write(str(playerObj[i].territories)+"\n")
        
    
    saveOneWrite.close()
