# --- PLAYER CLASS DEFINITION ---
class Player:
    # Class-level variable shared by all Player instances
    investment = 0

    # Constructor: initializes player attributes
    def __init__(self, name, troops=100, money=0, territories=[]):
        self.name = name
        self.troops = int(troops)
        self.money = int(money)
        self.territories = [t for t in territories]  # Copy list to avoid shared reference
        self.daily_income = 1000 + (len(self.territories) * 100)

    # Updates the player's money by adding daily income
    def income(self):
        self.daily_income = 1000 + (len(self.territories) * 100) + self.investment
        self.money += self.daily_income

    # Increases player's investment which boosts future income
    def invest(self):
        self.investment += 500

    # Buys troops by spending money (100 per troop)
    def buy_troops(self, amountOfTroops):
        self.troops += amountOfTroops
        self.money -= 100 * amountOfTroops

    # String representation for printing player info
    def __str__(self):
        printOutStatement = []
        printOutStatement.append(f"Player {self.name} has {self.money} money, {self.troops} soldiers and controls territories:")
        for territory in self.territories:
            printOutStatement.append(str(territory) + " ")
        return "".join(printOutStatement)

# -------------------------------
# -------- SAVE SLOT ONE --------
# -------------------------------

# Create first save for slot one using individual lists
def makingFirstSaveOnOne(numberOfPlayers, namesOfPlayers, moneyOfPlayers, troopsOfPlayers, territoriesOfPlayers):
    try:
        saveOneWrite = open("savedGameOne.txt", "w")
    except:
        print("File not found.")
    else:
        for i in range(numberOfPlayers):
            saveOneWrite.write(f"{namesOfPlayers[i]} {troopsOfPlayers[i].troops} {moneyOfPlayers[i].money} {territoriesOfPlayers[i].territories}\n")
        saveOneWrite.close()

# Load save slot one and reconstruct Player objects
def saveOneReadFunct():
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
            nameForThisPlayer = players[i][0]
            troopsForThisPlayer = players[i][1]
            moneyForThisPlayer = players[i][2]
            teritoriesForThisPlayer = players[i][3:]

            playerObjRead.append(Player(nameForThisPlayer, troopsForThisPlayer, moneyForThisPlayer, teritoriesForThisPlayer))
            print(playerObjRead[i])
        saveOneRead.close()

    return playerObjRead

# Save all player objects to file for slot one
def savingFileOne(playerObjWrite):
    try:
        saveOneWrite = open("savedGameOne.txt", "w")
    except:
        print("File not found.")
    else:
        for player in playerObjWrite:
            saveOneWrite.write(f"{player.name} {player.troops} {player.money} {' '.join(player.territories)}\n")
        saveOneWrite.close()

# Clear save slot one
def clearingFileOne():
    try:
        saveOneWrite = open("savedGameOne.txt", "w")
    except:
        print("File not found.")
    else:
        saveOneWrite.close()


# -------------------------------
# -------- SAVE SLOT TWO --------
# -------------------------------

# Same logic as slot one but for slot two
def makingFirstSaveOnTwo(numberOfPlayers, namesOfPlayers, moneyOfPlayers, troopsOfPlayers, territoriesOfPlayers):
    try:
        saveTwoWrite = open("savedGameTwo.txt", "w")
    except:
        print("File not found.")
    else:
        for i in range(numberOfPlayers):
            saveTwoWrite.write(f"{namesOfPlayers[i]} {troopsOfPlayers[i].troops} {moneyOfPlayers[i].money} {territoriesOfPlayers[i].territories}\n")
        saveTwoWrite.close()

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
            players.append(line.strip())

        print("there are " + str(len(players)) + " players")

        for i in range(len(players)):
            players[i] = players[i].split()
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
            saveTwoWrite.write(f"{player.name} {player.troops} {player.money} {' '.join(player.territories)}\n")
        saveTwoWrite.close()

def clearingFileTwo():
    try:
        saveTwoWrite = open("savedGameTwo.txt", "w")
    except:
        print("File not found.")
    else:
        saveTwoWrite.close()


# -------------------------------
# ------- SAVE SLOT THREE -------
# -------------------------------

# Identical structure as slot two
def makingFirstSaveOnThree(numberOfPlayers, namesOfPlayers, moneyOfPlayers, troopsOfPlayers, territoriesOfPlayers):
    try:
        saveThreeWrite = open("savedGameThree.txt", "w")
    except:
        print("File not found.")
    else:
        for i in range(numberOfPlayers):
            saveThreeWrite.write(f"{namesOfPlayers[i]} {troopsOfPlayers[i].troops} {moneyOfPlayers[i].money} {territoriesOfPlayers[i].territories}\n")
        saveThreeWrite.close()

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
            players.append(line.strip())

        print("there are " + str(len(players)) + " players")

        for i in range(len(players)):
            players[i] = players[i].split()
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
            saveThreeWrite.write(f"{player.name} {player.troops} {player.money} {' '.join(player.territories)}\n")
        saveThreeWrite.close()

def clearingFileThree():
    try:
        saveThreeWrite = open("savedGameThree.txt", "w")
    except:
        print("File not found.")
    else:
        saveThreeWrite.close()


# -------------------------------
# -------- MAIN TESTING ---------
# -------------------------------

# Load from slot one, invest and apply income to first player, and save
playerObj = saveOneReadFunct()
playerObj[0].invest()
playerObj[0].income()
savingFileOne(playerObj)
