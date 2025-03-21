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


#======================================================================

#External imports
import time
import sys

#======================================================================

#Create start menu function
def start_menu():
    print("\n" + "=" * 70)  #Print border line

    #blank line
    print()

    slow_dotted_text("Hello traveler")
    time.sleep(1)
    type_text("\nWelcome and thank you for playing", delay= .15)  #slow text effect

    time.sleep(2.5)  #Small pause before logo

    #blank line
    print()

    #game title
    print(ascii_art["game_title"])

    #blank line
    print()

    print("=" * 70)  #Borderline after flashing

#======================================================================

    #pause for instructions
    time.sleep(3)

    #Game instructions
    slow_dotted_text("\nHow to Play")
    type_text("\n• Explore, uncover, and make choices by typing the number corresponding to the action you wish to take.")
    type_text("\n• Search for clues, interact with objects, and uncover the truth lurking within The House.")
    type_text("\nQuickly now the storm approaches... Time is fleeting... You don't have very much longer... Until madness takes it's toll...", delay=0.15)

    #pause for exit instruction
    time.sleep(2)
    type_text("\n• To fully exit, you may close the game window or press Ctrl+C at any time.")
    time.sleep(1)
    type_text("\n• Type 'pause' at any time in the game menus to open the pause menu. From there, you can save, load, or exit.")
    time.sleep(2)
#======================================================================

    #Give begin, load, and exit chocies
    while True:  #Loop until the user enters a valid option
        print("\n1. Begin Game")
        print("2. Load Game")
        print("3. Exit")

        choice = input("\nEnter choice: ").strip().lower()  #Strips unwanted spaces and .lower to convert to lowercase

        if choice == "1":
            slow_dotted_text("\nYou start to come to")
            print()#blank line
            time.sleep(2)
            return "start_game"  #Return control to main.py - sends back with start game as choice

        elif choice == "2":
            if load_game():
                from game_mechanics import visit_room
                visit_room(game_states.current_room)  #Resume game from saved state
                return  #Return after loading to prevent loop
            else:
                print("\nNo saved game found. Returning to menu...")

        elif choice == "3":
            type_text("\nYou hesitate... Then decide it’s probably best to just stay put.")
            exit()#Quits game

        elif choice == "debug":
            debug_menu()  #Call the debug menu
            continue

        elif choice == "pause":
            from pause_menu import pause_menu
            pause_menu()

        else:
            print("\nInvalid choice. Type the number associated with your option and try again.")  #Reloads if invalid choice

#======================================================================

