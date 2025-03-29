#======================================================================
#Entryway Room: 4 - (First Room Inside the House)
#room_4_entryway.py
#======================================================================

#Imports
import game_states
from game_mechanics import visit_room, check_front_door, check_entryway_for_door, check_inventory, check_fuse_box, universal_wait
from text_effects import type_text
from ascii_art import ascii_art
from debug_mode import debug_menu
from pause_menu import pause_menu
from color_scheme import YELLOW, MAGENTA, BLUE, CYAN, RED, GREEN, DIM_WHITE, RESET
from sound_manager import play_ambient_loop, stop_ambient_loop, set_ambient_volume, play_sound_effect
import random

#======================================================================

#colorize for red fuse def before the room to prevent circular imports / keep ascii dictionary clean
def colorize_red_fuse():
    fuse_art = ascii_art["red_fuse"]

    for line in fuse_art.splitlines():
        if "RED" in line:
            line = line.replace("RED", f"{RED}RED{RESET}")
        print(line)

#======================================================================

#Entryway function room: 4
def room_4_entryway():

    #Room tracker
    room_name = "room_4_entryway"
    visit_count = game_states.room_visits.get(room_name, 0)

    #stop outside music and sounds and begin house music.
    stop_ambient_loop("rain", fade_out=1000)
    stop_ambient_loop("wind", fade_out=1000)
    stop_ambient_loop("spooky", fade_out=1000)
    stop_ambient_loop("vintage", fade_out=1000)
    play_ambient_loop("house", "house_loop.wav", 0.6)

    #Check if the front door has disappeared
    check_entryway_for_door()

    #Room state changes
    if visit_count == 0:  #Present
        type_text("\nAs you step into the room. The house creaks all around you.")
        type_text(f"The entryway is dimly {YELLOW}lit{RESET}. Dust flows through the air.")

    elif visit_count == 1:  #Past
        type_text(f"\nThe wallpaper is clean, the air carries the faint scent of  {MAGENTA}flowers{RESET} and coffee.")
        type_text("Shoes are neatly placed by the front, keys on the table, as if someone was just here...")

    elif visit_count == 2:  #Future
        type_text(f"\nThe walls have been repainted a deep {BLUE}blue{RESET} ... A new table and coat rack stands where the old one was...")
        type_text("It feels like someone else lives here now...")

    elif visit_count == 3:  #Eerie
        type_text("\nYour footsteps echo strangely, as if someone else is walking right behind you...")
        type_text(f"The temperature drops instantly... sending a {CYAN}chill{RESET} down your spine...")

    else:  #Altered Reality
        type_text(f"\nYou step inside, But {RED}the house{RESET} is... wrong... twisted and altered...")
        type_text("The room is now filled with stairs and doors leading nowhere...")

#======================================================================

    #Entryway art
    print(ascii_art["entryway"])
    play_sound_effect("thunder_2.wav", volume=0.4)

#======================================================================

#Entryway choices
    while True:
        print("\nWhat do you want to do?")
        print("1. Look around")
        print("2. Wait in the entryway")
        if not game_states.door_disappeared:
            print(f"3. {YELLOW}Check the front door{RESET}")  #When the door is still there
        else:
            print(f"3. {RED}Check where the door once stood{RESET}")  #After the door vanishes
        print("4. Go west to the Office")
        print("5. Go east to the Living Room")
        print("6. Check Inventory")
        print("7. Check the fuse box")

        choice = input("> ").strip()

        if choice == "1":
            look_around_entryway()

        elif choice == "2":
            universal_wait()
            input(f"\nPress {GREEN}Enter{RESET} to continue.")


        elif choice == "3":  #check_front_door() handles what happens
            check_front_door()

        elif choice == "4":
            game_states.room_visits[room_name] += 1
            visit_room("room_5_office")  #Move west
            break

        elif choice == "5":
            game_states.room_visits[room_name] += 1
            visit_room("room_8_living_room")  #Move east
            break

        elif choice == "6":
            check_inventory(room_4_entryway)

        elif choice == "7":
            check_fuse_box()

        elif choice == "debug":
            debug_menu()  #Calls the debug menu

        elif choice == "pause":
            pause_menu()

        else:
            print(f"\n{RED}Invalid choice. Try again{RESET}.")

#======================================================================

#Look around entryway
def look_around_entryway():
    while True:
        type_text("\nYou scan the dim entryway. What do you want to examine?")
        print("1. The mirror on the wall")
        print("2. The coat rack")
        print("3. The closet")
        print(f"4. {RED}Nevermind{RESET}")

        choice = input("> ").strip()

        if choice == "1":
            type_text(f"\nYou step up to the mirror. {DIM_WHITE}The reflection is hard to make out{RESET}.")
            print(ascii_art["mirror"])

        elif choice == "2":  #Red fuse
            if "Red Fuse" not in game_states.inventory and "Red Fuse" not in game_states.fuse_box:
                type_text("\nAn old coat rack stands by the door. A single coat hangs there.")
                type_text(f"Its pocket has a single {MAGENTA}Red Fuse{RESET}.")
                colorize_red_fuse()
                game_states.inventory.append("Red Fuse")
                type_text(f"{GREEN}This may be useful... you decide to take it for now{RESET}.")
            else:
                type_text(f"{YELLOW}The coat's pockets are empty now{RESET}.")

        elif choice == "3":
            type_text("\nThe closet is bare.")
            type_text(f"For a moment, you think you hear {RED}something{RESET} shuffling behind you...")
            print(ascii_art["door"])

        elif choice == "4":
            return  #Exit back to entryway menu

        elif choice == "debug":
            debug_menu()  #Calls the debug menu

        elif choice == "pause":
            pause_menu()

        else:
            print(f"\n{RED}Invalid choice. Try again{RESET}.")

#======================================================================

#End

#======================================================================

