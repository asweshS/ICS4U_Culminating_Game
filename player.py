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
        
        for i in range(len(self.territories)):
            printOutStatement.append(str(self.territories[i])+ " ")
        printOutStatement = "".join(printOutStatement)
            
        return printOutStatement
    

    def __str__(self):
        return str(self.name)
