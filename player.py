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

    def __init__(self, name):
        self.name = name
        self.troops = 100
        self.territories = 5
        self.money = 0

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
        return f"Player {self.name} has {self.money} money, {self.troops} soldiers, and controls {self.territories} territories with {self.factory_count} factories."
    
john = Player("John")


try:
    saveOneRead = open("One.txt", "r")
except:
    print("File not found.")
else:
    lines = saveOneRead.readlines()
    playerCount = 0
    for line in lines:
        print(line)
        if (line == "1"):
            playerCount+=1
    print(playerCount)
    saveOneRead.close()

try:
    saveOneWrite = open("One.txt", "w")
except:
    print("File not found.")
else:
    saveOneWrite.write("1")
    saveOneWrite.write("\n" + str(john.name) + "\n")
    saveOneWrite.write(str(john.money) + "\n")
    saveOneWrite.write(str(john.troops) + "\n")

    saveOneWrite.close()
