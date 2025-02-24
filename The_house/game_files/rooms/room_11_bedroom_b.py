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

#======================================================================

#External imports
import random

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
        type_text("\nThe bed is messy, covered in laundry. As if someone just got up or was mid-cleaning.")
        type_text("A book rests on the nightstand, a glass of water beside it.")

    elif visit_count == 2:  #Future
        type_text("\nThe room is lined with boxes... it's hard to tell if someone is coming or going...")
        type_text("Faint marks on the floor show where old furniture once sat.")

    elif visit_count == 3:  #Eerie
        type_text("\nYou feel a breath on your neck...")
        type_text("You turn and no one is there.")

    else:  #Altered Reality
        type_text("\nThe bed hovers feet above the ground...")
        type_text("The mirror ripples like water, reflecting a room that isn’t the same.")

#======================================================================

    #Bedroom B art
    print(ascii_art["bedroom_b"])

#======================================================================
    #Bedroom B choices
    while True:
        print("\nWhat do you want to do?")
        print("1. Look around")
        print("2. Go west to the Upstairs Hallway")
        print("3. Check Inventory")
        print("4. Wait around in Bedroom B")

        choice = input("> ").strip()

        if choice == "1":
            look_around_bedroom_b()

        elif choice == "2":
            game_states.room_visits[room_name] += 1
            visit_room("room_10_upstairs_hallway")

        elif choice == "3":
            check_inventory(room_11_bedroom_b)

        elif choice == "4":
            universal_wait()
            input("\nPress Enter to continue.")

        elif choice == "debug":
            debug_menu()  #Calls the debug menu

        else:
            print("\nInvalid choice. Try again.")

#======================================================================
#Looking around in Bedroom B

def look_around_bedroom_b():
    while True:
        type_text("\nYou scan the bedroom. What do you want to check?")
        print("1. The Bed")
        print("2. The Closet")
        print("3. The Desk")
        print("4. Nevermind")

        choice = input("> ").strip()

        if choice == "1":
            type_text("\nThe sheets are still slightly ruffled... but it seems no one has lived here in a long time.")
            print(ascii_art["bed_b"])

        elif choice == "2":
            type_text("\nThe closet door is slightly open. A musty smell drifts out, but there's nothing inside except old clothes.")
            print(ascii_art["bedroom_b_closet"])

        elif choice == "3":
            if "Safe Order Hint" not in game_states.inventory:
                type_text("\nOn the desk, an old note sits under a layer of dust. It reads:")
                type_text("\n_\"Down below, where there is no sight,_")
                type_text("\n_At the table, in flickering light,_")
                type_text("\n_Where the clock forgets what’s wrong from right.\"_")
                type_text("\nSomething about this feels important... You commit it to memory.")
                print(ascii_art["bedroom_b_desk"])
                game_states.inventory.append("Safe Order Hint")
            else:
                type_text("\nThe desk is empty now, the note we took was the only thing of interest here it seems.")

        elif choice == "4":
            return  #Exit back to the bedroom menu

        else:
            print("\nInvalid choice. Try again.")

#======================================================================