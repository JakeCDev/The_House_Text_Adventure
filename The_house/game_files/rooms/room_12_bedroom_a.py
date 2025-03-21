#======================================================================
#Bedroom A: Room 12
#room_12_bedroom_a.py
#======================================================================

#Internal imports
import game_states
from game_mechanics import visit_room, check_inventory, universal_wait
from text_effects import type_text
from ascii_art import ascii_art
from debug_mode import debug_menu
from pause_menu import pause_menu


#======================================================================

#External imports
import random

#======================================================================
#Bedroom A function

def room_12_bedroom_a():
    #Room tracker
    room_name = "room_12_bedroom_a"
    visit_count = game_states.room_visits.get(room_name, 0)

    #Room state changes
    if visit_count == 0:  #Present
        type_text("\nThe bedroom is neat, yet untouched.")
        type_text("The curtains are drawn, and a faint breeze stirs the dust.")

    elif visit_count == 1:  #Past
        type_text("\nSunlight filters through the window.")
        type_text("The bed is unmade, and the faint scent of perfume lingers.")

    elif visit_count == 2:  #Future
        type_text("\nThe bedroom has been repainted, but it still feels empty.")
        type_text("Only a few belongings remain scattered on the shelves.")

    elif visit_count == 3:  #Eerie
        type_text("\nYou hear faint whispers... but no one is here.")
        type_text("The shadows stretch too far across the walls.")

    else:  #Altered Reality
        type_text("\nThe room has no walls—only an endless expanse of doors leading to nowhere.")
        type_text("The bed floats in midair, suspended by invisible forces.")

#======================================================================

    #Bedroom A art
    print(ascii_art["bedroom_a"])

#======================================================================
    #Bedroom A choices
    while True:
        print("\nWhat do you want to do?")
        print("1. Look around")
        print("2. Go east to the Upstairs Hallway")
        print("3. Take the ladder up to the Attic")
        print("4. Check Inventory")
        print("5. Wait around in Bedroom A")

        choice = input("> ").strip()

        if choice == "1":
            look_around_bedroom_a()

        elif choice == "2":
            game_states.room_visits[room_name] += 1
            visit_room("room_10_upstairs_hallway")

        elif choice == "3":
            game_states.room_visits[room_name] += 1
            visit_room("room_13_attic")

        elif choice == "4":
            check_inventory(room_12_bedroom_a)

        elif choice == "5":
            universal_wait()
            input("\nPress Enter to continue.")

        elif choice == "debug":
            debug_menu()  #Calls the debug menu

        elif choice == "pause":
            pause_menu()

        else:
            print("\nInvalid choice. Try again.")

#======================================================================
#Looking around in Bedroom A

def look_around_bedroom_a():
    while True:
        type_text("\nYou scan the bedroom. What do you want to check?")
        print("1. The Mirror")
        print("2. The Bookshelf")
        print("3. The Nightstand")
        print("4. Nevermind")

        choice = input("> ").strip()

        if choice == "1":
            type_text("\nThe mirror is covered in dust. You can barely make out your reflection...")
            type_text("For a brief second, you thought you saw someone standing behind you.")
            print(ascii_art["bedroom_a_mirror"])

        elif choice == "2":
            type_text("\nAn old journal sits on the shelf. The pages are torn and scattered.")
            type_text("One page remains readable: 'It's all hidden in the attic.'")

            if "Attic Hint" not in game_states.inventory:  #Prevents duplicate entries
                type_text("This feels important... you should take note of this.")
                print(ascii_art["bookshelf"])
                game_states.inventory.append("Attic Hint")
            else:
                type_text("You've already taken notes of this.")

        elif choice == "3":
            type_text("\nThe nightstand is covered in dust. A small jewelry box sits on top.")
            print(ascii_art["nightstand"])

        elif choice == "4":
            return  #Exit back to the Bedroom A menu

        elif choice == "debug":
            debug_menu()  #Calls the debug menu

        elif choice == "pause":
            pause_menu()

        else:
            print("\nInvalid choice. Try again.")

#======================================================================
