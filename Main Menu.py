def main_Menu():

    def print_header():
        program_name = "Welcome To Conquest: A Territory Strategy Game!"
        version = "1.0"
        header_text = f"{program_name} - Version {version}"
        header_width = 80
        print("\n" + "=" * header_width)
        print(header_text.center(header_width))
        print("=" * header_width + "\n")

    def show_instructions():
        instruction_title = "Instructions on How to Play Conquest!"
        header_text = f"{instruction_title}"
        header_width = 80
        print()
        print("-" * header_width)
        print(header_text.center(header_width))
        print("-" * header_width)
        print()
        instructions = ["1. Rule 1", "2. Rule 2", "3. Rule 3"]
        print("Instructions:")
        for line in instructions:
            print(line)
        print()

    def main_Menu_logic():
        while True:
            try:
                choice = input("Would you like to see the instructions? (yes/no): ").strip().lower()
                if choice == "yes" or choice == "y":
                    show_instructions()
                    break
                elif choice == "no" or choice == "n":
                    print("\nSkipping instructions...\n")
                    break
                else: 
                    print("Enter a valid input.")
            except (EOFError):
                print("\nInput interrupted. Exiting program.")
                return
            
        while True:
            try:
                start_choice = input("Type 'start' to begin the game or 'exit' to quit: ").strip().lower()
                if start_choice == "start":
                    print("\nStarting the game...\n")
                    return True
                elif start_choice == "exit":
                    print("\nExiting the game. Goodbye!\n")
                    return False
                else:
                    print("Enter a valid input.")
            except (KeyboardInterrupt, EOFError):
                print("\nInput interrupted. Exiting program.")
                return False

    print_header()
    main_Menu_logic()
