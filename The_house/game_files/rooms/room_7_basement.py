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


#======================================================================

#External imports
import random

#======================================================================
#Basement function

def room_7_basement():
    #Room tracker
    room_name = "room_7_basement"
    visit_count = game_states.room_visits.get(room_name, 0)

    #Room state change
    if visit_count == 0:  #Present
        type_text("\nThe basement is cold and smells of mildew.")
        type_text("The lightbulb flickers, weakly casting shadows.")

    elif visit_count == 1:  #Past
        type_text("\nShelves are neatly stocked, and a single bulb glows steadily.")
        type_text("Tools and old keepsakes sit in labeled boxes, undisturbed.")

    elif visit_count == 2:  #Future
        type_text("\nThe basement is cleared out. Only dust and cobwebs remain.")
        type_text("The air is filled with dust and feels stale...")

    elif visit_count == 3:  #Eerie
        type_text("\nFootsteps echo, but you’re the only one down here...")
        type_text("Your heart races as your mind wanders...")

    else:  #Altered Reality
        type_text("\nThe walls are wet, pulsing like living flesh.")
        type_text("Your grasp on reality is slipping...")

    #Safe appears if not unlocked
    if not game_states.safe_unlocked:
        type_text("\nIn the center of the room stands an old, rusted safe. What could be inside?")

#======================================================================

    #Basement art
    print(ascii_art["basement"])

#======================================================================
    #Basement choices
    while True:
        print("\nWhat do you want to do?")
        print("1. Look around")
        print("2. Go upstairs to the Kitchen")
        print("3. Check Inventory")
        print("4. Wait around the basement")

        #Show only correct safe response
        if not game_states.safe_unlocked:
            print("5. Inspect the Safe")  #Safe is locked
        else:
            print("5. Check out the open safe")  #Safe is already unlocked

        choice = input("> ").strip()

        if choice == "1":
            look_around_basement()

        elif choice == "2":
            game_states.room_visits[room_name] += 1
            visit_room("room_6_kitchen")

        elif choice == "3":
            check_inventory(room_7_basement)

        elif choice == "4":
            universal_wait()
            input("\nPress Enter to continue.")

        elif choice == "5":
            if not game_states.safe_unlocked:
                inspect_safe()  #Call safe function
            else:
                type_text("\nThe safe is already open. There is nothing else in here.")

        elif choice == "debug":
            debug_menu()  #Calls the debug menu

        elif choice == "pause":
            pause_menu()

        else:
            print("\nInvalid choice. Try again.")

#======================================================================
#Looking around the basement

def look_around_basement():
    while True:
        type_text("\nYou scan the basement. What do you want to check?")
        print("1. The Pipes")
        print("2. The Old Workbench")
        print("3. The Walls")
        print("4. Nevermind")

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
            type_text("You rub away some of the dust. A single number is etched into the surface... 6.")

            if "Basement Safe Password Hint" not in game_states.inventory:
                game_states.inventory.append("Basement Safe Password Hint")
                type_text("This seems important... You should probably remember it.")

            else:
                type_text("You've already taken note of this.")

            #Wall art
            print(ascii_art["brick"])

        elif choice == "4":
            return  #Exit back to the basement menu

        elif choice == "debug":
            debug_menu()  #Calls the debug menu

        elif choice == "pause":
            pause_menu()

        else:
            print("\nInvalid choice. Try again.")

#======================================================================