#======================================================================
#Living Room: 8
#room_8_living_room.py
#======================================================================

# Internal imports
import game_states
from game_mechanics import visit_room, check_inventory, universal_wait
from text_effects import type_text
from ascii_art import ascii_art
from debug_mode import debug_menu

#======================================================================

#External imports
import random

#======================================================================
#Living Room function

def room_8_living_room():
    #Room tracker
    room_name = "room_8_living_room"
    visit_count = game_states.room_visits.get(room_name, 0)

    #Room state change
    if visit_count == 0:  #Present
        type_text("\nA dusty couch sits in the center of the room, untouched, wrapped in plastic.")
        type_text("The fireplace stands cold and empty.")

    elif visit_count == 1:  #Past
        type_text("\nA warm fire crackles, casting flickering light across the room.")
        type_text("A book rests open on the arm of the couch, its pages worn.")

    elif visit_count == 2:  #Future
        type_text("\nNew furniture sits where the old couch once was.")
        type_text("A modern TV is mounted on the wall, playing something you can’t quite hear.")

    elif visit_count == 3:  #Eerie
        type_text("\nThe couch is warm, as if someone was just sitting there.")
        type_text("The TV flickers on for a moment, playing static before shutting off.")

    else:  #Altered Reality
        type_text("\nThe room has changed drastically...")
        type_text("The couch and furniture have turned to stone... the walls are overgrown in moss...")

#======================================================================

    #Living room art
    print(ascii_art["living_room"])

#======================================================================
    #Living room choices
    while True:
        print("\nWhat do you want to do?")
        print("1. Look around")
        print("2. Go north to the Dining Room")
        print("3. Go west to the Entryway")
        print("4. Check Inventory")
        print("5. Wait around in the living room")

        choice = input("> ").strip()

        if choice == "1":
            look_around_living_room()

        elif choice == "2":
            game_states.room_visits[room_name] += 1
            visit_room("room_9_dining_room")

        elif choice == "3":
            game_states.room_visits[room_name] += 1
            visit_room("room_4_entryway")

        elif choice == "4":
            check_inventory(room_8_living_room)

        elif choice == "5":
            universal_wait()
            input("\nPress Enter to continue.")

        elif choice == "debug":
            debug_menu()  #Calls the debug menu

        else:
            print("\nInvalid choice. Try again.")

#======================================================================
#Looking Around Living Room

def look_around_living_room():
    while True:
        type_text("\nYou scan the living room. What do you want to check?")
        print("1. The Couch")
        print("2. The Clock")
        print("3. The TV Screen")
        print("4. Nevermind")

        choice = input("> ").strip()

        if choice == "1":
            type_text("\nThe couch is old and covered in dust. Something about it feels oddly familiar.")
            print(ascii_art["couch"])

        elif choice == "2":
            type_text("\nThe clock on the shelf flickers strangely, as if it's calling to you...")
            type_text("You see the time 3:00 flashing across its surface.")

            if "Living Room Safe Password Hint" not in game_states.inventory:
                game_states.inventory.append("Living Room Safe Password Hint")
                type_text("This feels important... You should take note of the time.")
            else:
                type_text("You've already taken note of this.")
            print(ascii_art["clock"])

        elif choice == "3":
            type_text("\nThe TV is off, but you swear you see something moving in its dark reflection.")
            print(ascii_art["tv"])

        elif choice == "4":
            return  #Exit back to the living room menu

        else:
            print("\nInvalid choice. Try again.")

#======================================================================