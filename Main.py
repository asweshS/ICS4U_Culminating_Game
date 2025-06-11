#######################
# File: Main.py
# Authors: Ryan MacLeod, Aswesh Sritharakumar, Devan Lucas, Andrew Urquhart
# Desc: This is the main project file that
# will integrate all of the files into one
# main program.
# History:
# 2025-06-10: Created file
# 2025-06-11: added opening save file
#######################

import Force
#import MainMenu
#import PartA
import player

class masterPlayer:
    ord = 0
    playerClass = ""
    #force = Force.Force

    def __init__(self, order, saveName):
        self.ord = order
        #self.playerClass = self.askName()
        self.checkSave(saveName)

    # check if a save has been loaded
    def checkSave(self, saveName):
        # might not be finsished yet
        try:
            save1 = open("saveName",'x')
        except FileExistsError:
            return True
        return False

    def __str__(self):
        return self.playerClass

def openSave():
    print("Do you want to open a save file (y or n): ", end="")
    des = input()
    if (des == 'y'):
        print("loadSave")

        try: 
            fileNum = int(input("Which save do you want to open (1-3): "))
        except ValueError:
            print("Invalid save number, try again")
            return openSave()
        else: 
            if (0 < fileNum < 4):
                fileName = "save" + fileNum
                return fileName
            else:
                print("Number is out of range, try again")
                return openSave()
        
    elif (des == "n"):
        print("Make new game")
        return
    else:
        print("invalid input, try again")
        return openSave()


openSave()
player = masterPlayer(1)
