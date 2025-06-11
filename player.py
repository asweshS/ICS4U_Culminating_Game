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
    investment = 0

    def __init__(self, name,troops = 100, money =0,territories=[]):
        
        self.name = name
        self.troops = int(troops)
        self.money = int(money)
        self.territories = []
        for i in range(len(territories)):
            self.territories.append(territories[i])
            
        self.daily_income = 1000 + (len(self.territories) * 100)

    def income(self):
        self.daily_income = 1000 + (len(self.territories) * 100)+self.investment
        self.money += self.daily_income

    def invest(self):
        self.investment += 500

    def buy_troops(self, amountOfTroops):
        self.troops += amountOfTroops
        self.money -= 100 * amountOfTroops



    def __str__(self):
        printOutStatement = []
        printOutStatement.append(f"Player {self.name} has {self.money} money, {self.troops} \
soldiers and controls territories:")
        
        for i in range(len(self.territories)):
            printOutStatement.append(str(self.territories[i])+ " ")
        printOutStatement = "".join(printOutStatement)
            
        return printOutStatement
    

def makingFirstSaveOnOne(numberOfPlayers,namesOfPlayers,moneyOfPlayers,troopsOfPlayers,territoriesOfPlayers):
    try:
        saveOneWrite = open("One.txt", "w")
    except:
        print("File not found.")
    else:
        for i in range(numberOfPlayers):        
            saveOneWrite.write(str(namesOfPlayers[i])+" ")
            saveOneWrite.write(str(troopsOfPlayers[i].troops)+" ")
            saveOneWrite.write(str(moneyOfPlayers[i].money)+" ")
            saveOneWrite.write(str(territoriesOfPlayers[i].territories)+"\n")
            
        
        saveOneWrite.close()


                    
def saveOneReadFunct():
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
            
        print("there are " +str(len(players)) + " players")#number of players
        
        for i in range(len(players)):
            players[i] = players[i].split()
            nameForThisPlayer = players[i][0]
            
            troopsForThisPlayer = players[i][1]
            
            moneyForThisPlayer = players[i][2]
            
            teritoriesForThisPlayer = []
            
            for index in range(len(players[i])-3):
                teritoriesForThisPlayer.append(players[i][index+3])
                                    

                             
            playerObjRead.append( Player(nameForThisPlayer,troopsForThisPlayer,\
                                moneyForThisPlayer,teritoriesForThisPlayer))
                
            print(playerObjRead[i])
            
        saveOneRead.close()
        
    return (playerObjRead)


#WRITNG TO FILE 
def savingFileOne(playerObjWrite):
    try:
        saveOneWrite = open("One.txt", "w")
    except:
        print("File not found.")
    else:
        for i in range(len(playerObj)):        
            saveOneWrite.write(str(playerObjWrite[i].name)+" ")
            saveOneWrite.write(str(playerObjWrite[i].troops)+" ")
            saveOneWrite.write(str(playerObjWrite[i].money)+" ")
            for index in range(len(playerObjWrite[i].territories)):
                saveOneWrite.write(str(playerObjWrite[i].territories[index])+ " ")
            saveOneWrite.write("\n")
        
        saveOneWrite.close()

playerObj = saveOneReadFunct()
playerObj[0].invest()
playerObj[0].income()
savingFileOne(playerObj)
