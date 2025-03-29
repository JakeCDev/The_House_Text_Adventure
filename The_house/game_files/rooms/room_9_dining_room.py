#======================================================================
#Dining Room: 9
#room_9_dining_room.py
#======================================================================

#Imports
import game_states
from game_mechanics import visit_room, check_inventory, universal_wait
from text_effects import type_text
from ascii_art import ascii_art
from debug_mode import debug_menu
from pause_menu import pause_menu
from color_scheme import YELLOW, MAGENTA, BLUE, CYAN, RED, GREEN, DIM_WHITE, RESET
from sound_manager import stop_ambient_loop, play_ambient_loop, play_sound_effect
import random

#======================================================================

def colorize_dining_table():
    table_art = ascii_art["dining_table"]
    for char in table_art:
        if char == "*":
            print(f"{YELLOW}*{RESET}", end="")  # Lit candle flame
        else:
            print(char, end="")

#======================================================================

def colorized_plates():
    plates_art = ascii_art["plates"]
    for char in plates_art:
        if char == "█":
            print(f"{RED}{char}{RESET}", end="")
        else:
            print(char, end="")

#======================================================================

#Dining room function
def room_9_dining_room():

    #Room tracker
    room_name = "room_9_dining_room"
    visit_count = game_states.room_visits.get(room_name, 0)

    #music
    stop_ambient_loop("vintage", fade_out=1000)
    play_ambient_loop("house", "house_loop.wav", 0.6)

    #Room state change
    if visit_count == 0:  #Present
        type_text("\nThe dining table is bare, the chairs neatly pushed in.")
        type_text(f"A {YELLOW}chandelier{RESET} hangs above.")

    elif visit_count == 1:  #Past
        type_text("\nThe table is set for dinner, plates arranged neatly.")
        type_text(f"You hear the faintest {DIM_WHITE}echo{RESET} of laughter, distant and fading.")

    elif visit_count == 2:  #Future
        type_text("\nThe dining room has been remodeled. A new table, new paintings, its all different now.")
        type_text("It feels as if a family lives here , though there’s no sign of them at the moment.")

    elif visit_count == 3:  #Eerie
        type_text("\nA single chair sits in the middle of the room...")
        type_text(f"The {YELLOW}chandelier{RESET} sways gently, though there’s no breeze...")

    else:  #Altered Reality
        type_text(f"\nThe table has {RED}snapped{RESET} into pieces that float around the room...")
        type_text("The floor now covered in silverware and shattered plates...")

#======================================================================

    #Dining room art
    colorize_dining_table()

#======================================================================

    #Dining room choices
    while True:
        print("\nWhat do you want to do?")
        print("1. Look around")
        print("2. Wait around the dining room")
        print("3. Go west to the Kitchen")
        print("4. Go south to the Living Room")
        print("5. Go upstairs to the Upstairs Hallway")
        print("6. Check Inventory")

        choice = input("> ").strip()

        if choice == "1":
            look_around_dining_room()

        elif choice == "2":
            universal_wait()
            input(f"\nPress {GREEN}Enter{RESET} to continue.")

        elif choice == "3":
            game_states.room_visits[room_name] += 1
            visit_room("room_6_kitchen")

        elif choice == "4":
            game_states.room_visits[room_name] += 1
            visit_room("room_8_living_room")

        elif choice == "5":
            game_states.room_visits[room_name] += 1
            play_sound_effect("stair_sound.wav")
            visit_room("room_10_upstairs_hallway")

        elif choice == "6":
            check_inventory(room_9_dining_room)

        elif choice == "debug":
            debug_menu()  # Calls the debug menu

        elif choice == "pause":
            pause_menu()

        else:
            print(f"\n{RED}Invalid choice. Try again.{RESET}")

#======================================================================

#Looking around dining room
def look_around_dining_room():
    while True:
        type_text("\nYou scan the dining room. What do you want to check?")
        print("1. The Table")
        print("2. The Chairs")
        print("3. The lamp")
        print(f"4. {RED}Nevermind{RESET}")

        choice = input("> ").strip()

        if choice == "1":
            type_text("\nYou run your fingers along the table’s surface. There’s a deep scratch, as if someone carved something here.")
            type_text(f"You look closer... A single number is {RED}etched{RESET} into the wood")

            if "Dining Room Safe Password Hint" not in game_states.inventory:
                game_states.inventory.append("Dining Room Safe Password Hint")
                type_text(f"{GREEN}This feels important... You should take note of this{RESET}.")
            else:
                type_text(f"{YELLOW}You've already taken note of this{RESET}.")

            colorized_plates()

        elif choice == "2":
            type_text("\nThe chairs are old and worn, as if they haven’t been used in years.")
            print(ascii_art["chair"])

        elif choice == "3":
            type_text(f"\nThe lamp {YELLOW}flickers{RESET} on and off, the chain doesn't seem to work either way.")
            print(ascii_art["lamp"])

        elif choice == "4":
            return  #Exit back to the dining room menu

        elif choice == "debug":
            debug_menu()  #Calls the debug menu

        elif choice == "pause":
            pause_menu()

        else:
            print(f"\n{RED}Invalid choice. Try again{RESET}.")

#======================================================================

#End

#======================================================================