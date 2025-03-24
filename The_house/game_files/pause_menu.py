#======================================================================
# pause menu functions
# pause_menu.py
#======================================================================

# Internal imports
from save_system import save_game, load_game
from game_mechanics import visit_room
from debug_mode import debug_menu
import game_states
from color_scheme import GREEN, RED, YELLOW, CYAN, MAGENTA, RESET

#======================================================================

# External imports
# (None needed right now)

#======================================================================

# pause menu function
def pause_menu():
    while True:
        print("\n[PAUSED] What would you like to do?")
        print(f"{MAGENTA}1. Resume Game{RESET}")
        print(f"{GREEN}2. Save Game{RESET}")
        print(f"{CYAN}3. Load Game{RESET}")
        print(f"{YELLOW}4. Return to Main Menu{RESET}")
        print(f"{RED}5. Quit Game{RESET}")

        choice = input("> ").strip().lower()

        if choice == "1":
            print(f"\n{GREEN}Resuming game...{RESET}")
            return  #Go back to wherever pause was triggered from

        elif choice == "2":
            save_game()

        elif choice == "3":
            if load_game():
                visit_room(game_states.current_room)
                return  #Prevent further loop after loading


        elif choice == "4":
            print(f"\n{YELLOW}Returning to main menu...{RESET}")
            from start_menu import start_menu  #prevents circular import
            from game_mechanics import full_reset_game

            full_reset_game()  #Reset all game states and sounds

            choice = start_menu()  #Restart main menu fresh

            if choice == "start_game":
                from rooms.room_1_car import room_1_car
                room_1_car()

            return

        elif choice == "5":
            print(f"\n{RED}Exiting game. Goodbye.{RESET}")
            exit()

        elif choice == "debug":
            debug_menu()

        else:
            print(f"\n{RED}Invalid choice. Try again.{RESET}")