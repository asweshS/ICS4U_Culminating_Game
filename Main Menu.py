def main_Menu():
    # This function displays the main menu of the game and handles user input.

    def print_header():
        # Prints the header of the game with the name and version.
        program_name = "Welcome To Conquest: A Territory Strategy Game!"
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
                    show_instructions()
                    break
                # if they choose no,then skip the instructions
                elif choice == "no" or choice == "n":
                    print("\nSkipping instructions...\n")
                    break
                else: 
                    print("Enter a valid input.")
            # Handle EOFerror 
            except (EOFError):
                print("\nInput interrupted. Exiting program.")
                return
        
        # After showing instructions or skipping, ask if they want to start the game
        while True:
            try:
                # Prompt the user to start the game or exit
                start_choice = input("Type 'start' to begin the game or 'exit' to quit: ").strip().lower()
                # If they choose start, return True and print the starting message
                if start_choice == "start":
                    print("\nStarting the game...\n")
                    return True
                # If they choose exit, print the exit message and return False
                elif start_choice == "exit":
                    print("\nExiting the game. Goodbye!\n")
                    return False
                else:
                    print("Enter a valid input.")
            # Handle EOFerror again - ts pmo
            except (EOFError):
                print("\nInput interrupted. Exiting program.")
                return False
    # Call the print_header function to display the header
    print_header()
    main_Menu_logic()
main_Menu()
