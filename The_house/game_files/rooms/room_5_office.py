#======================================================================
#Office Room: 5
#room_5_office.py
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
#Office room function

def room_5_office():
    #Room tracker
    room_name = "room_5_office"
    visit_count = game_states.room_visits.get(room_name, 0)

    #Room state changes
    if visit_count == 0:  #Present
        type_text("\nAn old desk sits against the far wall, covered in dust.")
        type_text("A single chair is pushed neatly into it.")

    elif visit_count == 1:  #Past
        type_text("\nA warm lamp glows on the desk. Papers are scattered almost as if mid-work.")
        type_text("A half-eaten meal sits beside an open notebook.")

    elif visit_count == 2:  #Future
        type_text("\nThe office has been nearly emptied... The desk is gone, the walls repainted. There are boxes everywhere...")
        type_text("Faint outlines of where pictures once hung are still visible.")

    elif visit_count == 3:  #Eerie
        type_text("\nThe curtains sway slightly, though there’s no breeze.")
        type_text("You feel as if someone is watching...")

    else:  #Altered Reality
        type_text("\nThe desk is massive, stretching infinitely far...")
        type_text("Papers fill the air, fluttering like trapped birds.")

#======================================================================

    #Office art
    print(ascii_art["office"])

#======================================================================
#Office choices
    while True:
        print("\nWhat do you want to do?")
        print("1. Look around")
        print("2. Wait in the office")
        print("3. Move north to the kitchen")
        print("4. Move east to the entryway")
        print("5. Check Inventory")

        choice = input("> ").strip()

        if choice == "1":
            look_around_office()

        elif choice == "2":
            universal_wait()
            input("\nPress Enter to continue.")

        elif choice == "3":
            type_text("\nYou walk towards the kitchen, the air growing colder as you move.")
            game_states.room_visits[room_name] += 1
            visit_room("room_6_kitchen")
            break

        elif choice == "4":
            type_text("\nYou step back into the entryway, the dim light flickering above.")
            game_states.room_visits[room_name] += 1
            visit_room("room_4_entryway")
            break

        elif choice == "5":
            check_inventory(room_5_office)

        elif choice == "debug":
            debug_menu()  #Calls the debug menu

        elif choice == "pause":
            pause_menu()

        else:
            print("\nInvalid choice. Try again.")

#======================================================================
#Look around office

def look_around_office():
    while True:
        type_text("\nYou scan the office. What do you want to examine?")
        print("1. The desk")
        print("2. The bookshelf")
        print("3. The filing cabinet")
        print("4. Nevermind")

        choice = input("> ").strip()

        if choice == "1":
            type_text("\nThe desk is neat, almost too neat...")
            type_text(f"The papers on top look shuffled but normal enough. Then it strikes you... {game_states.player_name}... as clear as day, scribbled on almost every sheet.")
            print(ascii_art["desk"])

        elif choice == "2":
            type_text("\nThe bookshelf is filled with old books, many of them worn and unreadable.")
            type_text("One title stands out: 'The House'.")
            print(ascii_art["books"])

        elif choice == "3":
            if "Fuse Order Hint" not in game_states.inventory:  #Prevent duplicates
                type_text("\nYou pull open a drawer in the filing cabinet. Most of the papers inside are faded or illegible.")
                type_text("One page, however, catches your eye: a maintenance log for the electrical system.")
                type_text("Scrawled in the margins, barely still readable: '**R → G → B**'.")
                type_text("This might be important later...")
                print(ascii_art["Fuse_Order_Hint"])
                game_states.inventory.append("Fuse Order Hint")
            else:
                type_text("\nYou've already noted down the important details from this drawer...")

        elif choice == "4":
            return  #Exit back to office menu

        elif choice == "debug":
            debug_menu()  #Calls the debug menu

        elif choice == "pause":
            pause_menu()

        else:
            print("\nInvalid choice. Try again.")

#======================================================================