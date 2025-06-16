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
import MainMenu
import GamePlay
import sys
import time
import random
import os
def typewriterTxt(msg, timeTake):
            for char in msg:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(random.randint(0,10)/100*timeTake)
MainMenu.initialization_of_game()
time.sleep(0.5)
os.system('cls')
typewriterTxt("initializing game...",2)
os.system('cls')
typewriterTxt("Making map",2)
os.system('cls')
typewriterTxt("Loading files...",2)
os.system('cls')
print("Game Starting, goodluck to all and  have fun!\n")
typewriterTxt("█████████████████████████████████████████████\n", 5)
os.system('cls')
time.sleep(1)               
GamePlay.gamePlay()
