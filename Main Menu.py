def main_Menu_Header():
    program_name = "Welcome To Conquest: A Territory Strategy Game!"
    version = "1.0"
    header_text = f"{program_name} - Version {version}"
    header_width = 100
    print()
    print("=" * header_width)
    print(header_text.center(header_width))
    print("=" * header_width)
    print()

    def show_instructions():
        program_name = "Instructions on How to Play Conquest!"
        header_text = f"{program_name}"
        header_width = 100
        print()
        print("=" * header_width)
        print(header_text.center(header_width))
        print("=" * header_width)
        print()
        instructions = ["1. Rule 1", "2. Rule 2", "3. Rule 3"]
        print("Instructions:")
        for line in instructions:
            print(line)
        print()

    def main_Menu():
        choice = input("Would you like to see the instructions? (yes/no): ").strip()
        if choice == "yes" or choice == "Yes" or choice == "Y":
            show_instructions()
        elif choice == "no" or choice == "No" or choice == "N":
            print("\nAlright, let's proceed to the game!\n")
        
        else: 
            print("Enter a valid input.")

    main_Menu()

main_Menu_Header()
