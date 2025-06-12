# Player class and save/load system for a territory strategy game
# All file operations support three separate save slots

class Player:
    # Class variable shared across all instances for tracking investments
    investment = 0

    def __init__(self, name, troops=100, money=0, territories=[]):
        # Initialize player attributes
        self.name = name
        self.troops = int(troops)
        self.money = int(money)

        # Create a fresh list of territories to avoid mutable default argument issues
        self.territories = []
        for i in range(len(territories)):
            self.territories.append(territories[i])

        # Base daily income = 1000 + 100 per territory
        self.daily_income = 1000 + (len(self.territories) * 100)

    def income(self):
        # Add daily income to player's money, including any investment bonus
        self.daily_income = 1000 + (len(self.territories) * 100) + self.investment
        self.money += self.daily_income

    def invest(self):
        # Increase future daily income through investments
        self.investment += 500

    def buy_troops(self, amountOfTroops):
        # Spend money to buy troops (100 money per troop)
        self.troops += amountOfTroops
        self.money -= 100 * amountOfTroops

    def __str__(self):
        # Return a nicely formatted summary of player status
        printOutStatement = []
        printOutStatement.append(f"Player {self.name} has {self.money} money, {self.troops} soldiers and controls territories:")
        for i in range(len(self.territories)):
            printOutStatement.append(str(self.territories[i]) + " ")
        return "".join(printOutStatement)

#--------------------------SAVE SLOT ONE FUNCTIONS--------------------------

def makingFirstSaveOnOne(numberOfPlayers, namesOfPlayers, moneyOfPlayers, troopsOfPlayers, territoriesOfPlayers):
    # Create Player objects and write them to save file 1
    try:
        saveOneWrite = open("savedGameOne.txt", "w")
    except:
        print("File not found.")
    else:
        playerObjFirstSaveOnOne = []
        for i in range(numberOfPlayers):
            playerObjFirstSaveOnOne.append(Player(namesOfPlayers[i], troopsOfPlayers[i], moneyOfPlayers[i], territoriesOfPlayers[i]))
            saveOneWrite.write(f"{namesOfPlayers[i]} {troopsOfPlayers[i]} {moneyOfPlayers[i]} {territoriesOfPlayers[i]}\n")
        saveOneWrite.close()
        return playerObjFirstSaveOnOne

def saveOneReadFunct():
    # Read player data from save file 1 and recreate Player objects
    try:
        saveOneRead = open("savedGameOne.txt", "r")
    except:
        print("File not found.")
    else:
        lines = saveOneRead.readlines()
        players = []
        playerObjRead = []

        for line in lines:
            players.append(line.strip())

        print("there are " + str(len(players)) + " players")

        for i in range(len(players)):
            players[i] = players[i].split()
            name = players[i][0]
            troops = players[i][1]
            money = players[i][2]
            territories = players[i][3:]  # Remaining elements are territories
            playerObjRead.append(Player(name, troops, money, territories))
            print(playerObjRead[i])
        saveOneRead.close()
        return playerObjRead

def savingFileOne(playerObjWrite):
    # Save current Player object data to save file 1
    try:
        saveOneWrite = open("savedGameOne.txt", "w")
    except:
        print("File not found.")
    else:
        for i in range(len(playerObjWrite)):
            saveOneWrite.write(f"{playerObjWrite[i].name} {playerObjWrite[i].troops} {playerObjWrite[i].money} ")
            for territory in playerObjWrite[i].territories:
                saveOneWrite.write(f"{territory} ")
            saveOneWrite.write("\n")
        saveOneWrite.close()

def clearingFileOne():
    # Clears save file 1 by opening and closing it in write mode
    try:
        saveOneWrite = open("savedGameOne.txt", "w")
    except:
        print("File not found.")
    else:
        saveOneWrite.close()

#--------------------------SAVE SLOT TWO FUNCTIONS--------------------------
# (Same structure as save slot one)

def makingFirstSaveOnTwo(numberOfPlayers, namesOfPlayers, moneyOfPlayers, troopsOfPlayers, territoriesOfPlayers):
    try:
        saveTwoWrite = open("savedGameTwo.txt", "w")
    except:
        print("File not found.")
    else:
        playerObjFirstSaveOnTwo = []
        for i in range(numberOfPlayers):
            playerObjFirstSaveOnTwo.append(Player(namesOfPlayers[i], troopsOfPlayers[i], moneyOfPlayers[i], territoriesOfPlayers[i]))
            saveTwoWrite.write(f"{namesOfPlayers[i]} {troopsOfPlayers[i]} {moneyOfPlayers[i]} {territoriesOfPlayers[i]}\n")
        saveTwoWrite.close()
        return playerObjFirstSaveOnTwo

def saveTwoReadFunct():
    try:
        saveTwoRead = open("savedGameTwo.txt", "r")
    except:
        print("File not found.")
    else:
        lines = saveTwoRead.readlines()
        players = []
        playerObjRead = []

        for line in lines:
            players.append(line.strip().split())

        print("there are " + str(len(players)) + " players")

        for i in range(len(players)):
            name = players[i][0]
            troops = players[i][1]
            money = players[i][2]
            territories = players[i][3:]
            playerObjRead.append(Player(name, troops, money, territories))
            print(playerObjRead[i])
        saveTwoRead.close()
        return playerObjRead

def savingFileTwo(playerObjWrite):
    try:
        saveTwoWrite = open("savedGameTwo.txt", "w")
    except:
        print("File not found.")
    else:
        for player in playerObjWrite:
            saveTwoWrite.write(f"{player.name} {player.troops} {player.money} ")
            for territory in player.territories:
                saveTwoWrite.write(f"{territory} ")
            saveTwoWrite.write("\n")
        saveTwoWrite.close()

def clearingFileTwo():
    try:
        saveTwoWrite = open("savedGameTwo.txt", "w")
    except:
        print("File not found.")
    else:
        saveTwoWrite.close()

#--------------------------SAVE SLOT THREE FUNCTIONS--------------------------
# (Same structure as the above two)

def makingFirstSaveOnThree(numberOfPlayers, namesOfPlayers, moneyOfPlayers, troopsOfPlayers, territoriesOfPlayers):
    try:
        saveThreeWrite = open("savedGameThree.txt", "w")
    except:
        print("File not found.")
    else:
        playerObjFirstSaveOnThree = []
        for i in range(numberOfPlayers):
            playerObjFirstSaveOnThree.append(Player(namesOfPlayers[i], troopsOfPlayers[i], moneyOfPlayers[i], territoriesOfPlayers[i]))
            saveThreeWrite.write(f"{namesOfPlayers[i]} {troopsOfPlayers[i]} {moneyOfPlayers[i]} {territoriesOfPlayers[i]}\n")
        saveThreeWrite.close()
        return playerObjFirstSaveOnThree

def saveThreeReadFunct():
    try:
        saveThreeRead = open("savedGameThree.txt", "r")
    except:
        print("File not found.")
    else:
        lines = saveThreeRead.readlines()
        players = []
        playerObjRead = []

        for line in lines:
            players.append(line.strip().split())

        print("there are " + str(len(players)) + " players")

        for i in range(len(players)):
            name = players[i][0]
            troops = players[i][1]
            money = players[i][2]
            territories = players[i][3:]
            playerObjRead.append(Player(name, troops, money, territories))
            print(playerObjRead[i])
        saveThreeRead.close()
        return playerObjRead

def savingFileThree(playerObjWrite):
    try:
        saveThreeWrite = open("savedGameThree.txt", "w")
    except:
        print("File not found.")
    else:
        for player in playerObjWrite:
            saveThreeWrite.write(f"{player.name} {player.troops} {player.money} ")
            for territory in player.territories:
                saveThreeWrite.write(f"{territory} ")
            saveThreeWrite.write("\n")
        saveThreeWrite.close()

def clearingFileThree():
    try:
        saveThreeWrite = open("savedGameThree.txt", "w")
    except:
        print("File not found.")
    else:
        saveThreeWrite.close()

#--------------------------CHECK WHICH FILES HAVE SAVES--------------------------

def whichFilesHaveData():
    # Checks which of the three save files contain more than one line (i.e., actual player data)
    whichOneList = []

    # Check file one
    with open("savedGameOne.txt", "r") as fileOne:
        lines = fileOne.readlines()
        whichOneList.append(len(lines) > 1)

    # Check file two
    with open("savedGameTwo.txt", "r") as fileTwo:
        lines = fileTwo.readlines()
        whichOneList.append(len(lines) > 1)

    # Check file three
    with open("savedGameThree.txt", "r") as fileThree:
        lines = fileThree.readlines()
        whichOneList.append(len(lines) > 1)

    return whichOneList
