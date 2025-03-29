#======================================================================
#Porch Room: 3 - (Front of the House)
#room_3_porch.py
#======================================================================

#Imports
import game_states
from game_mechanics import visit_room, check_inventory, universal_wait
from text_effects import type_text, slow_dotted_text
from ascii_art import ascii_art
from debug_mode import debug_menu
from pause_menu import pause_menu
from color_scheme import YELLOW, GREEN, DIM_WHITE, RED, BLUE, CYAN, MAGENTA, RESET
import random
import time
from sound_manager import play_ambient_loop, stop_ambient_loop, set_ambient_volume, play_sound_effect

#======================================================================

#colorize for porch - def before the room to prevent circular imports / keep ascii dictionary clean
def colorized_porch():
    porch_art = ascii_art["porch"]
    colors = [BLUE, CYAN, DIM_WHITE]

    for char in porch_art:
        if char == "*":
            print(f"{random.choice(colors)}*{RESET}", end="")
        else:
            print(char, end="")


#======================================================================

#Porch function room: 3
def room_3_porch():
    #Room tracker
    room_name = "room_3_porch"
    visit_count = game_states.room_visits.get(room_name, 0)

    #music
    set_ambient_volume("rain", 0.4)
    set_ambient_volume("wind", 0.5)
    play_ambient_loop("porch", "spooky_loop.wav", volume=0.2)
    play_sound_effect("thunder_3.wav", volume=0.6)

    #Room state change
    if visit_count == 0:  #Present
        type_text("\nYou step onto the porch. The wood flexes under your weight.")
        type_text(f"The front door stands closed before you. A dim {YELLOW}light{RESET} flickering inside.")

    elif visit_count == 1:  #Past
        type_text(f"\nThe air is thick here. The porch feels... {DIM_WHITE}different...{RESET}")
        type_text("The door seems farther away than before...")

    elif visit_count == 2:  #Future
        type_text(f"\nThe porch is rotting. The wood blackened, {BLUE}wet{RESET}. The house looks... abandoned.")

    elif visit_count == 3:  #Eerie
        type_text(f"\nA shadow moves across the porch... but when you look around, you are completely {RED}alone{RESET}.")

    else:  #Altered Reality
        type_text("\nYou stand on the porch... the floor feels like deep sand as you trudge to the door...")
        type_text(f"{RED}The house{RESET} seems to pulse and breathe, shifting in and out of focus...")

#======================================================================

    #Porch art
    colorized_porch()

#======================================================================

    #Porch choices
    while True:
        print("\nWhat do you want to do?")
        print("1. Look around")
        print("2. Wait on the porch")

        if not game_states.door_open:  #Before the door opens/door still locked
            if not game_states.door_checked:
                print(f"3. {YELLOW}Knock on the door{RESET}")
        else:  #Once the door has mysteriously opened
            print(f"3. {GREEN}Enter the house{RESET}")

        print("4. Check Inventory")

        choice = input("> ").strip()

        if choice == "1":
            look_around_porch()

        elif choice == "2":
            universal_wait()
            input(f"\nPress {GREEN}Enter{RESET} to continue.")

        elif choice == "3":
            if not game_states.door_open:
                locked_door_interaction()
            else:
                enter_house()

        elif choice == "4":
            check_inventory(room_3_porch)

        elif choice == "debug":
            debug_menu()  #Calls the debug menu

        elif choice == "pause":
            pause_menu()

        else:
            print(f"\n{RED}Invalid choice. Try again{RESET}.")

#======================================================================

#Door lock function
def locked_door_interaction():
    if game_states.door_checked:  #If they already knocked/tried the handle, do nothing
        type_text(f"\nThe door stands slightly {GREEN}open{RESET} now. You don't need to check the lock again.")
        return

    type_text("\nYou reach out and...", delay=0.03)
    time.sleep(1.0)
    print()
    play_sound_effect("door_knock.wav", volume=1.0)
    print(f"{DIM_WHITE}*THUMP*{RESET}")
    time.sleep(1)
    print()
    play_sound_effect("door_knock.wav", volume=1.0)
    print(f"{DIM_WHITE}*THUMP*{RESET}")
    time.sleep(1)
    print()
    play_sound_effect("door_knock.wav", volume=1.0)
    print(f"{DIM_WHITE}*THUMP*{RESET}")
    time.sleep(2)
    type_text("\nThere’s no response, Just silence...")
    time.sleep(2)
    type_text("\nYou grip the handle and turn. It won’t budge, locked tight")
    time.sleep(2)
    type_text("\nThen suddenly...")
    play_sound_effect("door_creak.wav", volume=0.8)
    time.sleep(.5)
    type_text(f"\n{RED}CREEEEEAAAAK......{RESET}")
    time.sleep(1)
    type_text(f"\n{DIM_WHITE}The door slowly swings open on its own...{RESET}")
    time.sleep(1)
    type_text(f"\nA gust of cold air rushes past you... {RED}The house{RESET} is waiting...")

    game_states.door_open = True  #The door is now open
    game_states.door_checked = True  #The player has tried the door at least once

#======================================================================

#Enter house
def enter_house():
    type_text("\nYou take a moment to prepare yourself and then you cross the threshold...")
    play_sound_effect("door_slam.wav", volume=0.9)
    time.sleep(.25)
    print(RED + ascii_art["slam"] + RESET)
    time.sleep(1.5)
    type_text(f"\n{YELLOW}The door slams shut behind you{RESET}.")
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
        print(f"5. {RED}Nevermind{RESET}")

        choice = input("> ").strip()

        if choice == "1":
            type_text("\nA single rocking chair sits on the porch, swaying slightly.")
            type_text(f"{DIM_WHITE}Though the wind has stopped blowing completely...{RESET}")
            print(ascii_art["rocking_chair"])

        elif choice == "2":
            type_text("\nYou step closer to the window. The glass is cracked and dirty.")
            type_text(f"For a moment, your reflection seems {DIM_WHITE}strange{RESET}. Like someone else is staring back at you.")
            print(ascii_art["window"])

        elif choice == "3":
            type_text("\nYou lift the doormat, half-expecting a key.")
            type_text("Nothing but dust and leaves.")
            print(ascii_art["welcome_mat"])

        elif choice == "4":  #Gain map of the house
            if "Map" not in game_states.inventory:
                type_text(f"\nAn old, {MAGENTA}weathered map{RESET} of the house was crumpled up and shoved in the mailbox. {GREEN}This could be useful{RESET}.")
                type_text(f"\n{GREEN}(The map has been added to your inventory.){RESET}")
                print(ascii_art["map"])
                game_states.inventory.append("Map")

            else:
                type_text(f"\n{YELLOW}The mailbox is empty now. You've already taken the map{RESET}.")

        elif choice == "5":
            return  #Exit back to the porch menu

        elif choice == "debug":
            debug_menu()  #Calls the debug menu

        elif choice == "pause":
            pause_menu()

        else:
            print(f"\n{RED}Invalid choice. Try again{RESET}.")

#======================================================================

#End

#======================================================================