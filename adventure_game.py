def start_game():
    print("Welcome to the Adventure Game!")
    inventory = []

    def first_room():
        print("\nYou are in a dark room. There is a door to your left and right.")
        choice = input("Which door do you take? (left/right) ").lower()
        if choice == 'left':
            left_room()
        elif choice == 'right':
            right_room()
        else:
            print("Invalid choice.")
            first_room()

    def left_room():
        print("\nYou found a key!")
        inventory.append('key')
        print(f"Inventory: {inventory}")
        first_room()

    def right_room():
        print("\nYou meet a dragon!")
        if 'key' in inventory:
            print("You use the key to open a treasure chest and win!")
        else:
            print("You have no weapon and the dragon defeats you. Game Over.")
        quit()

    first_room()

if __name__ == "__main__":
    start_game()
