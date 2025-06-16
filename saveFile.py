class Player_Save:
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
        print(f"New balance ${self.money}")
    def buy_troops(self, amountOfTroops):
        self.troops += amountOfTroops
        self.money -= 100 * amountOfTroops
        print(f"{self.name} has bought {amountOfTroops} troops.")
        self.balance()


    def __str__(self):
        #printOutStatement = []
        #printOutStatement.append(f"Player {self.name} has {self.money} money, {self.troops} \
#soldiers and controls territories: ")
        
     #   for i in range(len(self.territories)):
       #     printOutStatement.append(str(self.territories[i])+ " ")
       # printOutStatement = "".join(printOutStatement)
            
        return self.name





def makingFirstSaveOnOne(numberOfPlayers,namesOfPlayers,moneyOfPlayers,troopsOfPlayers,territoriesOfPlayers):
    try:
        saveOneWrite = open("savedGameOne.txt", "w")
    except:
        print("File not found.")
    else:
        playerObjFirstSaveOnOne = []
        for i in range(numberOfPlayers):
            playerObjFirstSaveOnOne.append(Player_Save(namesOfPlayers[i],troopsOfPlayers[i]\
                             ,moneyOfPlayers[i],territoriesOfPlayers[i]))
            saveOneWrite.write(str(namesOfPlayers[i])+" ")
            saveOneWrite.write(str(troopsOfPlayers[i])+" ")
            saveOneWrite.write(str(moneyOfPlayers[i])+" ")
            saveOneWrite.write(str(territoriesOfPlayers[i])+"\n")
            
        
        saveOneWrite.close()
        return playerObjFirstSaveOnOne

                    
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
                                    

                             
            playerObjRead.append( Player_Save(nameForThisPlayer,troopsForThisPlayer,\
                                moneyForThisPlayer,teritoriesForThisPlayer))
                
           # print(playerObjRead[i])
            
        saveOneRead.close()
        
    return (playerObjRead)


#WRITNG TO FILE 
def savingFileOne(playerObjWrite):
    try:
        saveOneWrite = open("savedGameOne.txt", "w")
    except:
        print("File not found.")
    else:
        for i in range(len(playerObjWrite)):        
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
        playerObjFirstSaveOnTwo = []
        for i in range(numberOfPlayers):
            playerObjFirstSaveOnTwo.append(Player_Save(namesOfPlayers[i],troopsOfPlayers[i]\
                             ,moneyOfPlayers[i],territoriesOfPlayers[i]))
            saveTwoWrite.write(str(namesOfPlayers[i])+" ")
            saveTwoWrite.write(str(troopsOfPlayers[i])+" ")
            saveTwoWrite.write(str(moneyOfPlayers[i])+" ")
            saveTwoWrite.write(str(territoriesOfPlayers[i])+"\n")
            
        
        saveTwoWrite.close()
        return playerObjFirstSaveOnTwo

                    
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
                                    

                             
            playerObjRead.append( Player_Save(nameForThisPlayer,troopsForThisPlayer,\
                                moneyForThisPlayer,teritoriesForThisPlayer))
                
 #           print(playerObjRead[i])
            
        saveTwoRead.close()
        
    return (playerObjRead)


#WRITNG TO FILE 
def savingFileTwo(playerObjWrite):
    try:
        saveTwoWrite = open("savedGameTwo.txt", "w")
    except:
        print("File not found.")
    else:
        for i in range(len(playerObjWrite)):        
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
        playerObjFirstSaveOnThree = []
        for i in range(numberOfPlayers):
            playerObjFirstSaveOnThree.append(Player_Save(namesOfPlayers[i],troopsOfPlayers[i]\
                                    ,moneyOfPlayers[i],territoriesOfPlayers[i]))
            saveThreeWrite.write(str(namesOfPlayers[i])+" ")
            saveThreeWrite.write(str(troopsOfPlayers[i])+" ")
            saveThreeWrite.write(str(moneyOfPlayers[i])+" ")
            saveThreeWrite.write(str(territoriesOfPlayers[i])+"\n")
            
        
        saveThreeWrite.close()
        return playerObjFirstSaveOnThree

                    
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
                                    

                             
            playerObjRead.append(Player_Save(nameForThisPlayer,troopsForThisPlayer,\
                                moneyForThisPlayer,teritoriesForThisPlayer))
                
           # print(playerObjRead[i])
            
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
        for i in range(len(playerObjWrite)):        
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




def doesFileOneHaveData():
    fileOne = open("savedGameOne.txt", "r")
    fileOneLines = fileOne.readlines()
    if len(fileOneLines) > 0:
        fileOne.close()
        return True
    else:   
        fileOne.close()
        return False
    
def doesFileTwoHaveData():
    fileTwo = open("savedGameTwo.txt", "r")
    fileTwoLines = fileTwo.readlines()
    if len(fileTwoLines) > 0:
        fileTwo.close()
        return True
    else:   
        fileTwo.close()
        return False

def doesFileThreeHaveData():
    fileThree = open("savedGameThree.txt", "r")
    fileThreeLines = fileThree.readlines()
    if len(fileThreeLines) > 0:
        fileThree.close()
        return True
    else:   
        fileThree.close()
        return False

def doesFileHaveData(numberOfFile):
    if numberOfFile == 1:
        return doesFileOneHaveData()
    elif numberOfFile == 2:
        return doesFileTwoHaveData()
    elif numberOfFile == 3:
        return doesFileThreeHaveData()
    else:
        print("Invalid file number.")
        return False

def loadSave(numberOfFile):
    if numberOfFile == 1:
        return saveOneReadFunct()
    elif numberOfFile == 2:
        return saveTwoReadFunct()
    elif numberOfFile == 3:
        return saveThreeReadFunct()
    else:
        print("Invalid file number.")
        return None

def makingFirstSave(numberOfFile, numberOfPlayers, namesOfPlayers, moneyOfPlayers, troopsOfPlayers, territoriesOfPlayers):
    if numberOfFile == 1:
        return makingFirstSaveOnOne(numberOfPlayers, namesOfPlayers, moneyOfPlayers, troopsOfPlayers, territoriesOfPlayers)
    elif numberOfFile == 2:
        return makingFirstSaveOnTwo(numberOfPlayers, namesOfPlayers, moneyOfPlayers, troopsOfPlayers, territoriesOfPlayers)
    elif numberOfFile == 3:
        return makingFirstSaveOnThree(numberOfPlayers, namesOfPlayers, moneyOfPlayers, troopsOfPlayers, territoriesOfPlayers)
    else:
        print("Invalid file number.")
        return None
