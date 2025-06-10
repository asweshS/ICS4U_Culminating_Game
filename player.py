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
    


def saveOneReadFunct(numberOfPlayers):
    try:
        saveOneRead = open("One.txt", "r")
    except:
        print("File not found.")
    else:

        #READING FROM FILE/ LOADING SAVE
        lines = saveOneRead.readlines()
        players =[]
        playerObjRead = []
        
        for line in lines:
            players.append(line)

        if (len(players) == 0 or len(players) == 1):#first save
            for i in range(numberOfPlayers):
                playerName = str(input("WHAT IS YOUR NAME: "))
                playerObjRead.append(Player(playerName))
            
        else:#loading save
            print(len(players))
            for i in range(len(players)):
                players[i] = players[i].split()
                nameForThisPlayer = players[i][0]
                troopsForThisPlayer = players[i][1]
                moneyForThisPlayer = players[i][2]
                             
                playerObjRead.append( Player(nameForThisPlayer,troopsForThisPlayer,\
                                      moneyForThisPlayer))
                
                print(playerObjRead[i])
            
        saveOneRead.close()
    return (playerObjRead)


#WRITNG TO FILE 
def savingFile(playerObjWrite):
    try:
        saveOneWrite = open("One.txt", "w")
    except:
        print("File not found.")
    else:
        for i in range(len(playerObj)):        
            saveOneWrite.write(str(playerObjWrite[i].name)+" ")
            saveOneWrite.write(str(playerObjWrite[i].troops)+" ")
            saveOneWrite.write(str(playerObjWrite[i].money)+" ")
            saveOneWrite.write(str(playerObjWrite[i].territories)+"\n")
            
        
        saveOneWrite.close()

playerObj = saveOneReadFunct(4)
savingFile(playerObj)
