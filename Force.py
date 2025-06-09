#######################
# File: Force.py
# Description: This will be 
# the files and classes that 
# determine how the atttacks and 
# combat mechanics will work
# History:
# 2025-06-04: Added simple attack function
# 2025-06-05: Taking territory action
# 2025-06-07: Started territory array and management
# 2025-06-09: Made defense and strength stats
#######################
import random

# force is from the perspective of the attacker
class Force:
    units = 0
    strength = 0
    territory = []
    
    # which player this class belongs to
    playNum = 0
    def __init__(self, unit, terr, playerNum):
        self.units = unit
        self.territory = terr
        self.playNum = playerNum
        print("units: ", self.units)

    # roll dice and see who wins, defense is p2
    def Attack(self, p2, terr):

        # when attacker doesn't have enough units
        if (self.units <= 1):
            print("You cannot attack, you dont have enough units")
            return

        # attacker dice
        dice1 = random.randint(1, 6)
        # defense dice
        dice2 = random.randint(1, 6)

        # attacker dice is higher
        if (dice1 > dice2):
            p2.units -= 1
            print("player 1 wins (p1: %s units left, p2: %s units left)" % (self.units, p2.units))

        # defender dice is higher or dice are even
        if (dice2 > dice1 or dice1 == dice2):
            self.units -= (50 - terr.defense) + self.strength
            print("player 2 wins (p1: %s units left, p2: %s units left)" % (self.units, p2.units))
            
        # if defender is out of units, then give land to attacker
        if (p2.units == 0): 
            self.territory.append(terr)

            # find the spot in opponents list and remove
            for idx in p2.territory:
                if (idx == terr):
                    del(p2.territory)
                    break
        # output the new territory
        return (self.territory, p2.territory)
