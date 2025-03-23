#======================================================================
#Road room: 2
#rooms/room_2_road.py
#======================================================================

#Internal imports
import game_states
from game_mechanics import visit_room, check_inventory, universal_wait
from text_effects import type_text
from ascii_art import ascii_art
from debug_mode import debug_menu
from pause_menu import pause_menu
from color_scheme import YELLOW, RED, WHITE, CYAN, BLUE, BRIGHT_BLUE, BRIGHT_CYAN, BRIGHT_YELLOW, DIM_WHITE, RESET


#======================================================================

#External imports
import random

#======================================================================

#Sky coloring function - def before the room to prevent circular imports / keep ascii dictionary clean
def colorized_sky(sky_art):
    sky_colors = {
        '*': [WHITE, DIM_WHITE, CYAN],
        'o': [YELLOW, BRIGHT_YELLOW],
        '/': [BRIGHT_CYAN, BRIGHT_BLUE],
        '\\': [BRIGHT_CYAN, BRIGHT_BLUE],
        '+': [CYAN, BRIGHT_CYAN],
    }

    for line in sky_art.strip("\n").splitlines():
        colored_line = ""
        for char in line:
            if char in sky_colors:
                color = random.choice(sky_colors[char])
                colored_line += f"{color}{char}{RESET}"
            else:
                colored_line += char
        print(colored_line)

#======================================================================

#Road function room: 2
def room_2_road():
    #Room tracker
    room_name = "room_2_road"
    visit_count = game_states.room_visits.get(room_name, 0)

    #Room states
    if visit_count == 0:  #Present
        type_text("\nThe road stretches ahead, wet with rain and lined with trees.")
        type_text(f"{RED}The house{RESET} looms in the distance, barely visible in the storm.")

    elif visit_count == 1:  #Past
        type_text(f"\nThe road feels different. The storm nearly gone, replaced by the golden {YELLOW}glow{RESET} of the sunset and streetlights.")
        type_text("You hear the distant sound of laughter—like a memory just out of reach.")

    elif visit_count == 2:  #Future
        type_text("\nThe road is cracked and overgrown. Covered in tire tracks and debris...")
        type_text(f"{DIM_WHITE}It feels like no one has walked this path in years...{RESET}")

    elif visit_count == 3:  #Eerie
        type_text("\nThe trees seem taller than before, their branches stretching toward you.")
        type_text(f"The wind carries a {BLUE}whisper{RESET}, though you can't quite make out the words...")

    else:  #Altered Reality
        type_text(f"\nThe road now bends and twists like a {CYAN}river{RESET}, flowing beneath your feet...")
        type_text("The trees have become a surreal dream, their trunks twist in all directions, their leaves glisten like glass...")

#======================================================================
    #Road art
    def print_colored_road(road_art):
        for line in road_art.strip("\n").splitlines():
            pipe_indexes = [i for i, c in enumerate(line) if c == "|"]
            if pipe_indexes:
                mid_index = pipe_indexes[len(pipe_indexes) // 2]
                chars = list(line)
                chars[mid_index] = f"{YELLOW}|{RESET}"
                print("".join(chars))
            else:
                print(line)
    print()
    print_colored_road(ascii_art["road"])

#======================================================================

    #Road choices
    while True:
        print("\nWhat do you want to do?")
        print("1. Look around")
        print("2. Wait on the road")
        print("3. Move north towards the house")
        print("4. Check Inventory")

        choice = input("> ").strip()

        if choice == "1":
            look_around_road()

        elif choice == "2":
            universal_wait()
            input("\nPress Enter to continue.")

        elif choice == "3":  #Move to porch
            type_text(f"\nYou move toward {RED}the house{RESET}...")
            game_states.room_visits[room_name] += 1
            visit_room("room_3_porch")
            break

        elif choice == "4":
            check_inventory(room_2_road)

        elif choice == "debug":
            debug_menu()  #Calls the debug menu

        elif choice == "pause":
            pause_menu()

        else:
            print(f"\n{RED}Invalid choice. Try again.{RESET}")

#======================================================================
#Look around road
def look_around_road():
    while True:
        type_text("\nYou glance around the empty road. What would you like to check?")
        print("1. The trees")
        print("2. The signpost")
        print("3. The sky")
        print(f"4. {RED}Nevermind{RESET}")

        choice = input("> ").strip()

        if choice == "1":
            type_text("\nThe trees are tall and twisted. Their branches reaching upward.")
            type_text(f"You have the distinct feeling that... {DIM_WHITE}something{RESET} is watching you.")
            print(ascii_art["tree"])

        elif choice == "2":
            type_text("\nYou step closer to the signpost. Unfortunately, the letters are too faded to read, perhaps it's for a nearby town.")
            type_text(f"For a moment, the words look... {DIM_WHITE}wrong{RESET}. Almost foreign.")
            print(ascii_art["signpost"])

        elif choice == "3":
            type_text("\nThe dark night sky is littered with stars. The occasional lightning flash breaks the darkness.")
            colorized_sky(ascii_art["sky"])

        elif choice == "4":
            return  #Exit back to the road menu

        elif choice == "debug":
            debug_menu()  #Calls the debug menu

        elif choice == "pause":
            pause_menu()

        else:
            print(f"\n{RED}Invalid choice. Try again.{RESET}")