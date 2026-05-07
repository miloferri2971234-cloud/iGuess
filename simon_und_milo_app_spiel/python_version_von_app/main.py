from src.core.städte_kette_game import städte_kette_game

def show_menu():
    print("1. Städte-Kette")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Exit")
    
def main():
    while True:
        show_menu()
        choice = input("Please select an option: ")
        
        if choice == '1':
            städte_kette_game()
        elif choice == '2':
            print("You selected Option 2")
        elif choice == '3':
            print("You selected Option 3")
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
