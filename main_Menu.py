import os
import time, sys

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
