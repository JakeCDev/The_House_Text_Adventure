#======================================================================
#Kitchen Room: 6
#room_6_kitchen.py
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
#Kitchen function

def room_6_kitchen():
    # Room tracker
    room_name = "room_6_kitchen"
    visit_count = game_states.room_visits.get(room_name, 0)

    if visit_count == 0:  #Present
        type_text("\nThe kitchen is eerily quiet. A thin layer of dust coats the countertops.")
        type_text("The refrigerator hums softly, but there's no food inside.")

    elif visit_count == 1:  #Past
        type_text("\nThe scent of something delicious lingers in the air.")
        type_text("Plates sit drying on a dish rack, a half-eaten meal half wrapped to be put away rests on the counter.")

    elif visit_count == 2:  #Future
        type_text("\nThe cabinets have been replaced, the floors redone.")
        type_text("A child's drawing is pinned to the fridge.")

    elif visit_count == 3:  #Eerie
        type_text("\nYou hear the sound of a knife chopping but the kitchen is vacant.")
        type_text("The air carries a metallic scent, sharp and unsettling.")

    else:  #Altered Reality
        type_text("\nA huge hole now fills the center of the room where there was once a table... it looks deep... you can't see a bottom...")
        type_text("The refrigerator light blares into the room as if it were a lighthouse...")

    #Show final door if the lockbox has been opened
    if "Lockbox Opened" in game_states.inventory and not game_states.final_door_appeared:
        type_text("\nA door you swear wasn’t there before now stands along the north wall in front of you.")
        type_text("A warm, soft light glows from beyond it, beckoning you forward. It feels... warm... familiar somehow...")
        game_states.final_door_appeared = True

#======================================================================

    #Kitchen art
    print(ascii_art["kitchen"])

#======================================================================
    #Kitchen choices
    while True:
        print("\nWhat do you want to do?")
        print("1. Look around")
        print("2. Go south to the Office")
        print("3. Go east to the Dining Room")
        print("4. Go downstairs to the Basement")

        if "Lockbox Opened" in game_states.inventory:
            print("5. Step through the mysterious door")

        print("6. Check Inventory")
        print("7. Wait in the kitchen")

        choice = input("> ").strip()

        if choice == "1":
            look_around_kitchen()

        elif choice == "2":
            game_states.room_visits[room_name] += 1
            visit_room("room_5_office")

        elif choice == "3":
            game_states.room_visits[room_name] += 1
            visit_room("room_9_dining_room")

        elif choice == "4":  #Block basement until power is restored
            if game_states.power_restored:
                type_text("\nThe basement is now dimly lit. You cautiously step down the stairs.")
                game_states.room_visits[room_name] += 1
                visit_room("room_7_basement")
            else:
                type_text("\nYou try to step into the basement, but it's pitch black.")
                type_text("You can't see anything down there. Once power is restored, you can come back.")
                input("\nPress enter to return to the kitchen.")

        elif choice == "5" and "Lockbox Opened" in game_states.inventory:
            game_states.inventory.append("Entered Final Room")  #Marks the point of no return
            game_states.room_visits[room_name] += 1
            visit_room("room_14_final_room")  #Move to the final sequence
            break

        elif choice == "6":
            check_inventory(room_6_kitchen)

        elif choice == "7":
            universal_wait()
            input("\nPress Enter to continue.")

        elif choice == "debug":
            debug_menu()  #Calls the debug menu

        else:
            print("\nInvalid choice. Try again.")

#======================================================================
#Looking around the kitchen

def look_around_kitchen():
    while True:
        type_text("\nYou scan the kitchen. What do you want to check?")
        print("1. The Counter")
        print("2. The Fridge")
        print("3. The Drawer")
        print("4. Nevermind")

        choice = input("> ").strip()

        if choice == "1":  #Blue Fuse
            if "Blue Fuse" not in game_states.inventory and "Blue Fuse" not in game_states.fuse_box:
                type_text("\nThe counter is covered in dust. A single Blue Fuse rests here.")
                print(ascii_art["blue_fuse"])
                game_states.inventory.append("Blue Fuse")
                type_text("This could be useful... You take the fuse for now")
            else:
                type_text("\nThe counter is empty now.")

        elif choice == "2":
            type_text("\nThe fridge hums softly, inside the shelves are nearly bare.")
            type_text("Just rotting food and a bad smell... you wonder when was the last time someone lived here.")
            print(ascii_art["fridge"])

        elif choice == "3":  #Drawer/Screwdriver
            if game_states.power_restored:  #Only accessible after restoring power
                if "Screwdriver" not in game_states.inventory:
                    type_text("\nYou open the drawer and find a rusty screwdriver.")
                    type_text("\nThis might be useful for prying something open... but what?")
                    print(ascii_art["screwdriver"])
                    game_states.inventory.append("Screwdriver")
                else:
                    type_text("\nThe drawer is empty now.")
            else:
                type_text("\nIt's too dark to see inside the drawer. You'll need to check back later.")

        elif choice == "4":
            return  #Exit back to the kitchen menu

        else:
            print("\nInvalid choice. Try again.")
#======================================================================