#======================================================================
#Basement Room: 7
#room_7_basement.py
#======================================================================

# Internal imports
import game_states
from game_mechanics import visit_room, check_inventory, inspect_safe, universal_wait
from text_effects import type_text
from ascii_art import ascii_art
from debug_mode import debug_menu
from pause_menu import pause_menu
from color_scheme import YELLOW, MAGENTA, BLUE, CYAN, RED, GREEN, DIM_WHITE, RESET
from sound_manager import stop_ambient_loop, play_ambient_loop, play_sound_effect
import random

#======================================================================
#Basement function

def room_7_basement():

    #Room tracker
    room_name = "room_7_basement"
    visit_count = game_states.room_visits.get(room_name, 0)

    #music
    stop_ambient_loop("house", fade_out=1000)
    play_ambient_loop("ghost", "ghost_whisper.wav", 0.6)
    play_ambient_loop("drip", "drip_sound.wav", 0.6)

    #Room state change
    if visit_count == 0:  #Present
        type_text("\nThe basement is cold and smells of mildew.")
        type_text(f"The lightbulb {YELLOW}flickers{RESET}, weakly casting shadows.")

    elif visit_count == 1:  #Past
        type_text(f"\nShelves are neatly stocked, and a single bulb {YELLOW}glows{RESET} steadily.")
        type_text("Tools and old keepsakes sit in labeled boxes, undisturbed.")

    elif visit_count == 2:  #Future
        type_text("\nThe basement is cleared out. Only dust and cobwebs remain.")
        type_text(f"The air is filled with {DIM_WHITE}dust{RESET} and feels stale...")

    elif visit_count == 3:  #Eerie
        type_text("\nFootsteps echo, but you’re the only one down here...")
        type_text(f"Your {RED}heart{RESET} races as your mind wanders...")

    else:  #Altered Reality
        type_text(f"\nThe walls are {BLUE}wet{RESET}, pulsing like living flesh.")
        type_text("Your grasp on reality is slipping...")

    #Safe appears if not unlocked
    if not game_states.safe_unlocked:
        type_text(f"\nIn the center of the room stands an old, rusted {MAGENTA}safe{RESET}. What could be inside?")

#======================================================================

    #Basement art
    print(ascii_art["basement"])

#======================================================================
    #Basement choices
    while True:
        print("\nWhat do you want to do?")
        print("1. Look around")
        print("2. Wait around the basement")
        print("3. Go upstairs to the Kitchen")
        print("4. Check Inventory")

        #Show only correct safe response
        if not game_states.safe_unlocked:
            print(f"5. {YELLOW}Inspect the Safe{RESET}")  #Safe is locked
        else:
            print(f"5. {GREEN}Check out the open safe{RESET}")  #Safe is already unlocked

        choice = input("> ").strip()

        if choice == "1":
            look_around_basement()

        elif choice == "2":
            universal_wait()
            input(f"\nPress {GREEN}Enter{RESET} to continue.")

        elif choice == "3":
            game_states.room_visits[room_name] += 1
            play_sound_effect("stair_sound.wav")
            visit_room("room_6_kitchen")

        elif choice == "4":
            check_inventory(room_7_basement)

        elif choice == "5":
            if not game_states.safe_unlocked:
                inspect_safe()
            else:
                type_text(f"\n{YELLOW}The safe is already open. There is nothing else in here{RESET}.")

        elif choice == "debug":
            debug_menu()

        elif choice == "pause":
            pause_menu()

        else:
            print(f"\n{RED}Invalid choice. Try again.{RESET}")

#======================================================================
#Looking around the basement

def look_around_basement():
    while True:
        type_text("\nYou scan the basement. What do you want to check?")
        print("1. The Pipes")
        print("2. The Old Workbench")
        print("3. The Walls")
        print(f"4. {RED}Nevermind{RESET}")

        choice = input("> ").strip()

        if choice == "1":
            type_text("\nThe rusted pipes creak and groan as if the house itself were alive.")
            print(ascii_art["pipes"])

        elif choice == "2":
            type_text("\nThe workbench is covered in tools.")
            type_text("Most too rusted to be useful...")
            print(ascii_art["work_bench"])

        elif choice == "3":
            type_text("\nYour eyes trace the cracks in the walls.")
            type_text("One section looks different... like something was carved into it long ago.")
            type_text(f"You rub away some of the dust. A single number is etched on the surface...")
            print(f"{RED}{ascii_art['wall_etch']}{RESET}")

            if "Basement Safe Password Hint" not in game_states.inventory:
                game_states.inventory.append("Basement Safe Password Hint")
                type_text(f"{GREEN}This seems important... You take note of it{RESET}.")

            else:
                type_text(f"{YELLOW}You've already taken note of this{RESET}.")


        elif choice == "4":
            return  #Exit back to the basement menu

        elif choice == "debug":
            debug_menu()  #Calls the debug menu

        elif choice == "pause":
            pause_menu()

        else:
            print(f"\n{RED}Invalid choice. Try again{RESET}.")

#======================================================================