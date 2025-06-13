#######################
# File: Force.py
# Description: This will be 
# the files and classes that 
# determine how the atttacks and 
# combat mechanics will work
# History:
# 2025-06-04: Added simple attack function
# 2025-06-05: Taking territory action
# 2025-06-07: Added territory class to put in territory array
# 2025-06-09: Made defense and strength stats
# 2025-06-13: added territory index marker and fixed bugs
#######################
import random

# force is from the perspective of the attacker
class Force:
    units = 100
    strength = 0
    territoryIdx = 0
    playerOwn = 0
    defense = 0
    
    # which player this class belongs to
    playNum = 0
    def __init__(self, idx, unit=100, playerNum=None):
        self.playerOwn = playerNum
        self.units = unit
        self.territoryIdx = idx
        #print("units: ", self.units)

    # roll dice and see who wins, defense is p2
    def Attack(self, p2):

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
            self.units -= random.randint(25, 50) - p2.defense + self.strength
            p2.units -= random.randint(25, 50) - p2.defense + self.strength
            
            print("player 1 wins (p1: %s units left, p2: %s units left)" % (self.units, p2.units))
            return True

        # defender dice is higher or dice are even
        if (dice2 > dice1 or dice1 == dice2):

            # winner still loses troops, depending on strength of other force
            p2.units -= random.randint(0, 20) + self.strength - p2.defense

            self.units -= random.randint(25, 50) + p2.defense - self.strength
            print("player 2 wins (p1: %s units left, p2: %s units left)" % (self.units, p2.units))
            return False
        '''
        # if defender is out of units, then give land to attacker
        if (p2.units == 0): 
            self.territory.append(p2)

            # find the spot in opponents list and remove
            for idx in p2.territory:
                if (idx == p2):
                    del(p2.territory)
                    break
        # output the new territory
        '''
