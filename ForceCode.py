#######################
# File: Force.py
# Description: This will be 
# the file and class that 
# determine how the attacks and 
# combat mechanics will work
# Algo: 
# class Force:    
#    units = 0
#    strength of army when attacking from this territory = 0
#    defense of territory = 0
#    territoryIdx = number of territory
#    playerNum = person who owns territory
#    def ATTACK(attacker, defender)
#        boolean attackerWins
#        if attacker units is <= 1
#            you can't attack, since you must have at least one unit in each terr.
#        attacker dice = random number between 1 and 6 + attacker strength - defenders defense
#        defender dice = random number between 1 and 6 - attacker strength + defenders defense
#        
#        if attacker dice > defender dice
#            subtract random small amount from attacker
#            subtract larger amount from defender for losing    
#            print("Attacker wins, P1: x of toops left. P2: x troops left)
#            attackerWins = True
#            return attackerWins
#         if defender dice > attacker dice or dice are same number
#            defender wins
#            subtract random small amount from defender
#            subtract larger amount from attacker for losing    
#            print("Defender wins, P1: x of toops left. P2: x troops left)
#            attackerWins = False
#            return attackerWins

# History:
# 2025-06-04: Added simple attack function
# 2025-06-05: Taking territory action
# 2025-06-07: Added territory class to put in territory array
# 2025-06-09: Made defense and strength stats
# 2025-06-13: added territory index marker and fixed bugs
#######################
import random

class Force:
    units = 0
    strength = 0
    defense = 0
    territory = []
    assignments = "ABCD"
    
    # which player this class belongs to
    playNum = 0
    def __init__(self, unit, terr, playerNum, assgnmnts ):
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
