# Name: Andrew Urquhart
# Course: ICS4U
# File: urquhart_andrew_player.py
# Description:
#   This file implements the Player class and all related file operations for a text-based
#   territory strategy game. It includes methods for managing income, troops, and investments,
#   as well as saving and loading player data across three separate save files.
#
# INPUTS:
#   - Player data: name (string), money (int), troops (int), and territories (list of strings)
#   - Number of players (int)
#   - In-game actions: investment and troop purchases (integers as function arguments)
#   - Save/load operations triggered by function calls
#
# OUTPUTS:
#   - Console messages showing current player status
#   - Three text save files containing player data: savedGameOne.txt, savedGameTwo.txt, savedGameThree.txt
#   - Updated player objects returned from save functions
#
# ALGORITHM:
#   1. Define the Player class with the following:
#       - Attributes: name, troops, money, list of territories, daily income (calculated), and investment.
#       - __init__ method initializes a player's stats and calculates base income from territory count.
#       - income() method adds daily income to money, factoring in investments and territory count.
#       - invest() method increases the player's future income by increasing the investment bonus.
#       - buy_troops(amount) method deducts money and increases troop count based on the amount.
#       - __str__ method returns a formatted string showing the player's current status.
#
#   2. Implement three sets of save functionality (One, Two, Three):
#       - makingFirstSaveOnX() functions create new save files from inputted lists of player data.
#           • Each player's attributes are written to the save file as a space-separated line.
#           • These functions return a list of Player objects created from the inputs.
#       - saveXReadFunct() functions read from the corresponding save file, reconstructing Player objects.
#           • Each line is split into name, troops, money, and territories.
#           • A new Player is created from the parsed data and added to a return list.
#       - savingFileX() functions write current player data to the save file.
#           • Data is written in the same format as in the initial save function.
#       - clearingFileX() functions open and immediately close the save file to clear it.
#
#   3. To save or load the game, the appropriate saveXReadFunct() and savingFileX() should be used
#      with a list of Player objects passed in as an argument.
#
# HISTORY:
#   2025.06.02 - Created Player class with base attributes and methods for money and territory logic
#   2025.06.09 - Developed save/load system for game data using text files
#   2025.06.12 - Added investment system, detailed income logic, and separate file clearing functions
#
# NOTE:
#   - The system supports three separate save slots, each with its own read/write/clear set of functions.
#   - All player management is handled through lists of Player objects passed between functions.




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
        playerObjFirstSaveOnOne = []
        for i in range(numberOfPlayers):
            playerObjFirstSaveOnOne.append(Player(namesOfPlayers[i],troopsOfPlayers[i]\
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
        playerObjFirstSaveOnTwo = []
        for i in range(numberOfPlayers):
            playerObjFirstSaveOnTwo.append(Player(namesOfPlayers[i],troopsOfPlayers[i]\
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
        playerObjFirstSaveOnThree = []
        for i in range(numberOfPlayers):
            playerObjFirstSaveOnThree.append(Player(namesOfPlayers[i],troopsOfPlayers[i]\
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


def whichFilesHaveData():
    whichOneList = []
    fileOne = open("savedGameOne.txt", "r")
    fileOneLines = fileOne.readlines()
    countFileOne = 0
    for line in fileOneLines:
        countFileOne+=1
    if countFileOne>1:
        whichOneList.append(True)
    else:
        whichOneList.append(False)
        
    fileTwo = open("savedGameTwo.txt", "r")
    fileTwoLines = fileTwo.readlines()
    countFileTwo = 0
    for line in fileTwoLines:
        countFileTwo+=1
    if countFileTwo>1:
        whichOneList.append(True)
    else:
        whichOneList.append(False)
    
    fileThree = open("savedGameThree.txt", "r")
    fileThreeLines = fileThree.readlines()
    countFileThree = 0
    for line in fileThreeLines:
        countFileThree+=1
        
    if countFileThree>1:
        whichOneList.append(True)
    else:
        whichOneList.append(False)
    return whichOneList

#MAIN
