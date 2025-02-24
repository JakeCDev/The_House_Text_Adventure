#======================================================================
#Dining Room: 9
#room_9_dining_room.py
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
#Dining room function

def room_9_dining_room():
    #Room tracker
    room_name = "room_9_dining_room"
    visit_count = game_states.room_visits.get(room_name, 0)

    #Room state change
    if visit_count == 0:  #Present
        type_text("\nThe dining table is bare, the chairs neatly pushed in.")
        type_text("A chandelier hangs above.")

    elif visit_count == 1:  #Past
        type_text("\nThe table is set for dinner, plates arranged neatly.")
        type_text("You hear the faintest echo of laughter, distant and fading.")

    elif visit_count == 2:  #Future
        type_text("\nThe dining room has been remodeled. A new table, fresh paint.")
        type_text("It feels as if a family lives here now, though there’s no sign of them at the moment.")

    elif visit_count == 3:  #Eerie
        type_text("\nA single chair sits in the middle of the room...")
        type_text("The chandelier sways gently, though there’s no breeze...")

    else:  #Altered Reality
        type_text("\nThe table has snapped into pieces...")
        type_text("The floor is covered in silverware and shattered plates...")

#======================================================================

    #Dining room art
    print(ascii_art["dining_table"])

#======================================================================
    #Dining room choices
    while True:
        print("\nWhat do you want to do?")
        print("1. Look around")
        print("2. Go west to the Kitchen")
        print("3. Go south to the Living Room")
        print("4. Go upstairs to the Upstairs Hallway")
        print("5. Check Inventory")
        print("6. Wait around the dining room")

        choice = input("> ").strip()

        if choice == "1":
            look_around_dining_room()

        elif choice == "2":
            game_states.room_visits[room_name] += 1
            visit_room("room_6_kitchen")

        elif choice == "3":
            game_states.room_visits[room_name] += 1
            visit_room("room_8_living_room")

        elif choice == "4":
            game_states.room_visits[room_name] += 1
            visit_room("room_10_upstairs_hallway")

        elif choice == "5":
            check_inventory(room_9_dining_room)

        elif choice == "6":
            universal_wait()
            input("\nPress Enter to continue.")

        elif choice == "debug":
            debug_menu()  #Calls the debug menu

        else:
            print("\nInvalid choice. Try again.")

#======================================================================
#Looking around dining room

def look_around_dining_room():
    while True:
        type_text("\nYou scan the dining room. What do you want to check?")
        print("1. The Table")
        print("2. The Chairs")
        print("3. The lamp")
        print("4. Nevermind")

        choice = input("> ").strip()

        if choice == "1":
            type_text("\nYou run your fingers along the table’s surface. There’s a deep scratch, as if someone carved something here.")
            type_text("You look closer... A single number is scratched into the wood: 7.")

            if "Dining Room Safe Password Hint" not in game_states.inventory:
                game_states.inventory.append("Dining Room Safe Password Hint")
                type_text("This feels important... You should take note of this.")
            else:
                type_text("You've already taken note of this.")

            print(ascii_art["plates"])

        elif choice == "2":
            type_text("\nThe chairs are old and worn, as if they haven’t been used in years.")
            print(ascii_art["chair"])

        elif choice == "3":
            type_text("\nThe lamp flickers on and off, the chain doesn't seem to work either way.")
            print(ascii_art["lamp"])

        elif choice == "4":
            return  #Exit back to the dining room menu

        else:
            print("\nInvalid choice. Try again.")

#======================================================================