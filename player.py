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
#   2025.06.12- created clear file functions


#NOTE- all instances of playerObj or any variation with that in it is a
#       list of objects with each object being an instance of the player class




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
    
#One
def makingFirstSaveOnOne(numberOfPlayers,namesOfPlayers,moneyOfPlayers,troopsOfPlayers,territoriesOfPlayers):
    try:
        saveOneWrite = open("savedGameOne.txt", "w")
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
        saveOneRead = open("savedGameOne.txt", "r")
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
        saveOneWrite = open("savedGameOne.txt", "w")
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

#Clearing file/reseting save
def clearingFileOne():
    try:
        saveOneWrite = open("savedGameOne.txt", "w")
    except:
        print("File not found.")
    else:
        saveOneWrite.close()




#two
def makingFirstSaveOnTwo(numberOfPlayers,namesOfPlayers,moneyOfPlayers,troopsOfPlayers,territoriesOfPlayers):
    try:
        saveTwoWrite = open("savedGameTwo.txt", "w")
    except:
        print("File not found.")
    else:
        for i in range(numberOfPlayers):        
            saveTwoWrite.write(str(namesOfPlayers[i])+" ")
            saveTwoWrite.write(str(troopsOfPlayers[i].troops)+" ")
            saveTwoWrite.write(str(moneyOfPlayers[i].money)+" ")
            saveTwoWrite.write(str(territoriesOfPlayers[i].territories)+"\n")
            
        
        saveTwoWrite.close()


                    
def saveTwoReadFunct():
    try:
        saveTwoRead = open("savedGameTwo.txt", "r")
    except:
        print("File not found.")
    else:

        #READING FROM FILE/ LOADING SAVE
        lines = saveTwoRead.readlines()
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
            
        saveTwoRead.close()
        
    return (playerObjRead)


#WRITNG TO FILE 
def savingFileTwo(playerObjWrite):
    try:
        saveTwoWrite = open("savedGameTwo.txt", "w")
    except:
        print("File not found.")
    else:
        for i in range(len(playerObj)):        
            saveTwoWrite.write(str(playerObjWrite[i].name)+" ")
            saveTwoWrite.write(str(playerObjWrite[i].troops)+" ")
            saveTwoWrite.write(str(playerObjWrite[i].money)+" ")
            for index in range(len(playerObjWrite[i].territories)):
                saveTwoWrite.write(str(playerObjWrite[i].territories[index])+ " ")
            saveTwoWrite.write("\n")
        
        saveTwoWrite.close()

#Clearing file/reseting save
def clearingFileTwo():
    try:
        saveTwoWrite = open("savedGameTwo.txt", "w")
    except:
        print("File not found.")
    else:
        saveTwoWrite.close()


#three
def makingFirstSaveOnThree(numberOfPlayers,namesOfPlayers,moneyOfPlayers,troopsOfPlayers,territoriesOfPlayers):
    try:
        saveThreeWrite = open("savedGameThree.txt", "w")
    except:
        print("File not found.")
    else:
        for i in range(numberOfPlayers):        
            saveThreeWrite.write(str(namesOfPlayers[i])+" ")
            saveThreeWrite.write(str(troopsOfPlayers[i].troops)+" ")
            saveThreeWrite.write(str(moneyOfPlayers[i].money)+" ")
            saveThreeWrite.write(str(territoriesOfPlayers[i].territories)+"\n")
            
        
        saveThreeWrite.close()


                    
def saveThreeReadFunct():
    try:
        saveThreeRead = open("savedGameThree.txt", "r")
    except:
        print("File not found.")
    else:

        #READING FROM FILE/ LOADING SAVE
        lines = saveThreeRead.readlines()
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
            
        saveThreeRead.close()
        
    return (playerObjRead)


#WRITNG TO FILE
#must put list of each object of player into parameters
def savingFileThree(playerObjWrite):
    try:
        saveThreeWrite = open("savedGameThree.txt", "w")
    except:
        print("File not found.")
    else:
        for i in range(len(playerObj)):        
            saveThreeWrite.write(str(playerObjWrite[i].name)+" ")
            saveThreeWrite.write(str(playerObjWrite[i].troops)+" ")
            saveThreeWrite.write(str(playerObjWrite[i].money)+" ")
            for index in range(len(playerObjWrite[i].territories)):
                saveThreeWrite.write(str(playerObjWrite[i].territories[index])+ " ")
            saveThreeWrite.write("\n")
        
        saveThreeWrite.close()

#Clearing file/reseting save
def clearingFileThree():
    try:
        saveThreeWrite = open("savedGameThree.txt", "w")
    except:
        print("File not found.")
    else:
        saveThreeWrite.close()

#MAIN 
playerObj = saveOneReadFunct()
playerObj[0].invest()
playerObj[0].income()
savingFileOne(playerObj)
