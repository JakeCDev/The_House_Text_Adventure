#======================================================================
#Final Room - Ending of the Game
#room_14_final_room.py
#======================================================================

#Internal imports
import game_states
from text_effects import type_text
from game_mechanics import visit_room
from start_menu import start_menu  #To return to the main menu
from ascii_art import ascii_art
from debug_mode import debug_menu

#======================================================================
#Final function room: 14 - The Ending
def room_14_final_room():
    #Room tracker
    room_name = "room_14_final_room"
    visit_count = game_states.room_visits.get(room_name, 0)

    type_text("\nYou step through the doorway. The air is warm, familiar.")
    type_text("A soft glow fills the space ahead. It feels... safe.")

    type_text("\nYour thoughts begin to clear. The memories return in waves...")
    type_text("The rain. The road. The crash.")

    type_text("\nSomewhere in the distance, a child cries. A lullaby hums softly in response.")
    type_text("The weight in your chest begins to fade. The fear loosens its grip.")

    type_text("\nThere is no turning back.")

    #Final Choice
    print("\nWhat do you want to do?")
    print("1. Step forward into the light")

    attempts = 0
    while attempts < 3:
        choice = input("> ").strip()

        if choice == "1":
            end_game()
            return
        else:
            type_text("\nSomething urges you forward. There is no other path.")
            attempts += 1

    type_text("\nAn unseen force pulls you forward...")
    end_game()

#======================================================================
#End game function
def end_game():
    type_text("\nYou step forward. The light engulfs you.")
    type_text("The weight you've carried lifts, and the fear fades.")

    type_text("\nThe lullaby grows clearer. A soft, distant voice hums with it.")
    type_text("\nFor the first time in what feels like forever... you understand.")

    type_text("\nAt last... you are free.")

    #Display ending artwork
    print(ascii_art["ending"])

    type_text("\nTHE END.")

    input("\nPress Enter to return to the main menu.")  #Pause before restarting
    full_reset_game()
    start_menu()  #Return to the main menu

#======================================================================
