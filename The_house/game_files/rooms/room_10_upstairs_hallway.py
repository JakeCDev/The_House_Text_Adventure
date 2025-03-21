#======================================================================
#Upstairs Hallway: 10
#room_10_upstairs_hallway.py
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
#Upstairs hallway function

def room_10_upstairs_hallway():
    #Room tracker
    room_name = "room_10_upstairs_hallway"
    visit_count = game_states.room_visits.get(room_name, 0)

    #Room state changes
    if visit_count == 0:  #Present
        type_text("\nThe hallway is long and empty, the floor creaking beneath your steps.")
        type_text("A soft light fills the hallway.")

    elif visit_count == 1:  #Past
        type_text("\nThe hallway is warm and well-lit. A coat hangs on the banister.")
        type_text("Family photos line the walls, but their faces seem blurred.")

    elif visit_count == 2:  #Future
        type_text("\nThe walls are repainted, the doors replaced.")
        type_text("The hallway has the scent of fresh pine.")

    elif visit_count == 3:  #Eerie
        type_text("\nThe hallway seems much longer than before.")
        type_text("A door at the end wasn’t there last time you looked... it opens to a brick wall.")

    else:  #Altered Reality
        type_text("\nThe hallway shrinks and the walls narrow as you progress down it.")
        type_text("You are barely able to squeeze through to the other end.")

#======================================================================

    #Hallway stair art
    print(ascii_art["stairs"])

#======================================================================
    #Upstairs hallway choices
    while True:
        print("\nWhat do you want to do?")
        print("1. Look around")
        print("2. Go west to Bedroom A")
        print("3. Go east to Bedroom B")
        print("4. Go downstairs to the Dining Room")
        print("5. Check Inventory")
        print("6. Wait around the upstairs hallway")

        choice = input("> ").strip()

        if choice == "1":
            look_around_upstairs_hallway()

        #Safe key required lock
        elif choice == "2":
            if "Skeleton Key" in game_states.inventory:
                game_states.room_visits[room_name] += 1
                visit_room("room_12_bedroom_a")
            else:
                type_text("\nThe door to Bedroom A is locked. You need a key.")

        #Power restored lock
        elif choice == "3":
            if game_states.power_restored:
                game_states.room_visits[room_name] += 1
                visit_room("room_11_bedroom_b")
            else:
                type_text("\nIt's too dark inside Bedroom B. You can't see anything... You must restore the power first.")

        elif choice == "4":
            game_states.room_visits[room_name] += 1
            visit_room("room_9_dining_room")

        elif choice == "5":
            check_inventory(room_10_upstairs_hallway)

        elif choice == "6":
            universal_wait()
            input("\nPress Enter to continue.")

        elif choice == "debug":
            debug_menu()  #Call the debug menu

        elif choice == "pause":
            pause_menu()

        else:
            print("\nInvalid choice. Try again.")

#======================================================================
#Looking around the upstairs hallway

def look_around_upstairs_hallway():
    while True:
        type_text("\nYou scan the upstairs hallway. What do you want to check?")
        print("1. The Portraits")
        print("2. The Dresser")
        print("3. Vase of flowers")
        print("4. Nevermind")

        choice = input("> ").strip()

        if choice == "1":
            type_text("\nThe portraits on the wall are faded. The eyes seem to follow you.")
            print(ascii_art["picture_frame"])

        elif choice == "2":
            if "Green Fuse" not in game_states.inventory and "Green Fuse" not in game_states.fuse_box:
                type_text("\nInside the dresser, you find a small Green Fuse.")
                print(ascii_art["green_fuse"])
                game_states.inventory.append("Green Fuse")  #Green fuse
                type_text("This could be useful... you decide to take it just in case.")
            else:
                type_text("\nThe dresser is empty now.")

        elif choice == "3":
            type_text("\nThese flowers seem fresh...")
            print(ascii_art["vase"])

        elif choice == "4":
            return  #Exit back to the hallway menu

        elif choice == "debug":
            debug_menu()  #Calls the debug menu

        elif choice == "pause":
            pause_menu()

        else:
            print("\nInvalid choice. Try again.")

#======================================================================