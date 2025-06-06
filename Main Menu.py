import time, sys
def main_Menu():

    def typewriter_txt(msg):
        for char in msg:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
    TITLE = "Conquest: A Territory Strategy Game"

    load_game = "\nLaunching Game...\n"
    typewriter_txt(load_game)

    time.sleep(5)

    loaded_game = f"Successfully Loaded '{TITLE}'\n"
    typewriter_txt(loaded_game)

    def print_header():
        # Prints the header of the game with the name and version.
        program_name = f"Welcome To {TITLE}!"
        version = "1.0"
        header_text = f"{program_name} - Version {version}"
        header_width = 80
        print("\n" + "=" * header_width)
        print(header_text.center(header_width))
        print("=" * header_width + "\n")

    def show_instructions():
        # Displays the instructions on how to play the game.
        instruction_title = "Instructions on How to Play Conquest!"
        header_text = f"{instruction_title}"
        header_width = 80
        print()
        print("-" * header_width)
        print(header_text.center(header_width)) # Centering the title
        print("-" * header_width)
        print()
        instructions = ["1. Rule 1", "2. Rule 2", "3. Rule 3"] # Placeholder for actual instructions
        print("Instructions:")
        for line in instructions:
            print(line)
        print()

    def main_Menu_logic():
        # Handles the logic of the main menu, including showing instructions and starting/exiting the game.
        while True:
            # Try and except to handle user input and anything else that might go wrong (which is so kevin)
            try:
                # Prompt the user to see the instructions
                choice = input("Would you like to see the instructions? (yes/no): ").strip().lower()
                # If they choose yes, show the instructions
                if choice == "yes" or choice == "y":
                    load_msg = "\nLoading...\n"
                    typewriter_txt(load_msg)
                    time.sleep(2)
                    show_instructions()
                    time.sleep(15) # Enter a realistic number in seconds that a user can read the instructions then return back to menu to start playing
                    return_msg = "Returning back to main menu...\n"
                    typewriter_txt(return_msg)
                    break
                # if they choose no,then skip the instructions
                elif choice == "no" or choice == "n":
                    skip_msg = "\nSkipping instructions...\n"
                    typewriter_txt(skip_msg)
                    time.sleep(2)
                    break
                else: 
                    print("Enter a valid input.")
            # Handle EOFerror 
            except (KeyboardInterrupt, EOFError):
                print("\nInput interrupted. Exiting program.")
                return
        
        # After showing instructions or skipping, ask if they want to start the game
        while True:
            print_header()
            try:
                # Prompt the user to start the game or exit
                start_choice = input("Type 'start' to begin the game or 'exit' to quit: ").strip().lower()
                # If they choose start, return True and print the starting message
                if start_choice == "start":
                    print("\nStarting the game...\n")
                    time.sleep(2)
                    return True
                # If they choose exit, print the exit message and return False
                elif start_choice == "exit":
                    print("\nExiting the game. Goodbye!\n")
                    return False
                else:
                    print("Enter a valid input.")
            # Handle EOFerror again - ts pmo
            except (KeyboardInterrupt, EOFError):
                print("\nInput interrupted. Exiting program.")
                return False
    # Call the print_header function to display the header
    print_header()
    main_Menu_logic()
main_Menu()
