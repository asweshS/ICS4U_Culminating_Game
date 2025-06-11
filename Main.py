#######################
# File: Main.py
# Authors: Ryan MacLeod, Aswesh Sritharakumar, Devan Lucas, Andrew Urquhat
# Desc: This is the main project file that
# will integrate all of the files into one
# main program.
#######################

#import Map
import Force
#import PartA
import main_menu
import player

class masterPlayer:
    ord = 0
    playerClass = ""
    #force = Force.Force

    def __init__(self, order):
        self.ord = order
        self.playerClass = self.askName()

    def askName(self):
        print("Whats is player %s name? " % self.ord, end="")
        return player.Player(input())

    def __str__(self):
        return self.playerClass


def askPlayers():
    print("How many players between 2 and 4: ", end="")
    playerAmt = int(input())

    # if theres more than 4 players or less than 2, try again
    if (playerAmt > 4 or playerAmt < 2):
        print("Invalid amount of players, try again")
        return askPlayers()
    return playerAmt
    
# put players in a master class and then an array to make organizing easier
playerArr = []
for idx in range(askPlayers()):
    playerArr.append(masterPlayer(idx + 1))


def Turn():
    for idx in range(len(playerArr)):
        print("%s's turn: " % playerArr[idx].playerClass.name)
    
Turn()
