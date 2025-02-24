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

    type_text("Hello,", delay=0.3)
    slow_dotted_text("\nWelcome and thank you for playing")  #slow text effect

    time.sleep(.5)  #Small pause before flashing logo

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
    type_text("\nHow to Play:", delay=0.3)
    type_text("\n• Explore, uncover, and make choices by typing the number corresponding to the action you wish to take.")
    type_text("\n• Search for clues, interact with objects, and uncover the truth lurking within The House...")
    type_text("\nThe storm approaches... Time feels fleeting... You don't have very much longer... Until madness takes it's toll...", delay=0.15)

    #pause for exit instruction
    time.sleep(3)
    print("\n• To exit, you may close the game window or press Ctrl+C at any time.")

#======================================================================

    #Give "begin game" and "exit" choices.
    while True:  #Loop until the user enters a valid option
        print("\n1. Begin Game")
        print("2. Exit")

        choice = input("\nEnter choice: ").strip().lower()  #Strips unwanted spaces and .lower to convert to lowercase

        if choice == "1":
            type_text("\nYou begin to regain clarity...", delay=0.15)
            print()#blank line
            time.sleep(2)
            return "start_game"  #Return control to main.py - sends back with start game as choice
        elif choice == "2":
            type_text("\nYou hesitate... Then decide it’s probably best to just stay put.")
            exit()#Quits game
        elif choice == "debug":
            debug_menu()  #Call the debug menu
            continue
        else:
            print("\nInvalid choice. Try again.")  #Reloads if invalid choice

#======================================================================

