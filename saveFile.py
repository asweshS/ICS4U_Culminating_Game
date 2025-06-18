# Name: Andrew Urquhart, Devan Lucas
# Course: ICS4U
# File: saveFile.py
# Description:
#   This file contains the implementation of a save/load system for a game.
#   It allows players to save their game state to text files and load it back later.
#   The system supports three separate save slots, each with its own read/write/clear set of functions.
#
# INPUTS:
#   - Player data including name, troops, money, territories, strength, and defense 
#   - Save file numbers (1, 2, or 3) to determine which save slot to read/write/clear
#   - Player actions such as buying strength or defense, attacking other players
#
# OUTPUTS:
#   - Game state saved to text files in a structured format
# ALGORITHM:
"""
   CLASS SaveForce
    VARIABLES:
        units
        strength
        defense
        territory
        assignments
        playNum

    METHOD __init__(unit, terr, playerNum, assgnmnts, strength=0, defense=0)
        SET instance variables accordingly

    METHOD Attack(p2, player1_name, player2_name, selfTroops, p2Troops)
        IF self has less than 1 unit
            PRINT "Not enough units to attack"
            RETURN

        ROLL dice1 = random 1–6 * selfTroops
        ROLL dice2 = random 1–6 * p2Troops

        IF attacker dice > defender dice THEN
            CALCULATE troop changes with defense and strength
            UPDATE both players' units
            PRINT result
            RETURN True
        ELSE
            CALCULATE troop changes with defense and strength
            UPDATE both players' units
            PRINT result
            RETURN False
        ENDIF

        IF defender units = 0 THEN
            RETURN True (attacker wins)
        ENDIF

    METHOD buyStrength(player)
        IF player has no money
            PRINT warning
            RETURN

        ASK how many strength levels to buy
        CALCULATE cost
        CONFIRM with user
        IF confirmed AND player has enough money
            ADD to strength
            DEDUCT money
        ELSE
            OFFER to retry
        ENDIF

    METHOD buyDefense(player)
        SAME LOGIC AS buyStrength, but for defense
    
    CLASS Player_Save
    VARIABLES:
        name
        troops
        money
        territories
        investment

    METHOD __init__(name, troops, money, territories)
        SET instance variables

    METHOD income()
        CALCULATE income = 500 + (100 * number of territories)
        ADD income to money

    METHOD invest()
        ADD 1000 to money

    METHOD balance()
        PRINT current money

    METHOD buy_troops(amount)
        CALCULATE cost = amount * 100
        IF player has enough money
            ADD troops
            DEDUCT money
            PRINT success
        ELSE
            PRINT "Not enough money"
        ENDIF

    METHOD __str__()
        RETURN name

    REPEATED FUNCTIONS FOR EACH SAVE FILE:
    FUNCTION saveOneReadFunct()
        TRY to open savedGameOne.txt    
        READ lines into players list
        FOR each line in players
            SPLIT line into attributes
            CREATE SaveForce and Player_Save objects
            APPEND to respective lists
        RETURN forceObjRead, playerObjRead
    FUNCTION savingFileOne(playerObjWrite, forceObj)
        TRY to open savedGameOne.txt for writing
        FOR each player in playerObjWrite
            WRITE attributes to file
        CLOSE file
    FUNCTION clearingFileOne()
        TRY to open savedGameOne.txt for writing (clearing it)
        CLOSE file  
    FUNCTION doesFileOneHaveData()
        TRY to open savedGameOne.txt
        IF file has lines, return True
        ELSE return False   
    FUNCTION loadSave(numberOfFile)
        IF numberOfFile == 1 THEN
            RETURN saveOneReadFunct()
        ELSE IF numberOfFile == 2 THEN
            RETURN saveTwoReadFunct()
        ELSE IF numberOfFile == 3 THEN
            RETURN saveThreeReadFunct()
        ELSE
            PRINT "Invalid file number"
            RETURN None
    FUNCTION savingFile(numberOfFile, playerObjWrite, forceObj)
        IF numberOfFile == 1 THEN
            savingFileOne(playerObjWrite, forceObj)
        ELSE IF numberOfFile == 2 THEN
            savingFileTwo(playerObjWrite, forceObj)
        ELSE IF numberOfFile == 3 THEN
            savingFileThree(playerObjWrite, forceObj)
        ELSE
            PRINT "Invalid file number"
# END ALGORITHM
"""
#
# HISTORY:
#   2025.06.09 - Developed basic save/load system for game data using text files
#   2025.06.10 - continued development of Player class with methods for income, investment, and troop management
#   2025.06.11 - worked on bugs in saving logic and added functionality for multiple save files
#   2025.06.13 - continued to work on bugs in save/load functionality, added methods for reading and writing player data 
#   2025.06.15 - Added methods for buying strength and defense, and managing player income
#   2025.06.16 - Implemented clear save functionality and checks for existing data in save files
#   2025.06.17 - Finalized save/load functionality, added comments and documentation
# Note:
#   - The system supports three separate save slots, each with its own read/write/clear set of functions.
#   - All player management is handled through lists of Player objects passed between functions.import random

import random
class SaveForce:
    troops = 0
    strength = 0
    defense = 0
    territory = []
    assignments = "ABCD"
    
    # which player this class belongs to
    playNum = 0
    def __init__(self, troop, terr, playerNum, assgnmnts, strength = 0, defense = 0):
        self.troops = int(troop)
        self.territory = terr
        self.playNum = playerNum
        self.strength = int(strength)
        self.defense = int(defense)

    # roll dice and see who wins, defense is p2
    def Attack(self, p2, player1, player2, selfTroops, p2Troops):

        # when attacker doesn't have enough units
        if (self.troops <1):
            print("You cannot attack, you dont have enough troops")
            return

        # attacker dice
        dice1 = random.randint(1, 6) * selfTroops
        # defense dice
        dice2 = random.randint(1, 6) * p2Troops

        # attacker dice is higher
        if (dice1 > dice2):
            difference = (random.randint(5,10)*self.defense) -  (random.randint(5,10) * p2.strength)
            difference2 = (random.randint(10,20)*p2.defense) -  (random.randint(10,20) * self.strength)
            if difference >-10:
                difference = -10
            if difference2 > -10:
                difference2 = -10
            # if defender is out of units, then give land to attacker
            self.troops += difference 
            p2.troops += difference2
            if (self.troops < 0):
                self.troops = 0
            if p2.troops < 0:
                p2.troops = 0
            print("%s wins!" % player1)
            print("%s: %s troops left, %s: %s troops left)" % (player1, self.troops, player2, p2.troops))
            return True
        # defender dice is higher or dice are even
        if (dice2 > dice1 or dice1 == dice2):
            difference = (random.randint(10,20)*self.defense) -  (random.randint(10,20) * p2.strength)
            difference2 = (random.randint(5,10)*p2.defense) -  (random.randint(5,10) * self.strength)
            if difference >-10:
                difference = -10
            if difference2 > -10:
                difference2 = -10
            # if defender is out of units, then give land to attacker
            self.troops += difference 
            p2.troops += difference2
            if (self.troops < 0):
                self.troops = 0
            if p2.troops < 0:
                p2.troops = 0
            print("%s wins!" % player2)
            print("%s: %s troops left, %s: %s troops left)" % (player1, self.troops, player2, p2.troops))
            return False            
        # if defender is out of units, then give land to attacker
        if (p2.troops == 0): 
            return True
    def buyStrength(self, playerClass):
        baseCost = 300
        INCREMENT = 300
        print("Strength level: %s" % self.strength)
        if playerClass.money == 0:
            print("You don't have any money!")
            return
        validInput = False
        while not validInput:
            try:
                amt = int(input("How many strength levels would you like to buy?  ($300 each): " ))
            except:
                print("Invalid input, try again")
                return self.buyStrength(playerClass)
            else:
                if amt < 0:
                    print("You cannot buy negative strength levels!")
                    return self.buyStrength(playerClass)
                elif amt == 0:
                    print("Buying no strength levels!")
                    return
                else:
                    validInput = True
        # add increasing 
        totalCost = (baseCost) + (INCREMENT * amt)- INCREMENT
        des = input("Increase strength costs %s, are you sure you want to buy? (y or n): " % totalCost)
        if (des == 'y'):
            # if player doesn't have enough money
            if (playerClass.money - totalCost <= 0):
                print("You don't have enough money!")
                return self.buyStrength(playerClass)
            self.strength += amt
            playerClass.money -= totalCost
        elif (des == 'n'): 
            des1=""
            while (des1 != "y" or des1 != 'n'):
                des1 = input("Cancelled, do you want to buy troops still? (y or n): ")
                if (des1 == 'y'):
                    return self.buyStrength(playerClass)
                if (des1 == 'n'):
                    return 
                
        else: 
            print("Invalid input, try again")
            return self.buyStrength(playerClass)
            
    def buyDefense(self, playerClass):
        baseCost = 300
        INCREMENT = 300
        print("Defense level: %s" % self.defense)
        if playerClass.money == 0:
            print("You don't have any money!")
            return
        validInput = False
        while not validInput:
            try:
                amt = int(input("How many defense levels would you like to buy? ($300 each): " ))
            except:
                print("Invalid input, try again")
                return self.buyDefense(playerClass)
            else:
                if amt < 0:
                    print("You cannot buy negative defense levels!")
                    return self.buyDefense(playerClass)
                elif amt == 0:
                    print("Buying no defense levels!")
                    return
                else:
                    validInput = True
        
        # add increasing 
        totalCost = (baseCost) + (INCREMENT * amt)- INCREMENT
        des = input("Increase defenese costs %s, are you sure you want to buy? (y or n): " % totalCost)
        if (des == 'y'):
            # if player doesn't have enough money
            if (playerClass.money - totalCost <= 0):
                print("You don't have enough money!")
                return self.buyDefense(playerClass)
            else:
                self.defense += amt
                playerClass.money -= totalCost
                return
        elif (des == 'n'): 
            des1=""
            while (des1 != "y" or des1 != 'n'):
                des1 = input("Cancelled, do you want to buy troops still? (y or n): ")
                if (des1 == 'y'):
                    return self.buyDefense(playerClass)
                if (des1 == 'n'):
                    return
            
        else: 
            print("Invalid input, try again")
            return self.buyDefense(playerClass)
class Player_Save:
    investment = 0

    def __init__(self, name,troops = 100, money =0,territories=[]):

        self.name = name
        self.troops = int(troops)
        self.money = int(money)
        self.territories = []
        for i in range(len(territories)):
            self.territories.append(territories[i])

    def invest(self):
        investment = 0
        moneyDupe = self.money
        while True:
            if moneyDupe>= 10000:
                moneyToAdd = random.randint((investment+100), (investment+400))
                if moneyToAdd<=200:
                    moneyToAdd = 200
                self.money += moneyToAdd
                return moneyToAdd
            else:
                moneyDupe +=20
                investment += 1

        print(f"New balance ${self.money}")
    def buy_troops(self, amountOfTroops, forcePlay):
        self.troops += amountOfTroops
        self.money -= 10 * amountOfTroops
        print(f"{self.name} has bought {amountOfTroops} troops!")

    def income(self):
        self.daily_income = 500 + (len(self.territories) * 100)
        self.money += self.daily_income
        print(f"{self.name} has earned ${self.daily_income} from their territories.")

    def __str__(self):
        return self.name


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
        forceObjRead = []

        for line in lines:
            players.append(line)

        print("there are " +str(len(players)) + " players")#number of players

        for i in range(len(players)):
            players[i] = players[i].split()

            strenthForThisPlayer = players[i][0]
            defenseForThisPlayer = players[i][1]
            nameForThisPlayer = players[i][2]

            troopsForThisPlayer = players[i][3]

            moneyForThisPlayer = players[i][4]

            teritoriesForThisPlayer = []

            for index in range(len(players[i])-5):
                teritoriesForThisPlayer.append(players[i][index+5])


            forceObjRead.append(SaveForce(troopsForThisPlayer, teritoriesForThisPlayer, i, players[i][2], strenthForThisPlayer, defenseForThisPlayer))                 
            playerObjRead.append( Player_Save(nameForThisPlayer,troopsForThisPlayer,\
                                moneyForThisPlayer,teritoriesForThisPlayer))



        saveOneRead.close()

    return forceObjRead, playerObjRead


#WRITNG TO FILE 
def savingFileOne(playerObjWrite, forceObj):
    try:
        saveOneWrite = open("savedGameOne.txt", "w")
    except:
        print("File not found.")
    else:
        for i in range(len(playerObjWrite)):     
            saveOneWrite.write(str(forceObj[i].strength)+" ")
            saveOneWrite.write(str(forceObj[i].defense)+" ")   
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
        forceObjRead = []

        for line in lines:
            players.append(line)

        print("there are " +str(len(players)) + " players")#number of players

        for i in range(len(players)):
            players[i] = players[i].split()

            strenthForThisPlayer = players[i][0]
            defenseForThisPlayer = players[i][1]
            nameForThisPlayer = players[i][2]

            troopsForThisPlayer = players[i][3]

            moneyForThisPlayer = players[i][4]

            teritoriesForThisPlayer = []

            for index in range(len(players[i])-5):
                teritoriesForThisPlayer.append(players[i][index+5])


            forceObjRead.append(SaveForce(troopsForThisPlayer, teritoriesForThisPlayer, i, players[i][2], strenthForThisPlayer, defenseForThisPlayer))                 
            playerObjRead.append( Player_Save(nameForThisPlayer,troopsForThisPlayer,\
                                moneyForThisPlayer,teritoriesForThisPlayer))

        saveTwoRead.close()

    return forceObjRead, playerObjRead


#WRITNG TO FILE 
def savingFileTwo(playerObjWrite, forceObj):
    try:
        saveTwoWrite = open("savedGameTwo.txt", "w")
    except:
        print("File not found.")
    else:
        for i in range(len(playerObjWrite)):   
            saveTwoWrite.write(str(forceObj[i].strength)+" ")
            saveTwoWrite.write(str(forceObj[i].defense)+" ")       
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
        forceObjRead = []

        for line in lines:
            players.append(line)

        print("there are " +str(len(players)) + " players")#number of players

        for i in range(len(players)):
            players[i] = players[i].split()

            strenthForThisPlayer = players[i][0]
            defenseForThisPlayer = players[i][1]
            nameForThisPlayer = players[i][2]

            troopsForThisPlayer = players[i][3]

            moneyForThisPlayer = players[i][4]

            teritoriesForThisPlayer = []

            for index in range(len(players[i])-5):
                teritoriesForThisPlayer.append(players[i][index+5])


            forceObjRead.append(SaveForce(troopsForThisPlayer, teritoriesForThisPlayer, i, players[i][2], strenthForThisPlayer, defenseForThisPlayer))                 
            playerObjRead.append( Player_Save(nameForThisPlayer,troopsForThisPlayer,\
                                moneyForThisPlayer,teritoriesForThisPlayer))

        saveThreeRead.close()

    return forceObjRead, playerObjRead


#WRITNG TO FILE
#must put list of each object of player into parameters
def savingFileThree(playerObjWrite, forceObj):
    try:
        saveThreeWrite = open("savedGameThree.txt", "w")
    except:
        print("File not found.")
    else:
        for i in range(len(playerObjWrite)):
            saveThreeWrite.write(str(forceObj[i].strength)+" ")
            saveThreeWrite.write(str(forceObj[i].defense)+" ")  
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
    try:
        # Attempt to open the file to check if it exists
        fileOne = open("savedGameOne.txt", "r")
    except: return False  # If the file does not exist, return False
    else:
        fileOneLines = fileOne.readlines()
        if len(fileOneLines) > 0:
            fileOne.close()
            return True
        else:   
            fileOne.close()
            return False

def doesFileTwoHaveData():
    try:
        # Attempt to open the file to check if it exists
        fileTwo = open("savedGameTwo.txt", "r")
    except: return False  # If the file does not exist, return False
    else:
        fileTwoLines = fileTwo.readlines()
        if len(fileTwoLines) > 0:
            fileTwo.close()
            return True
        else:   
            fileTwo.close()
            return False

def doesFileThreeHaveData():
    try:
        fileThree = open("savedGameThree.txt", "r")
    except: return False  # If the file does not exist, return False
    else:
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


def savingFile(numberOfFile, playerObjWrite, forceObj):
    if numberOfFile == 1:
        savingFileOne(playerObjWrite, forceObj)
    elif numberOfFile == 2:
        savingFileTwo(playerObjWrite, forceObj)
    elif numberOfFile == 3:
        savingFileThree(playerObjWrite, forceObj)
    else:
        print("Invalid file number.")
