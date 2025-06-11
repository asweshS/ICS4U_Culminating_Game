######################################
# File Name: main_menu.py
# Author(s): Aswesh Sritharakumar
# Description: A main menu program that is the first user interface (UI) for the player when they enter the game
# History:
# 2025-06-04 Created the header for the game 
# 2025-06-05 Added a concept for the instructions menu and created a start game or exit game input
# 2025-06-06 Found how to do a typewriter effect, which makes it seem more professional
# 2025-06-08 Created a simple launching game prompt
# 2025-06-10 FINALLY figured out how to clear the screen after an input is given from the user, this makes it look professional, and I will not change it cuz it looks cool
######################################


import os
import time, sys

# I'm ngl I think I cooked with this one, straight fire
class intro: # using a class because it just makes it easier (imo) when everyone else is using a class
    def main_Menu():
        def typewriter_txt(msg):
            for char in msg:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.02)

        TITLE = "Conquest: A Territory Strategy Game"
        load_game = "\nLaunching Game...\n"
        typewriter_txt(load_game)
        time.sleep(1)
        loaded_game = f"Successfully Loaded '{TITLE}'\n"
        typewriter_txt(loaded_game)

        # print the header 
        def print_header():
            os.system('cls') # I FINALLY FIGURED OUT HOW TO CLEAR THE SCREEN LET'S GO
            header_width = 80
            print("\n" + "=" * header_width)
            print(f"Welcome To {TITLE}!".center(header_width))
            print("Version 1.0".center(header_width))
            print("=" * header_width + "\n")

        def show_instructions():
            os.system('cls') # Basically, what this does is, before showing the instructions page, it will just clear everything before it and then create a new clean terminal and then display whatever is after that  
            header_width = 80
            print("-" * header_width)
            print("Instructions on How to Play Conquest!".center(header_width))
            print("-" * header_width)
            print()
            instructions = ["1. -", "2. -", "3. -"] # Place holder for actual instructions
            for line in instructions:
                print(line)
            print()
            input("Press Enter to return to the main menu...")

        def main_Menu_logic():
            while True:
                print_header()
                print("MAIN MENU".center(80, "-"))
                print("1. See Instructions")
                print("2. Start Game")
                print("3. Exit")
                choice = input("\nEnter your choice (1-3): ").strip()
                if choice == "1":
                    show_instructions()
                elif choice == "2":
                    print("\nStarting the game...\n")
                    time.sleep(1)
                    return True
                elif choice == "3":
                    print("\nExiting the game. Goodbye!\n")
                    sys.exit()
                else:
                    print("Enter a valid input (1-3).")
                    time.sleep(1)

        main_Menu_logic()

def clear_screen():
    os.system('cls')

intro.main_Menu()
