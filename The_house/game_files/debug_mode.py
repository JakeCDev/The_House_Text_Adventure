#======================================================================
#Debugging menu options
#debug_mode.py
#======================================================================
from text_effects import type_text
#Internal imports
from game_mechanics import visit_room
import game_states

#======================================================================

#External imports
import time

#======================================================================

def debug_menu():
    #Handles debug commands for teleporting, inventory changes, and room tracking
    type_text("\n[DEBUG MODE] Bending reality please hold")

#======================================================================

    #Repeat the effect for two lines
    for _ in range(1):
        for _ in range(3):  #Print 3 dots with delays
            print(".", end=" ", flush=True)  #Print dot without newline
            time.sleep(1)  #Delay for 1 second
        print()  #Move to the next line after 3 dots

    print("Type a command or 'exit' to leave.")
    print("Type 'help' for a list of debug commands.")

    while True:
        command = input("\n[DEBUG] > ").strip().lower()

#======================================================================

        #Debug teleport with alias mapping
        if command.startswith("teleport "):
            room_input = command.replace("teleport ", "").strip()

            #Check for a valid alias
            if room_input in game_states.room_aliases:
                room_name = game_states.room_aliases[room_input]  #Convert alias to real room name
                print(f"\n[DEBUG] Teleporting to {room_input} ({room_name})...")
                visit_room(room_name)
                return  #Return to gameplay after teleporting
            else:
                print("\n[DEBUG] Invalid room name. Try again.")

#======================================================================

        #Debug inventory manipulation
        elif command.startswith("add "):
            item = command.replace("add ", "").strip()
            if item:
                if item in game_states.inventory:
                    print(f"\n[DEBUG] '{item}' is already in inventory.")
                else:
                    game_states.inventory.append(item)
                    print(f"\n[DEBUG] Added '{item}' to inventory.")
            else:
                print("\n[DEBUG] Invalid item name.")

        elif command.startswith("remove "):
            item = command.replace("remove ", "").strip()
            if item in game_states.inventory:
                game_states.inventory.remove(item)
                print(f"\n[DEBUG] Removed '{item}' from inventory.")
            else:
                print(f"\n[DEBUG] '{item}' is not in your inventory.")

#======================================================================

        #Debug check room visit count
        elif command.startswith("visits"):
            room_input = command.replace("visits ", "").strip().lower()

            if room_input == "all":  #Show visits for all rooms
                print("\n[DEBUG] Room Visit Counts:")
                for alias, room_name in sorted(game_states.room_aliases.items(), key=lambda x: x[1]):
                    count = game_states.room_visits.get(room_name, 0)
                    print(f"  {alias.title()}: {count} visits")
            elif room_input in game_states.room_aliases:
                room_name = game_states.room_aliases[room_input]
                count = game_states.room_visits.get(room_name, 0)
                print(f"\n[DEBUG] {room_input.title()} has been visited {count} times.")
            else:
                print(f"\n[DEBUG] No room found matching '{room_input}'. Try again.")

#======================================================================

        #Help command
        elif command == "help":
            print("\n[DEBUG] Available commands:")
            print("  - teleport <room_name>  → Move instantly to a room (e.g., 'teleport attic').")
            print("  - add <item_name>       → Add an item to inventory.")
            print("  - remove <item_name>    → Remove an item from inventory.")
            print("  - visits <room_name>    → Check how many times a room was visited.")
            print("  - visits all            → Show visit counts for all rooms.")
            print("  - check states          → View all permanent game states.")
            print("  - exit                  → Leave debug mode.")
#======================================================================
        #Check game states
        elif command == "check states":
            print("\n[DEBUG] Permanent Game States:")
            print(f"  Power Restored: {game_states.power_restored}")
            print(f"  Safe Unlocked: {game_states.safe_unlocked}")
            print(f"  Fuse Order Hint Found: {game_states.fuse_order_hint_found}")
            print(f"  Safe Order Hint Found: {game_states.safe_order_hint_found}")
            print(f"  Front Door Disappeared: {game_states.door_disappeared}")
            print(f"  Final Door Appeared: {game_states.final_door_appeared}")
            print(f"  Final Sequence Started: {game_states.final_sequence_started}")
            print(f"  Incorrect Fuse Attempts: {game_states.incorrect_fuse_attempts}")
            print(f"  Incorrect Safe Attempts: {game_states.incorrect_safe_attempts}")
            print(f"  Fuse Box State: {game_states.fuse_box}")
#======================================================================
        #Debug Exit
        elif command == "exit":
            print("\n[DEBUG] Exiting debug mode...")
            return  #Return to normal gameplay

        else:
            print("\n[DEBUG] Invalid command. Type 'help' for a list of debug commands.")