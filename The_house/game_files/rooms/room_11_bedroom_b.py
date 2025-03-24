#======================================================================
#Bedroom B: Room 11
#room_11_bedroom_b.py
#======================================================================

#Internal imports
import game_states
from game_mechanics import visit_room, check_inventory, universal_wait
from text_effects import type_text
from ascii_art import ascii_art
from debug_mode import debug_menu
from pause_menu import pause_menu
from color_scheme import YELLOW, MAGENTA, BLUE, CYAN, RED, GREEN, DIM_WHITE, RESET
from sound_manager import play_ambient_loop, stop_ambient_loop, play_sound_effect
import random
import time

#======================================================================
#Bedroom B function

def room_11_bedroom_b():
    #Room tracker
    room_name = "room_11_bedroom_b"
    visit_count = game_states.room_visits.get(room_name, 0)

    #Room state changes
    if visit_count == 0:  #Present
        type_text("\nThe bed is neatly made, untouched.")
        type_text("A dresser stands against the wall.")

    elif visit_count == 1:  #Past
        type_text("\nThe bed is now messy, covered in laundry. As if someone just got up or was mid-cleaning.")
        type_text(f"A book rests on the nightstand, a glass of {CYAN}water{RESET} beside it.")

    elif visit_count == 2:  #Future
        type_text("\nThe room is lined with boxes and bags... it's hard to tell if someone is coming or going...")
        type_text("Faint marks on the floor show where old furniture once sat.")

    elif visit_count == 3:  #Eerie
        type_text(f"\nYou feel a {RED}breath{RESET} on your neck...")
        type_text("You turn and no one is there.")

    else:  #Altered Reality
        type_text("\nThe bed hovers feet above the ground...")
        type_text(f"The mirror ripples like {CYAN}water{RESET}, reflecting a room that isn’t the same.")

#======================================================================

    #Bedroom B art
    print(ascii_art["bedroom_b"])

#======================================================================
    #Bedroom B choices
    while True:
        print("\nWhat do you want to do?")
        print("1. Look around")
        print("2. Wait around in Bedroom B")
        print("3. Go back to the Upstairs Hallway")
        print("4. Check Inventory")

        choice = input("> ").strip()

        if choice == "1":
            look_around_bedroom_b()

        elif choice == "2":
            universal_wait()
            input(f"\nPress {GREEN}Enter{RESET} to continue.")

        elif choice == "3":
            game_states.room_visits[room_name] += 1
            visit_room("room_10_upstairs_hallway")

        elif choice == "4":
            check_inventory(room_11_bedroom_b)

        elif choice == "debug":
            debug_menu()  # Calls the debug menu

        elif choice == "pause":
            pause_menu()

        else:
            print(f"\n{RED}Invalid choice. Try again.{RESET}")

#======================================================================
#Looking around in Bedroom B

def look_around_bedroom_b():
    while True:
        type_text("\nYou scan the bedroom. What do you want to check?")
        print("1. The Bed")
        print("2. The Closet")
        print("3. The Desk")
        print(f"4. {RED}Nevermind{RESET}")

        choice = input("> ").strip()

        if choice == "1":
            type_text("\nThe sheets look cozy... but this is no time for a nap.")
            print(ascii_art["bed_b"])

        elif choice == "2":
            type_text("\nThe closet door is slightly open. A musty smell drifts out, but there's nothing inside except old clothes.")
            print(ascii_art["bedroom_b_closet"])

        elif choice == "3":
            if "Safe Order Hint" not in game_states.inventory:
                stop_ambient_loop("house", fade_out=1000)
                time.sleep(1)
                play_ambient_loop("music_box", "music_box.wav", 0.6)
                time.sleep(8)
                type_text("\nOn the desk, a music box begins to play on its own... Next to it sits an old note under a layer of dust. It reads:")
                type_text("\n\"First, down below, where there was no sight,")
                type_text("\nThen at the table, in flickering light,")
                type_text("\nAt last, where the clock forgets what’s wrong from right.")
                type_text(f"\nThis feels important... Maybe it is a password hint to something... {GREEN}You commit it to memory{RESET}.")
                print(ascii_art["bedroom_b_desk"])
                game_states.inventory.append("Safe Order Hint")
            else:
                type_text(f"\n{YELLOW}The desk is empty now, the note we took was the only thing of interest here it seems{RESET}.")

        elif choice == "4":
            return  #Exit back to the bedroom menu

        elif choice == "debug":
            debug_menu()  #Calls the debug menu

        elif choice == "pause":
            pause_menu()

        else:
            print(f"\n{RED}Invalid choice. Try again{RESET}.")

#======================================================================