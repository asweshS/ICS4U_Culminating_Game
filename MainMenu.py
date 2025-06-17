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
        time.sleep(1)
        def print_header():
            os.system('cls')
            header_width = 80
            print("\n" + "=" * header_width)
            print(f"Welcome To {TITLE}!".center(header_width))
            print("Version 1.0".center(header_width))
            print("=" * header_width + "\n")

        def show_instructions():
            os.system('cls')
            header_width = 80
            print("-" * header_width)
            print("Instructions on How to Play Conquest!".center(header_width))
            print("-" * header_width)
            print()
            instructions = [
                  "OBJECTIVE", #More actions
                "-" * 40, 
                "| Conquer all 12 territories on the map before your opponents do. The first player to control all territories win!",
                "\n",
                "SETUP",
                "-" * 40,
                "1. Players:",
                "| The game supports 2-4 players.",
                "| Each player chooses a name.",
                "",
                "2. Turn Order:",
                "| Players are randomly assigned a turn order(A, B, C, D).",
                "",
                "3. Territory Selection:",
                "| There are 12 territories, each represented by numbers 1-12.",
                "| Players take turns picking unclaimed territory until all are claimed.",
                "| On each turn, a player selects a territory by entering its number and confirms their choice.",
                "",
                "4. Starting Troops:",
                "| Each territory grants 100 troops to the owner at the start.",
                "| Players begin with $0 money."
                "\n",
                "GAMEPLAY",
                "-" * 40,
                "1. Income: ",
                "| At the start of each round (after the first), each player receives $500 plus $100 per owned territory.",
                "",
                "2. Map Display",
                "| The map and your status (money, troops, territories) are shown.",
                "",
                "3. Choose an Action: ",
                "   1. Invest: ",
                "       | Adds $1000 to your money balance.",
                "   2. Purchase Troops: ",
                "       | Buy as many troops as you wish at $100 per troop, provided you have enough money.",
                "       | Enter the number of troops to buy.",
                "   3. Attack: ",
                "       | Attempt to conquer an opponent's territory adjacent to one of yours.",
                "       | Select which of your territories to attack from.",
                "       | Select an adjacent enemy territory to attack.",
                "       | Combat is resolved by rolling dice (with troop numbers as multipliers). The winner keeps the territory and the loser loses 100 troops.",
                "       | If you win, you take control of the territory.",
                "",
                "4. End of Turn: ",
                "| After your action, the next player's turn begins",
                "",
                "5. Winning the Game: ",
                "| If you control all 12 territories, you win!",
                "\n"
                "ADDITIONAL RULES",
                "-" * 40,
                "Territories: ",
                "| You can only attack territories that are adjacent to yours and not already owned by you.",
                "| If you lose all territories, you are effectively out of the game.",
                "",
                "Troops: ",
                "| Troops are required to attack and defend territories.",
                "| Troops can be purchased with money.",
                "",
                "Money: ",
                "| Earned by getting investments or income at the end of each round.",
                "",
                "Rounds: ",
                "| A round is completed when all players have taken a turn.",
                "\n",
                "CONTROLS",
                "-" * 40,
                "| All inputs are prompted in the command line.",
                "| Confirm all territory selections and attack choices as prompted.",
                "\n",
                "TIPS",
                "-" * 40,
                "| Plan your attacks strategically! Attacking with more troops increases your chance to win.",
                "| Invest early on to build up funds for buying troops.",
                "| Pay attention to where the territories are for attacking opportunities!",
                "\n",
                "-" * 40,
                "Good luck and have fun!"
                            ]
            for line in instructions:
                print(line)
            print()
            input("Press Enter to return to the main menu...")

        def main_Menu_logic():
            while True:
                print_header()
                print("MAIN MENU".center(80, "-"))
                print()
                print("1. See Instructions")
                print("2. Start Game")
                print("3. Exit")
                choice = input("\nEnter your choice (1-3): ").strip()
                if choice == "1":
                    show_instructions()
                elif choice == "2":
                    return True
                elif choice == "3":
                    print("\nExiting the game. Goodbye!\n")
                    sys.exit()
                else:
                    print("\nEnter a valid input (1-3).")
                    time.sleep(1)

        return main_Menu_logic()

def clear_screen():
    os.system('cls')
def initialization_of_game():
    player_type = intro.main_Menu()
