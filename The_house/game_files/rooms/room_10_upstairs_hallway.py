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
from color_scheme import YELLOW, MAGENTA, BRIGHT_CYAN, BRIGHT_MAGENTA, BLUE, BRIGHT_BLUE, CYAN, RED, GREEN, BRIGHT_WHITE, RESET

#======================================================================

#External imports
import random

#======================================================================

#colorize for red fuse def before the room to prevent circular imports / keep ascii dictionary clean

def colorize_green_fuse():
    fuse_art = ascii_art["green_fuse"]

    for line in fuse_art.splitlines():
        if "GREEN" in line:
            line = line.replace("GREEN", f"{GREEN}GREEN{RESET}")
        print(line)

#======================================================================

#colorize flowers in the vase - def before the room to prevent circular imports / keep ascii dictionary clean
def colorize_vase():
    vase_art = ascii_art["vase"]
    colors = [MAGENTA, CYAN, BRIGHT_CYAN, BRIGHT_MAGENTA, BLUE, BRIGHT_BLUE]

    for char in vase_art:
        if char == "@":
            print(f"{random.choice(colors)}@{RESET}", end="")
        else:
            print(char, end="")
#======================================================================

#Upstairs hallway function

def room_10_upstairs_hallway():
    #Room tracker
    room_name = "room_10_upstairs_hallway"
    visit_count = game_states.room_visits.get(room_name, 0)

    #Room state changes
    if visit_count == 0:  #Present
        type_text("\nThe hallway is long and empty, the floor creaking beneath your steps.")
        type_text(f"A soft {YELLOW}light{RESET} fills the hallway.")

    elif visit_count == 1:  #Past
        type_text(f"\nThe hallway is warm and well {YELLOW}lit{RESET}. A coat hangs on the banister.")
        type_text("Family photos line the walls, but their faces seem blurred.")

    elif visit_count == 2:  #Future
        type_text("\nThe walls are a new print of wallpaper, the doors replaced.")
        type_text(f"The hallway has the scent of fresh {GREEN}pine{RESET}.")

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
        print("2. Wait around the upstairs hallway")
        print("3. Go west to Bedroom A")
        print("4. Go east to Bedroom B")
        print("5. Go downstairs to the Dining Room")
        print("6. Check Inventory")

        choice = input("> ").strip()

        if choice == "1":
            look_around_upstairs_hallway()

        elif choice == "2":
            universal_wait()
            input(f"\nPress {GREEN}Enter{RESET} to continue.")

        #Bedroom A west – requires Skeleton Key
        elif choice == "3":
            if "Skeleton Key" in game_states.inventory:
                game_states.room_visits[room_name] += 1
                visit_room("room_12_bedroom_a")
            else:
                type_text(f"\nThe door to Bedroom A is {RED}locked{RESET}. You need a {MAGENTA}key{RESET}.")

        #Bedroom B east – requires power restored
        elif choice == "4":
            if game_states.power_restored:
                game_states.room_visits[room_name] += 1
                visit_room("room_11_bedroom_b")
            else:
                type_text(f"\nIt's too dark inside Bedroom B. You can't see anything... You must restore the {RED}power{RESET} first.")

        elif choice == "5":
            game_states.room_visits[room_name] += 1
            visit_room("room_9_dining_room")

        elif choice == "6":
            check_inventory(room_10_upstairs_hallway)

        elif choice == "debug":
            debug_menu()  #Call the debug menu

        elif choice == "pause":
            pause_menu()

        else:
            print(f"\n{RED}Invalid choice. Try again.{RESET}")

#======================================================================
#Looking around the upstairs hallway

def look_around_upstairs_hallway():
    while True:
        type_text("\nYou scan the upstairs hallway. What do you want to check?")
        print("1. The Portraits")
        print("2. The Dresser")
        print("3. Vase of flowers")
        print(f"4. {RED}Nevermind{RESET}")

        choice = input("> ").strip()

        if choice == "1":
            type_text("\nThe portraits on the wall are faded. The eyes seem to follow you.")
            print(ascii_art["picture_frame"])

        elif choice == "2":
            if "Green Fuse" not in game_states.inventory and "Green Fuse" not in game_states.fuse_box:
                type_text("\nInside the dresser, you find a small Green Fuse.")
                colorize_green_fuse()
                game_states.inventory.append("Green Fuse")  #Green fuse
                type_text(f"{GREEN}This could be useful... you decide to take it just in case{RESET}.")
            else:
                type_text(f"\n{YELLOW}The dresser is empty now{RESET}.")

        elif choice == "3":
            type_text("\nThese flowers seem fresh...")
            colorize_vase()

        elif choice == "4":
            return  #Exit back to the hallway menu

        elif choice == "debug":
            debug_menu()  #Calls the debug menu

        elif choice == "pause":
            pause_menu()

        else:
            print(f"\n{RED}Invalid choice. Try again{RESET}.")

#======================================================================