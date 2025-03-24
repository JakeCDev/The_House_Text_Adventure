#======================================================================
#Attic Room: 13
#room_13_attic.py
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

#======================================================================

#def colorize before the room to prevent circular imports / keep ascii dictionary clean
def colorized_moon():
    moon_art = ascii_art["moon"]
    yellow_chars = set("_',.`:()")

    for char in moon_art:
        if char in yellow_chars:
            print(f"{YELLOW}{char}{RESET}", end="")
        else:
            print(char, end="")

#======================================================================
#Attic function room: 13

def room_13_attic():
    #Room tracker
    room_name = "room_13_attic"
    visit_count = game_states.room_visits.get(room_name, 0)

    #music
    stop_ambient_loop("house", fade_out=1000)
    play_ambient_loop("ominous", "ominous_loop.wav", 0.6)

    #Room state change
    if visit_count == 0:  #Present
        type_text(f"\nYou climb into the attic. Dust swirls in the dim {YELLOW}light{RESET}.")

    elif visit_count == 1:  #Past
        type_text("\nThe attic is strangely well kept. Boxes neatly stacked and no clutter in sight.")

    elif visit_count == 2:  #Future
        type_text(f"\nEverything is covered in a thick layer of cobwebs. The light {YELLOW}flickers{RESET}, seems like it is barely holding on.")

    elif visit_count == 3:  #Eerie
        type_text(f"\nYou hear {RED}shuffling{RESET}, but see no one.")

    else:  #Altered reality
        type_text("\nThe attic seems endless. A maze of shifting boxes, twisting shadows, and endless passage ways.")

#======================================================================

    #Attic art
    print(ascii_art["ladder"])

#======================================================================
    #Attic choices
    while True:
        print("\nWhat do you want to do?")
        print("1. Look around")
        print("2. Wait around in the attic")
        print("3. Go downstairs to Bedroom A")
        print("4. Check Inventory")

        choice = input("> ").strip()

        if choice == "1":
            look_around_attic()

        elif choice == "2":
            universal_wait()
            input(f"\nPress {GREEN}Enter{RESET} to continue.")

        elif choice == "3":
            game_states.room_visits[room_name] += 1
            visit_room("room_12_bedroom_a")

        elif choice == "4":
            check_inventory(room_13_attic)

        elif choice == "debug":
            debug_menu()  # Calls the debug menu

        elif choice == "pause":
            pause_menu()

        else:
            print(f"\n{RED}Invalid choice. Try again.{RESET}")

#======================================================================
#Looking around the attic

def look_around_attic():
    #If the lockbox hasn't been picked up yet
    if "Locked Box" not in game_states.inventory:
        play_sound_effect("thunder_3.wav", volume=0.6)
        type_text("\nThe attic is filled with old boxes, furniture, and forgotten relics.")
        type_text(f"\nAmong them, one catches your eye... a small, {MAGENTA}rusted lockbox{RESET}.")
        type_text("\nYou carefully pick it up. It's heavy, the lid fused shut with rust.")
        type_text(f"\n{YELLOW}If only you had a tool to pry it open...{RESET}")
        type_text(f"\nYou recall seeing a screwdriver in the {GREEN}kitchen{RESET} somewhere.")
        print(ascii_art["lockbox_closed"])
        game_states.inventory.append("Locked Box")  #Add to inventory

    else:
        type_text("\nThe attic remains silent. Dust swirls in the moonlight.")
        type_text("\nA tattered painting leans against the wall, its subject faded beyond recognition.")
        type_text("\nThe air feels dense here... this place feels long forgotten.")
        colorized_moon()

    input(f"\nPress {GREEN}Enter{RESET} to continue.")

#======================================================================
