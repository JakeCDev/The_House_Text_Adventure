#======================================================================
#Road room: 2
#rooms/room_2_road.py
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
#Road function room: 2
def room_2_road():
    #Room tracker
    room_name = "room_2_road"
    visit_count = game_states.room_visits.get(room_name, 0)

    #Room states
    if visit_count == 0:  #Present
        type_text("\nThe road stretches ahead, wet with rain and lined with trees.")
        type_text("The house looms in the distance, barely visible in the storm.")

    elif visit_count == 1:  #Past
        type_text("\nThe road feels different. The storm nearly gone, replaced by the golden glow of the sunset and streetlights.")
        type_text("You hear the distant sound of laughter—like a memory just out of reach.")

    elif visit_count == 2:  #Future
        type_text("\nThe road is cracked and overgrown. Covered in tire tracks and debris...")
        type_text("It feels like no one has walked this path in years...")

    elif visit_count == 3:  #Eerie
        type_text("\nThe trees seem taller than before, their branches stretching toward you.")
        type_text("The wind carries a whisper, though you can't quite make out the words...")

    else:  #Altered Reality
        type_text("\nThe road now bends and twists like a river, flowing beneath your feet...")
        type_text("The trees have become surreal, their trunks twist in all directions, their leaves glisten like glass...")

#======================================================================
    #Road art
    print(ascii_art["road"])

#======================================================================
    #Road choices
    while True:
        print("\nWhat do you want to do?")
        print("1. Look around")
        print("2. Wait on the road")
        print("3. Move north towards the house")
        print("4. Check Inventory")

        choice = input("> ").strip()

        if choice == "1":
            look_around_road()

        elif choice == "2":
            universal_wait()
            input("\nPress Enter to continue.")

        elif choice == "3":  #Move to porch
            type_text("\nYou move toward the house...")
            game_states.room_visits[room_name] += 1
            visit_room("room_3_porch")
            break

        elif choice == "4":
            check_inventory(room_2_road)

        elif choice == "debug":
            debug_menu()  #Calls the debug menu

        else:
            print("\nInvalid choice. Try again.")

#======================================================================
#Look around road
def look_around_road():
    while True:
        type_text("\nYou glance around the empty road. What would you like to check?")
        print("1. The trees")
        print("2. The signpost")
        print("3. The sky")
        print("4. Nevermind")

        choice = input("> ").strip()

        if choice == "1":
            type_text("\nThe trees are tall and twisted. Their branches reaching upward.")
            type_text("You have the distinct feeling that... something is watching you.")
            print(ascii_art["tree"])

        elif choice == "2":
            type_text("\nYou step closer to the signpost. Unfortunately, the letters are too faded to read, perhaps it's for a nearby town.")
            type_text("For a moment, the words look... wrong. Almost foreign.")
            print(ascii_art["signpost"])

        elif choice == "3":
            type_text("\nThe dark night sky is littered with stars. The occasional lightning flash breaks the darkness.")
            print(ascii_art["sky"])

        elif choice == "4":
            return  #Exit back to the road menu

        else:
            print("\nInvalid choice. Try again.")