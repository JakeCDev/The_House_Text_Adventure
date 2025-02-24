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

#======================================================================

#External imports
import random

#======================================================================
#Attic function room: 13

def room_13_attic():
    #Room tracker
    room_name = "room_13_attic"
    visit_count = game_states.room_visits.get(room_name, 0)

    #Room state change
    if visit_count == 0:  #Present
        type_text("\nYou climb into the attic. Dust swirls in the dim light.")

    elif visit_count == 1:  #Past
        type_text("\nThe attic is strangely well-kept. Boxes are neatly stacked, as if someone still lives here.")

    elif visit_count == 2:  #Future
        type_text("\nEverything is covered in a thick layer of cobwebs. The light flickers, barely holding on.")

    elif visit_count == 3:  #Eerie
        type_text("\nYou hear shuffling, but see no one. Something was just here.")

    else:  #Altered reality
        type_text("\nThe attic is endless. A maze of shifting boxes, twisting shadows, and endless doors.")

#======================================================================

    #Attic art
    print(ascii_art["ladder"])

#======================================================================
    #Attic choices
    while True:
        print("\nWhat do you want to do?")
        print("1. Look around")
        print("2. Go downstairs to Bedroom A")
        print("3. Check Inventory")
        print("4. Wait around in the attic")

        choice = input("> ").strip()

        if choice == "1":
            look_around_attic()
        elif choice == "2":
            game_states.room_visits[room_name] += 1
            visit_room("room_12_bedroom_a")
        elif choice == "3":
            check_inventory(room_13_attic)
        elif choice == "4":
            universal_wait()
            input("\nPress Enter to continue.")
        elif choice == "debug":
            debug_menu()  #Calls the debug menu
        else:
            print("\nInvalid choice. Try again.")

#======================================================================
#Looking around the attic

def look_around_attic():
    #If the lockbox hasn't been picked up yet
    if "Locked Box" not in game_states.inventory:
        type_text("\nThe attic is filled with old boxes, furniture, and forgotten relics.")
        type_text("\nAmong them, one catches your eye... a small, rusted lockbox.")
        type_text("\nYou carefully pick it up. It's heavy, the lid fused shut with rust.")
        type_text("\nIf only you had a tool to pry it open...")
        type_text("\nYou recall seeing a screwdriver in the kitchen somewhere.")
        print(ascii_art["lockbox_closed"])
        game_states.inventory.append("Locked Box")  #Add to inventory

    else:
        type_text("\nThe attic remains silent. Dust swirls in the moonlight.")
        type_text("\nA tattered painting leans against the wall, its subject faded beyond recognition.")
        type_text("\nThe air feels heavier here... like a place long forgotten.")
        print(ascii_art["moon"])

    input("\nPress Enter to continue.")

#======================================================================
