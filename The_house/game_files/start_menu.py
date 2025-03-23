#======================================================================
#Start menu functions
#start_menu.py
#======================================================================

#Internal imports
from ascii_art import ascii_art  #Import ascii art file
from text_effects import type_text, slow_dotted_text  #Import text effect file
from debug_mode import debug_menu  #Import debug mode
import game_states
import game_intro #Import game into dialogue
from rooms.room_1_car import room_1_car
from save_system import load_game
from color_scheme import RED, GREEN, CYAN, MAGENTA, YELLOW, BRIGHT_RED, BRIGHT_GREEN, BRIGHT_YELLOW, BRIGHT_CYAN, DIM_WHITE, RESET

#======================================================================

#External imports
import time
import sys

#======================================================================

#Create start menu function
def start_menu():
    print(f"\n{RED}{'=' * 70}{RESET}")  #Print border line

    #blank line
    print()

    type_text(f"{DIM_WHITE}Hello traveler...{RESET}", delay=.15)
    time.sleep(1)
    type_text(f"\n{DIM_WHITE}Welcome and thank you for playing{RESET}", delay=.15)  #slow text effect

    time.sleep(2.5)  #Small pause before logo

    #blank line
    print()

    #game title
    print(BRIGHT_RED + ascii_art["game_title"]+ RESET)

    #blank line
    print()

    print(f"\n{RED}{'=' * 70}{RESET}")  #Borderline after flashing

#======================================================================

    #pause for instructions
    time.sleep(3)

    #Game instructions
    type_text(f"\n{BRIGHT_GREEN}How to Play{RESET}", delay=.15)
    type_text("\n• Explore, uncover, and make choices by typing the number corresponding to the action you wish to take.")
    type_text(f"\n• Search for clues, interact with objects, and uncover the truth lurking within {BRIGHT_RED}The House{RESET}.")
    type_text("\nQuickly now the storm approaches... Time is fleeting... You don't have very much longer... Until madness takes it's toll...", delay=0.10)

    #pause for exit instruction
    time.sleep(2)
    type_text(f"\n• To fully {RED}exit{RESET}, you may close the game window or press {RED}Ctrl+C{RESET} at any time.")
    time.sleep(1)
    type_text(f"\n• Type '{YELLOW}pause{RESET}' at any time in the game menus to open the pause menu. From there, you can {GREEN}save{RESET}, {CYAN}load{RESET}, or {RED}exit{RESET}.")
    time.sleep(2)
#======================================================================

    #Give begin, load, and exit chocies
    while True:  #Loop until the user enters a valid option
        print(BRIGHT_GREEN + "\n1. Begin Game" + RESET)
        print(CYAN + "2. Load Game" + RESET)
        print(BRIGHT_RED + "3. Exit" + RESET)

        choice = input(f"\n{MAGENTA}Enter choice: {RESET}").strip().lower()  #Strips unwanted spaces and .lower to convert to lowercase

        if choice == "1":
            print()
            type_text(f"{DIM_WHITE}\nYou start to come to...{RESET}")
            print()#blank line
            time.sleep(2)
            return "start_game"  #Return control to main.py - sends back with start game as choice

        elif choice == "2":
            if load_game():
                from game_mechanics import visit_room
                visit_room(game_states.current_room)  #Resume game from saved state
                return  #Return after loading to prevent loop
            else:
                print(BRIGHT_RED + "\nNo saved game found. Returning to menu..." + RESET)

        elif choice == "3":
            type_text(BRIGHT_RED + "\nYou hesitate... Then decide it’s probably best to just stay put." + RESET)
            exit()#Quits game

        elif choice == "debug":
            debug_menu()  #Call the debug menu
            continue

        elif choice == "pause":
            from pause_menu import pause_menu
            pause_menu()

        else:
            print(RED + "\nInvalid choice. Type the " + BRIGHT_RED + "number associated with your option" + RED + " and try again." + RESET)  #Reloads if invalid choice

#======================================================================

