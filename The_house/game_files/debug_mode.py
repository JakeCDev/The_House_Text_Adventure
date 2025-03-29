#======================================================================
#Debugging menu options
#debug_mode.py
#======================================================================

#Imports
from text_effects import type_text
import game_states
from color_scheme import RED, GREEN, YELLOW, BLUE, CYAN, MAGENTA, BRIGHT_MAGENTA, BRIGHT_YELLOW, BRIGHT_CYAN, DIM_WHITE, RESET
from game_mechanics import visit_room
from sound_manager import sync_ambient_to_room, play_sound_effect
import time
import random

#======================================================================

#Rainbow text
def colorize_rainbow_text(text, delay=0.01):
    colors = [RED, GREEN, BLUE, MAGENTA, CYAN]
    for char in text:
        color = random.choice(colors)
        print(f"{color}{char}{RESET}", end='', flush=True)
        time.sleep(delay)
    print()  #Finish with new line

#======================================================================

def debug_menu():
    #Handles debug commands for teleporting, inventory changes, and room tracking
    #use end= to prevent new line
    print(f"\n{BRIGHT_YELLOW}[DEBUG MODE]{RESET} ", end='')
    colorize_rainbow_text("Bending reality please hold...", delay=0.02)
    play_sound_effect("debug_sound.wav")

#======================================================================

    #slow dot "loading" effect
    for _ in range(1):
        for _ in range(3):  #Print 3 dots with delays
            print(".", end=" ", flush=True)  #Print dot without newline
            time.sleep(.5)  #Delay
        print()  #Move to the next line after 3 dots

    print(f"Type a command or '{RED}exit{RESET}' to leave.")
    print(f"Type '{GREEN}help{RESET}' for a list of debug commands.")

    while True:
        command = input(f"\n{BRIGHT_YELLOW}[DEBUG] > ").strip().lower()

#======================================================================

        #Debug teleport with alias mapping
        if command.startswith("teleport "):
            room_input = command.replace("teleport ", "").strip()

            #Check for a valid alias
            if room_input in game_states.room_aliases:
                room_name = game_states.room_aliases[room_input]  #Convert alias to real room name
                print(f"\n{BRIGHT_YELLOW}[DEBUG]{RESET} {BRIGHT_MAGENTA}Teleporting to {room_input} ({room_name})...{RESET}")

                #Sync ambient sounds before entering the room
                if room_name in game_states.room_sound_map:
                    sync_ambient_to_room(room_name, game_states.room_sound_map)

                else:
                    print(f"{BRIGHT_YELLOW}[DEBUG]{RESET} {RED}No expected ambient data found for {room_name}.{RESET}")
                visit_room(room_name)
                return  #Return to gameplay after teleporting

            else:
                print(f"\n{BRIGHT_YELLOW}[DEBUG]{RESET} {RED}Invalid room name. Try again.{RESET}")

#======================================================================

        #Debug inventory manipulation
        elif command.startswith("add "):
            item = command.replace("add ", "").strip()

            #Ensure correct item checking exact match in item_descriptions
            item = next((key for key in game_states.item_descriptions if key.lower() == item.lower()), item)

            if item in game_states.inventory:
                print(f"\n{YELLOW}[DEBUG] '{item}' is already in inventory.{RESET}")
            elif item in game_states.item_descriptions:
                game_states.inventory.append(item)
                print(f"\n{BRIGHT_YELLOW}[DEBUG]{RESET} {GREEN}Added '{item}' to inventory.{RESET}")
            else:
                print(f"\n{BRIGHT_YELLOW}[DEBUG]{RESET} {RED}Invalid item name. Check spelling or refer to available items.{RESET}")

        elif command.startswith("remove "):
            item = command.replace("remove ", "").strip()

            #Match against exact item names
            item = next((key for key in game_states.item_descriptions if key.lower() == item.lower()), item)

            if item in game_states.inventory:
                game_states.inventory.remove(item)
                print(f"\n{BRIGHT_YELLOW}[DEBUG]{RESET} {GREEN}Removed '{item}' from inventory.{RESET}")
            else:
                print(f"\n{BRIGHT_YELLOW}[DEBUG]{RESET} {RED}'{item}' is not in your inventory.{RESET}")

#======================================================================

        #Debug check room visit count
        elif command.startswith("visits"):
            room_input = command.replace("visits ", "").strip().lower()

            if room_input == "all":  #Show visits for all rooms
                print(f"\n{BRIGHT_YELLOW}[DEBUG]{RESET} {BRIGHT_MAGENTA}Room Visit Counts:{RESET}")
                for alias, room_name in sorted(game_states.room_aliases.items(), key=lambda x: x[1]):
                    count = game_states.room_visits.get(room_name, 0)
                    print(f"  {alias.title()}: {count} visits")
            elif room_input in game_states.room_aliases:
                room_name = game_states.room_aliases[room_input]
                count = game_states.room_visits.get(room_name, 0)
                print(f"\n{BRIGHT_YELLOW}[DEBUG]{RESET} {BRIGHT_MAGENTA}{room_input.title()} has been visited {count} times.{RESET}")
            else:
                print(f"\n{BRIGHT_YELLOW}[DEBUG]{RESET} {RED}No room found matching '{room_input}'. Try again.{RESET}")

#======================================================================

        #Help command
        elif command == "help":
            print(f"\n{BRIGHT_YELLOW}[DEBUG]{RESET} {GREEN}Available commands:{RESET}")
            print("  - teleport <room_name>  → Move instantly to a room (ex - 'teleport attic').")
            print("  - add <item_name>       → Add an item to inventory.")
            print("  - remove <item_name>    → Remove an item from inventory.")
            print("  - list items            → Show all valid item names.")
            print("  - visits <room_name>    → Check how many times a room was visited.")
            print("  - visits all            → Show visit counts for all rooms.")
            print("  - check states          → View all permanent game states.")
            print("  - toggle power          → Toggle power on/off for testing.")
            print("  - toggle safe           → Toggle safe unlocked/locked.")
            print("  - toggle door           → Toggle front door disappearing.")
            print("  - reset attempts        → Reset fuse/safe incorrect attempts.")
            print("  - reset fuse            → Reset the fuse box.")
            print(f"  - {RED}exit{RESET}                  → {RED}Leave debug mode{RESET}.")

#======================================================================

        #Check game states
        elif command == "check states":
            print(f"\n{BRIGHT_YELLOW}[DEBUG]{RESET} {GREEN}Permanent Game States:{RESET}")

            def state_line(label, value):
                color = GREEN if value else RED
                return f"{label}: {color}{value}{RESET}"

            print("  " + state_line("Power Restored", game_states.power_restored))
            print("  " + state_line("Safe Unlocked", game_states.safe_unlocked))
            print("  " + state_line("Fuse Order Hint Found", game_states.fuse_order_hint_found))
            print("  " + state_line("Safe Order Hint Found", game_states.safe_order_hint_found))
            print("  " + state_line("Front Door Disappeared", game_states.door_disappeared))
            print("  " + state_line("Final Door Appeared", game_states.final_door_appeared))
            print("  " + state_line("Final Sequence Started", game_states.final_sequence_started))

            print(f"  Incorrect Fuse Attempts: {YELLOW}{game_states.incorrect_fuse_attempts}{RESET}")
            print(f"  Incorrect Safe Attempts: {YELLOW}{game_states.incorrect_safe_attempts}{RESET}")
            print(f"  Fuse Box State: {CYAN}{game_states.fuse_box}{RESET}")

#======================================================================

        #toggle states

        #Toggle power restored (for testing kitchen drawer)
        elif command == "toggle power":
            game_states.power_restored = not game_states.power_restored
            status = f"{GREEN}ON{RESET}" if game_states.power_restored else f"{RED}OFF{RESET}"
            print(f"\n{BRIGHT_YELLOW}[DEBUG]{RESET} Power Restored: {status}")

        # Toggle safe unlocked
        elif command == "toggle safe":
            game_states.safe_unlocked = not game_states.safe_unlocked
            status = f"{GREEN}UNLOCKED{RESET}" if game_states.safe_unlocked else f"{RED}LOCKED{RESET}"
            print(f"\n{BRIGHT_YELLOW}[DEBUG]{RESET} Safe Unlocked: {status}")

        # Toggle front door disappearance
        elif command == "toggle door":
            game_states.door_disappeared = not game_states.door_disappeared
            status = f"{GREEN}TRUE{RESET}" if game_states.door_disappeared else f"{RED}FALSE{RESET}"
            print(f"\n{BRIGHT_YELLOW}[DEBUG]{RESET} Front Door Disappeared: {status}")

        #Reset incorrect puzzle attempts
        elif command == "reset attempts":
            game_states.incorrect_fuse_attempts = 0
            game_states.incorrect_safe_attempts = 0
            print(f"\n{BRIGHT_YELLOW}[DEBUG]{RESET} {GREEN}All incorrect puzzle attempts reset.{RESET}")

        #Reset fuse box
        elif command == "reset fuse":
            game_states.fuse_box = ["Empty", "Empty", "Empty"]
            print(f"\n{BRIGHT_YELLOW}[DEBUG]{RESET} {GREEN}Fuse Box has been reset.{RESET}")

#======================================================================

            #List all available items
        elif command == "list items":
            print(f"\n{BRIGHT_YELLOW}[DEBUG]{RESET} {GREEN}Available Items:{RESET}")
            for item in game_states.item_descriptions.keys():
                print(f"  - {item}")

#======================================================================

        #Debug Exit
        elif command == "exit":
            print(f"\n{BRIGHT_YELLOW}[DEBUG]{RESET} {RED}Exiting debug mode...{RESET}")
            return  #Return to normal gameplay

        else:
            print(f"\n{BRIGHT_YELLOW}[DEBUG]{RESET} {RED}Invalid command{RESET}. Type '{GREEN}help{RESET}' {RED}for a list of debug commands.{RESET}")

#======================================================================

#End

#======================================================================