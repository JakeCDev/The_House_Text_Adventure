#======================================================================
#Main game file for 'The House' - By Jake Chrissinger
#main.py
#======================================================================

#Import modules

from start_menu import start_menu
from game_mechanics import visit_room, get_player_name
from game_intro import game_intro
import game_states  #Import game state tracker before anything else to ensure tracks properly
from text_effects import type_text
from color_scheme import BRIGHT_GREEN, RESET
import time

#======================================================================
#Game start
#======================================================================

#Create entry/start point of game "main"
def main():
    #Load in/run the start_menu.py file
    choice = start_menu()

#Received start game choice from start_menu
    if choice == "start_game":
        #Show intro sequence - run game_intro
        game_intro()

#Ask for confirmation after intro but before the game sends you to the first room
        input(f"\n{BRIGHT_GREEN}Press enter to begin the game...{RESET}")
        time.sleep(1)
        get_player_name()
        time.sleep(1)
        #Start the game in the car room
        visit_room("room_1_car")

#======================================================================
#Run game
#======================================================================

if __name__ == "__main__":
    main()  #Only runs if this file is executed directly

#======================================================================