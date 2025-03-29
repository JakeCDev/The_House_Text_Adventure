#======================================================================
#Kitchen Room: 6
#room_6_kitchen.py
#======================================================================

#Imports
import game_states
from game_mechanics import visit_room, check_inventory, universal_wait
from text_effects import type_text
from ascii_art import ascii_art
from debug_mode import debug_menu
from pause_menu import pause_menu
from color_scheme import YELLOW, MAGENTA, BLUE, CYAN, RED, GREEN, DIM_WHITE, RESET
from sound_manager import play_ambient_loop, stop_ambient_loop, play_sound_effect
import random

#======================================================================

def colorize_blue_fuse():
    fuse_art = ascii_art["blue_fuse"]

    for line in fuse_art.splitlines():
        if "BLUE" in line:
            line = line.replace("BLUE", f"{BLUE}BLUE{RESET}")
        print(line)

#======================================================================

#Kitchen function
def room_6_kitchen():

    # Room tracker
    room_name = "room_6_kitchen"
    visit_count = game_states.room_visits.get(room_name, 0)

    #music
    stop_ambient_loop("ghost", fade_out=1000)
    stop_ambient_loop("drip", fade_out=1000)
    play_ambient_loop("house", "house_loop.wav", 0.6)

    if visit_count == 0:  #Present
        type_text("\nThe kitchen is eerily quiet. A thin layer of dust coats the countertops.")
        type_text(f"The refrigerator has an eerie {YELLOW}glow{RESET} as it hums softly, doubtful there's fresh food inside.")

    elif visit_count == 1:  #Past
        type_text("\nThe scent of something delicious lingers in the air.")
        type_text(f"Plates sit drying on a dish rack still {BLUE}wet{RESET}, a half-eaten meal half wrapped to be put away rests on the counter.")

    elif visit_count == 2:  #Future
        type_text(f"\nThe cabinets have been replaced, the floors redone. A vase with fresh {YELLOW}sunflowers{RESET} now sits on the counter.")
        type_text("A child's drawing is pinned to the fridge.")

    elif visit_count == 3:  #Eerie
        type_text("\nYou thought you heard the sound of a knife chopping but the kitchen is vacant.")
        type_text(f"The air carries a {DIM_WHITE}metallic{RESET} scent and taste, sharp and unsettling.")

    else:  #Altered Reality
        type_text("\nA huge hole now fills the center of the room where there was once a table... it looks deep... with no bottom in sight...")
        type_text(f"The refrigerator {YELLOW}light{RESET} blares into the room like a lighthouse...")

    #Show final door if the lockbox has been opened
    if "Lockbox Opened" in game_states.inventory and not game_states.final_door_appeared:
        type_text(f"\nA {GREEN}door{RESET} you swear wasn’t there before now stands along the north wall in front of you.")
        type_text(f"A warm, soft {YELLOW}light{RESET} glows from beyond it, beckoning you forward. It feels... warm... familiar somehow...")
        game_states.final_door_appeared = True

#======================================================================

    #Kitchen art
    print(ascii_art["kitchen"])

#======================================================================

    #Kitchen choices
    while True:
        print("\nWhat do you want to do?")
        print("1. Look around")
        print("2. Wait in the kitchen")
        print("3. Go south to the Office")
        print("4. Go east to the Dining Room")
        print("5. Go downstairs to the Basement")
        print("6. Check Inventory")

        if "Lockbox Opened" in game_states.inventory:
            print(f"7. {GREEN}Step through the mysterious new door{RESET}")

        choice = input("> ").strip()

        if choice == "1":
            look_around_kitchen()

        elif choice == "2":
            universal_wait()
            input(f"\nPress {GREEN}Enter{RESET} to continue.")

        elif choice == "3":
            game_states.room_visits[room_name] += 1
            visit_room("room_5_office")

        elif choice == "4":
            game_states.room_visits[room_name] += 1
            visit_room("room_9_dining_room")

        elif choice == "5":  #Block basement until power is restored
            if game_states.power_restored:
                type_text(f"\nThe basement is now dimly {YELLOW}lit{RESET}. You cautiously step down the stairs.")
                play_sound_effect("stair_sound.wav")
                game_states.room_visits[room_name] += 1
                visit_room("room_7_basement")
            else:
                type_text("\nYou try to step into the basement, but it's pitch black.")
                type_text(f"You can't see anything down there. Once power is {RED}restored{RESET}, you can come back.")
                input(f"\nPress {GREEN}Enter{RESET} to return to the kitchen.")

        elif choice == "6":
            check_inventory(room_6_kitchen)

        elif choice == "7" and "Lockbox Opened" in game_states.inventory:
            game_states.inventory.append("Entered Final Room")  #Marks the point of no return
            game_states.room_visits[room_name] += 1
            visit_room("room_14_final_room")
            break

        elif choice == "debug":
            debug_menu()

        elif choice == "pause":
            pause_menu()

        else:
            print(f"\n{RED}Invalid choice. Try again.{RESET}")

#======================================================================

#Looking around the kitchen
def look_around_kitchen():
    while True:
        type_text("\nYou scan the kitchen. What do you want to check?")
        print("1. The Counter")
        print("2. The Fridge")
        print("3. The Drawer")
        print(f"4. {RED}Nevermind{RESET}")

        choice = input("> ").strip()

        if choice == "1":  #Blue Fuse
            if "Blue Fuse" not in game_states.inventory and "Blue Fuse" not in game_states.fuse_box:
                type_text(f"\nThe counter is covered in dust. A single {MAGENTA}Blue Fuse{RESET} rests here.")
                colorize_blue_fuse()
                game_states.inventory.append("Blue Fuse")
                type_text(f"{GREEN}This could be useful... You take the fuse for now{RESET}")
            else:
                type_text(f"\n{YELLOW}The counter is empty now{RESET}.")

        elif choice == "2":
            type_text("\nThe fridge hums softly, inside the shelves are nearly bare.")
            type_text("Just rotting food and a bad smell... you wonder when was the last time someone lived here.")
            print(ascii_art["fridge"])

        elif choice == "3":  #Drawer/Screwdriver
            if game_states.power_restored:  #Only accessible after restoring power
                if "Screwdriver" not in game_states.inventory:
                    type_text(f"\nYou {GREEN}open{RESET} the drawer and find a rusty screwdriver.")
                    type_text(f"\n{GREEN}This might be useful for prying something open... but what?{RESET}")
                    print(ascii_art["screwdriver"])
                    game_states.inventory.append("Screwdriver")
                else:
                    type_text(f"\n{YELLOW}The drawer is empty now{RESET}.")
            else:
                type_text(f"\n{DIM_WHITE}It's too dark to see inside the drawer{RESET}. You'll need to check back later one the {RED}power{RESET} is restored.")

        elif choice == "4":
            return  #Exit back to the kitchen menu

        elif choice == "debug":
            debug_menu()  #Calls the debug menu

        elif choice == "pause":
            pause_menu()

        else:
            print(f"\n{RED}Invalid choice. Try again{RESET}.")

#======================================================================

#End

#======================================================================