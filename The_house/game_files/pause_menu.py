#======================================================================
# pause menu functions
# pause_menu.py
#======================================================================

# Internal imports
from save_system import save_game, load_game
from game_mechanics import visit_room
from debug_mode import debug_menu
import game_states

#======================================================================

# External imports
# (None needed right now)

#======================================================================

# pause menu function
def pause_menu():
    while True:
        print("\n[PAUSED] What would you like to do?")
        print("1. Resume Game")
        print("2. Save Game")
        print("3. Load Game")
        print("4. Return to Main Menu")
        print("5. Quit Game")

        choice = input("> ").strip().lower()

        if choice == "1":
            print("\nResuming game...")
            return  #Go back to wherever pause was triggered from

        elif choice == "2":
            save_game()

        elif choice == "3":
            if load_game():
                visit_room(game_states.current_room)
                return  #Prevent further loop after loading


        elif choice == "4":
            print("\nReturning to main menu...")
            from start_menu import start_menu  #prevents circular import
            choice = start_menu()
            if choice == "start_game":
                from rooms.room_1_car import room_1_car
                room_1_car()

            return

        elif choice == "5":
            print("\nExiting game. Goodbye.")
            exit()

        elif choice == "debug":
            debug_menu()

        else:
            print("\nInvalid choice. Try again.")