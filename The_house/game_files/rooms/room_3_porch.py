#======================================================================
#Porch Room: 3 - (Front of the House)
#room_3_porch.py
#======================================================================

#Internal imports
import game_states
from game_mechanics import visit_room, check_inventory, universal_wait
from text_effects import type_text, slow_dotted_text
from ascii_art import ascii_art
from debug_mode import debug_menu

#======================================================================

#External imports
import random
import time

#======================================================================
#Porch function room: 3

def room_3_porch():
    #Room tracker
    room_name = "room_3_porch"
    visit_count = game_states.room_visits.get(room_name, 0)

    #Room state change
    if visit_count == 0:  #Present
        type_text("\nYou step onto the porch. The wood creaks under your weight.")
        type_text("The front door stands closed before you. A dim light flickering inside.")

    elif visit_count == 1:  #Past
        type_text("\nThe air is thick here. The porch feels... different...")
        type_text("The door seems farther away than before...")

    elif visit_count == 2:  #Future
        type_text("\nThe porch is rotting. The wood blackened, wet. The house looks... abandoned.")

    elif visit_count == 3:  #Eerie
        type_text("\nA shadow moves across the porch... but when you look around, you are completely alone.")

    else:  #Altered Reality
        type_text("\nYou stand on the porch... the floor feels like deep sand as you trudge to the door...")
        type_text("The house seems to pulse and breathe, shifting in and out of focus...")

#======================================================================

    #Porch art
    print(ascii_art["porch"])

#======================================================================
    #Porch choices
    while True:
        print("\nWhat do you want to do?")

        if not game_states.door_open:  #Before the door opens/door still locked
            if not game_states.door_checked:
                print("1. Knock on the door")
        else:  #Once the door has mysteriously opened
            print("1. Enter the house")

        print("2. Look around")
        print("3. Wait on the porch")
        print("4. Check Inventory")

        choice = input("> ").strip()

        if choice == "1":
            if not game_states.door_open:
                locked_door_interaction()
            else:
                enter_house()

        elif choice == "2":
            look_around_porch()

        elif choice == "3":
            universal_wait()
            input("\nPress Enter to continue.")

        elif choice == "4":
            check_inventory(room_3_porch)

        elif choice == "debug":
            debug_menu()  #Calls the debug menu

        else:
            print("\nInvalid choice. Try again.")

#======================================================================
#Door lock function
def locked_door_interaction():
    if game_states.door_checked:  #If they already knocked/tried the handle, do nothing
        type_text("\nThe door stands slightly open now. You don't need to check the lock again.")
        return

    type_text("\nYou reach out and...", delay=0.03)
    time.sleep(1)
    print()
    print("*THUMP*")
    time.sleep(1)
    print()
    print("*THUMP*")
    time.sleep(1)
    print()
    print("*THUMP*")
    time.sleep(2)
    type_text("\nThere’s no response, Just silence...")
    time.sleep(2)
    type_text("\nYou grip the handle and turn. It won’t budge, locked tight")
    time.sleep(2)
    slow_dotted_text("\nThen suddenly")
    type_text("\nCREEEEEAAAAK...", delay=0.5)
    time.sleep(1)
    type_text("\nThe door slowly swings open on its own...")
    time.sleep(1)
    type_text("\nA gust of cold air rushes past you... The house is waiting...")

    game_states.door_open = True  #The door is now open
    game_states.door_checked = True  #The player has tried the door at least once

#======================================================================
#Enter house
def enter_house():
    type_text("\nYou take a moment to prepare yourself and then you cross the threshold...")
    time.sleep(2)
    print(ascii_art["slam"])
    time.sleep(1.5)
    type_text("\nThe door slams shut behind you.")
    time.sleep(1.5)

    game_states.room_visits["room_3_porch"] += 1  #Increment visit count
    visit_room("room_4_entryway")  #Move the player into the house

#======================================================================
#Look Around the porch
def look_around_porch():
    while True:
        type_text("\nYou scan the darkened porch. What do you want to examine?")
        print("1. The rocking chair")
        print("2. The windows")
        print("3. The doormat")
        print("4. The mailbox")
        print("5. Nevermind")

        choice = input("> ").strip()

        if choice == "1":
            type_text("\nA single rocking chair sits on the porch, swaying slightly.")
            type_text("Even when the wind isn’t blowing...")
            print(ascii_art["rocking_chair"])

        elif choice == "2":
            type_text("\nYou step closer to the window. The glass is cracked and dirty.")
            type_text("For a moment, your reflection seems strange. Like someone else is staring back at you.")
            print(ascii_art["window"])

        elif choice == "3":
            type_text("\nYou lift the doormat, half-expecting a key.")
            type_text("Nothing but dust and leaves.")
            print(ascii_art["welcome_mat"])

        elif choice == "4":  #Gain map of the house
            if "Map" not in game_states.inventory:
                type_text(
                    "\nAn old, weathered map of the house was crumpled up and shoved in the mailbox. This could be useful."
                )
                type_text("\n(The map has been added to your inventory.)")
                print(ascii_art["map"])
                game_states.inventory.append("Map")

            else:
                type_text("\nThe mailbox is empty now. You've already taken the map.")

        elif choice == "5":
            return  #Exit back to the porch menu

        elif choice == "debug":
            debug_menu()  #Calls the debug menu

        else:
            print("\nInvalid choice. Try again.")

#======================================================================