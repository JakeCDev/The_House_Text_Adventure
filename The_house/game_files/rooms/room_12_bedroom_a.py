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
from color_scheme import YELLOW, MAGENTA, BLUE, CYAN, RED, GREEN, BRIGHT_WHITE, RESET

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
        type_text("\nThe bedroom is neat and untouched.")
        type_text("The curtains are drawn, a faint breeze stirs the dust.")

    elif visit_count == 1:  #Past
        type_text(f"\n{YELLOW}Sunlight{RESET} filters through the window.")
        type_text("The bed is unmade, and the faint scent of perfume lingers.")

    elif visit_count == 2:  #Future
        type_text(f"\nThe bedroom has been re furnished, even the {YELLOW}lighting{RESET} seems different.")
        type_text("A few belongings remain scattered on shelves.")

    elif visit_count == 3:  #Eerie
        type_text(f"\nYou hear faint {RED}whispers{RESET}... but no one is here.")
        type_text("The shadows stretch far across the walls.")

    else:  #Altered Reality
        type_text("\nThe room has no walls, an endless desert filled with doors and hallways leading to nowhere.")
        type_text("Nearby the bed floats midair, as if suspended in time.")

#======================================================================

    #Bedroom A art
    print(ascii_art["bedroom_a"])

#======================================================================
    #Bedroom A choices
    while True:
        print("\nWhat do you want to do?")
        print("1. Look around")
        print("2. Wait around in Bedroom A")
        print("3. Go back to the Upstairs Hallway")
        print(f"4. {GREEN}Take the ladder up to the Attic{RESET}")
        print("5. Check Inventory")

        choice = input("> ").strip()

        if choice == "1":
            look_around_bedroom_a()

        elif choice == "2":
            universal_wait()
            input(f"\nPress {GREEN}Enter{RESET} to continue.")

        elif choice == "3":
            game_states.room_visits[room_name] += 1
            visit_room("room_10_upstairs_hallway")

        elif choice == "4":
            game_states.room_visits[room_name] += 1
            visit_room("room_13_attic")

        elif choice == "5":
            check_inventory(room_12_bedroom_a)

        elif choice == "debug":
            debug_menu()  # Calls the debug menu

        elif choice == "pause":
            pause_menu()

        else:
            print(f"\n{RED}Invalid choice. Try again.{RESET}")

#======================================================================
#Looking around in Bedroom A

def look_around_bedroom_a():
    while True:
        type_text("\nYou scan the bedroom. What do you want to check?")
        print("1. The Mirror")
        print("2. The Bookshelf")
        print("3. The Nightstand")
        print(f"4. {RED}Nevermind{RESET}")

        choice = input("> ").strip()

        if choice == "1":
            type_text("\nThe mirror is covered in dust. You can barely make out your reflection...")
            type_text(f"For a brief second, you thought you saw {RED}someone{RESET} standing behind you.")
            print(ascii_art["bedroom_a_mirror"])

        elif choice == "2":
            type_text("\nAn old journal sits on the shelf. The pages are torn and scattered.")
            type_text(f"One page remains barely legible : {RED}'It was all hidden in the attic'{RESET}.")

            if "Attic Hint" not in game_states.inventory:  #Prevents duplicate entries
                type_text(f"This feels important... {GREEN}you take note of this{RESET}.")
                print(ascii_art["bookshelf"])
                game_states.inventory.append("Attic Hint")
            else:
                type_text(f"{YELLOW}You've already taken notes of this{RESET}.")

        elif choice == "3":
            type_text("\nThe nightstand is covered in a thick layer of dust. A small jewelry box sits on top.")
            print(ascii_art["nightstand"])

        elif choice == "4":
            return  #Exit back to the Bedroom A menu

        elif choice == "debug":
            debug_menu()  #Calls the debug menu

        elif choice == "pause":
            pause_menu()

        else:
            print(f"\n{RED}Invalid choice. Try again{RESET}.")

#======================================================================
