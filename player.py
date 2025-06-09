# Name:Andrew Urquhart
# course: ICS4U
# file urquhart_andrew_Culmanating.py
# description:
#   
# INPUTS:

# OUTPUTS:

# ALGORITHM
#   1. Create a Player class with attributes for name, money, resources, territories, forces, and factory count.
#   2. Implement a method to create a factory that costs money and increases daily income.
# HISTORY
#   2025.06.02- created player class with attributes and methods for a basic resources game


class Player:
    daysGoneBy = 0

    def __init__(self, name):
        self.name = name
        self.military = 100
        self.territories = 5
        self.money = 0

    def income(self,invest):
        self.daily_income = 1000 + (self.territories * 100)
        if invest == 1:
            self.daily_income += 500
        elif invest == 2:
            self.daily_income += 1000
        self.money += self.daily_income

    def buy_military(self):
        self.military += 10
        self.money -= 100000



    def __str__(self):  
        return f"Player {self.name} has {self.money} money, {self.military} soldiers, and controls {self.territories} territories with {self.factory_count} factories."
    
john = Player("John")


try:
    saveOne = open("One.txt", "r")
except:
    print("File not found.")
else:
    j = saveOne.readline(10)
    #saveOne.write(str(john.name) + "\n")
    #saveOne.write(str(john.money) + "\n")
    #saveOne.write(str(john.factory_count) + "\n")
    #saveOne.write(str(john.military) + "\n")
    #print("DONE")
    saveOne.close()
