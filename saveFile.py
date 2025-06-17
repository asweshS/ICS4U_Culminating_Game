import random

class SaveForce:
    units = 0
    strength = 0
    defense = 0
    territory = []
    assignments = "ABCD"
    
    # which player this class belongs to
    playNum = 0
    def __init__(self, unit, terr, playerNum, assgnmnts, strength=0, defense=0):
        self.units = int(unit)
        self.territory = terr
        self.playNum = playerNum
        self.strength = 0
        self.defense = 0
        print("%s's units: %s" %(assgnmnts[playerNum], self.units))

    # roll dice and see who wins, defense is p2
    def Attack(self, p2, player1, player2, selfTroops, p2Troops):

        # when attacker doesn't have enough units
        if (self.units <1):
            print("You cannot attack, you dont have enough units")
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
            self.units += difference 
            p2.units += difference2
            if (self.units < 0):
                self.units = 0
            if p2.units < 0:
                p2.units = 0
            print("%s wins!" % player1)
            print("%s: %s troops left, %s: %s troops left)" % (player1, self.units, player2, p2.units))
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
            self.units += difference 
            p2.units += difference2
            if (self.units < 0):
                self.units = 0
            if p2.units < 0:
                p2.units = 0
            print("%s wins!" % player2)
            print("%s: %s units left, %s: %s units left)" % (player1, self.units, player2, p2.units))
            return False            
        # if defender is out of units, then give land to attacker
        if (p2.units == 0): 
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
                amt = int(input("How many strength levels would you like to buy? (First costs $50 and more are additional $10): " ))
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
                des1 = input("Cancelled, do you want to buy units still? (y or n): ")
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
                amt = int(input("How many defense levels would you like to buy? ($300 each)" ))
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
                des1 = input("Cancelled, do you want to buy units still? (y or n): ")
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
                                    

            forceObjRead.append(SaveForce(strenthForThisPlayer, teritoriesForThisPlayer, i, players[i][2], strenthForThisPlayer, defenseForThisPlayer))                 
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
                                    

            forceObjRead.append(SaveForce(strenthForThisPlayer, teritoriesForThisPlayer, i, players[i][2], strenthForThisPlayer, defenseForThisPlayer))                 
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
