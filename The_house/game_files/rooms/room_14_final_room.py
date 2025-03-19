#======================================================================
#Final Room - Ending of the Game
#room_14_final_room.py
#======================================================================

#Internal imports
import game_states
from text_effects import type_text, slow_dotted_text
from game_mechanics import visit_room, distort_name
from start_menu import start_menu  #To return to the main menu
from ascii_art import ascii_art
from debug_mode import debug_menu

#======================================================================

#External imports
import random
import time

#======================================================================
#Final function room: 14 - The Ending
def room_14_final_room():
    #Room tracker
    room_name = "room_14_final_room"
    visit_count = game_states.room_visits.get(room_name, 0)

    slow_dotted_text("\nYou step through the doorway. The air is warm and familiar, like you have been here before")
    time.sleep(1)

    type_text("A soft glow fills the space ahead. It feels... safe.")
    time.sleep(1)

    type_text("\nYour thoughts begin to clear. The memories return in waves...")
    time.sleep(1)
    slow_dotted_text("The Rain")
    time.sleep(.5)
    slow_dotted_text("The Road")
    time.sleep(.5)
    slow_dotted_text("The Crash")
    time.sleep(.5)
    slow_dotted_text("The House")
    time.sleep(1)

    type_text("\nSomewhere in the distance, a child cries. A lullaby hums softly in response.")
    type_text("The weight in your chest begins to fade. The fear loosens its grip.")
    time.sleep(1)

    type_text("\nYou feel something calling you forward. And then... you hear a name...")
    time.sleep(2)

    slow_dotted_text(f"\n'{game_states.player_name}'... Are you there, do you hear me?")
    time.sleep(1)

    type_text("\nThe air seems to tremble.")
    time.sleep(1)

    type_text("\nYou feel a strange pull, a soft whisper calling you forward.")
    time.sleep(1)

    type_text("\nThe name almost feels like a vague memory...")
    time.sleep(1)

    slow_dotted_text(f'"You\'re almost there"')
    time.sleep(1)

    #Final Choice
    print("\nWhat do you want to do?")
    print("1. Step forward into the light")

    while True:
        choice = input("> ").strip()

        if choice == "1":
            #Second name call - distorted
            distorted_name = distort_name(game_states.player_name, stage=2)
            time.sleep(1)
            slow_dotted_text(f"\n'{distorted_name}...?' The voice warps, muffled, as if the sound is slipping away")

            end_game()  #Proceed to the end of the game after the name distortion
            return
        else:
            time.sleep(1)
            type_text("\nSomething urges you forward. There is no other path. You must move on.")
            time.sleep(1)

#======================================================================
#End game function
def end_game():
    type_text("\nYou step forward as the light engulfs you.")
    type_text("The weight you've carried lifts, and the fear fades.")
    time.sleep(1)

    type_text("\nThe lullaby grows clearer. A soft, distant voice hums with it.")
    slow_dotted_text("\nFor the first time in what feels like forever... you have this unexplainable sense of peace")
    time.sleep(2)

    #third name call fully distorted
    distorted_name = distort_name(game_states.player_name, stage=3)
    time.sleep(1)
    type_text(f"\nYour name now lost, distorted, incomprehensible. The world around you feels lost.")
    time.sleep(1)
    slow_dotted_text(f"The light grows stronger, blinding... you hear the voice one final time... {distorted_name}")
    time.sleep(1)

    type_text("\nAt last...")

    #Display ending artwork
    print(ascii_art["ending"])

    type_text("\nTHE END.")
    time.sleep(2)

    input("\nPress Enter to return to the main menu.")  #Pause before restarting
    full_reset_game()
    start_menu()  #Return to the main menu

#======================================================================
