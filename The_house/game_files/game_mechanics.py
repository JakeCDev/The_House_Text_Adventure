#======================================================================
#Game Mechanics - Handles Room Transitions, Doors, and Resets
#game_mechanics.py
#======================================================================

#Internal imports
import game_states
from room_loader import load_room
from text_effects import type_text
from ascii_art import ascii_art

#======================================================================

#External imports
import random

#======================================================================
#Room movement system
#======================================================================

def visit_room(room_name):
    #Check if alias exists and convert to actual room name
    if room_name in game_states.room_aliases:
        room_name = game_states.room_aliases[room_name]

    #Track last room before updating
    game_states.last_room = game_states.current_room
    game_states.current_room = room_name

    #Ensure visit count exists
    if room_name not in game_states.room_visits:
        game_states.room_visits[room_name] = 0  #Start at 0 if not tracked

    #Call the function for the new room
    room_function = load_room(room_name)
    if room_function:
        room_function()
    else:
        print(f"\nERROR - Room '{room_name}' could not be loaded.")
        game_states.current_room = game_states.last_room  #Revert if error

    #Increment visit count (capped at 5)
    game_states.room_visits[room_name] = min(game_states.room_visits[room_name] + 1, 5)

#======================================================================

#======================================================================

universal_wait_responses = [
    "The silence stretches on...",
    "A soft creaking noise echoes through the space... It stops the moment you focus on it.",
    "For a split second, you feel certain something just moved behind you...",
    "The air feels thicker now, almost heavy. Like something unseen is pressing against you.",
    "A shiver runs down your spine...",
    "A faint whisper drifts past, but the words are impossible to catch.",
    "The shadows shift at the edge of your vision... Maybe your mind is playing tricks...",
    "A slow drip echoes somewhere nearby...",
    "You feel a soft vibration under your feet... It stops the moment you notice it.",
    "A gust of wind stirs, carrying a scent you can’t place. Old. Forgotten.",
    "The temperature shifts slightly, but no breeze moves the air...",
    "A flicker of movement—your own shadow? Or something else?",
    "Something in the distance shifts... You can’t quite focus on it.",
    "Your heartbeat seems too loud. Or is everything else just too quiet...",
    "For just a moment, your own name echoes back at you..."
]

def universal_wait():
    #Display random wait response
    print(random.choice(universal_wait_responses))


#======================================================================

#======================================================================
#Inventory check system
#======================================================================

def check_inventory(current_room_function):
    if not game_states.inventory:
        print("\nYour inventory is empty.")
        input("\nPress Enter to return.")
        return

    while True:
        print("\nInventory:")
        for i, item in enumerate(game_states.inventory, 1):
            print(f"{i}. {item}")

        #Allow use of screwdriver functionality
        use_screwdriver_option = None
        if "Screwdriver" in game_states.inventory and "Locked Box" in game_states.inventory:
            use_screwdriver_option = len(game_states.inventory) + 1
            print(f"{use_screwdriver_option}. Use Screwdriver to Open the Lockbox")

        back_option = len(game_states.inventory) + (2 if use_screwdriver_option else 1)
        print(f"{back_option}. Exit Inventory")

        choice = input("\nWhat do you want to do? ").strip()

        if choice.isdigit():
            choice = int(choice)

            if use_screwdriver_option and choice == use_screwdriver_option:
                use_screwdriver()
                return

            elif choice == back_option:
                print("\nExiting inventory...")
                return

            elif 1 <= choice <= len(game_states.inventory):
                item = game_states.inventory[choice - 1]
                print(f"\n{item}: {game_states.item_descriptions.get(item, 'Nothing special about this item.')}")
                input("\nPress enter to return...")

            else:
                print("\nInvalid choice. Try again.")
        else:
            print("\nInvalid choice. Try again.")

#======================================================================

#======================================================================
#Screwdriver mechanics
#======================================================================

def use_screwdriver():
    #Prevent using the screwdriver if the lockbox is already opened
    if "Lockbox Opened" in game_states.inventory:
        type_text("\nThe lockbox is already open. There’s nothing left to pry.")
        return

    #Ensure the player has both the screwdriver and the locked box
    if "Screwdriver" in game_states.inventory and "Locked Box" in game_states.inventory:
        type_text("\nYou carefully wedge the screwdriver under the lock.")
        type_text("With a sharp pop, the lock snaps open.")

        type_text("\nInside, you find a collection of burnt, faded papers.")
        type_text("A newspaper clipping... An obituary... A name that feels... familiar.")
        type_text("\nYour head starts pounding. Memories blur but start to resurface.")

        #Remove the locked box and screwdriver from inventory
        game_states.inventory.remove("Locked Box")
        game_states.inventory.remove("Screwdriver")
        game_states.inventory.append("Lockbox Opened")  #Add opened lockbox to inventory

        #Trigger final door appearance
        game_states.final_door_appeared = True

        type_text("\nA strange warmth fills the air. Something has changed...")
        type_text("Maybe you should check the kitchen again...")
    else:
        type_text("\nYou have nothing to use the screwdriver on.")

#======================================================================
#Front door mechanics
#======================================================================

#When player checks door from outside
def check_front_door():
    #If the door has disappeared, warn the player
    if game_states.door_disappeared:
        if not game_states.front_door_warning_shown:
            type_text("\nYou glance toward the front door...")
            type_text("\nIt's gone.")
            type_text("Nothing remains but a blank wall where the door once stood.")
            game_states.front_door_warning_shown = True  #Ensures message only shows once
        else:
            type_text("\nThe front door is gone. Just an empty wall remains.")
    else:
        type_text("\nYou check the front door. It’s locked. There's no way out.")

#======================================================================

#When the player re enters the entryway / door dissapearance
def check_entryway_for_door():
    #If the door has already disappeared and the warning was shown, do nothing
    if game_states.door_disappeared and game_states.front_door_warning_shown:
        return

    #If this is the player's first entry, the door should NOT disappear yet
    if game_states.room_visits["room_4_entryway"] == 0:
        return  # Do nothing, door stays for now

    #If the player is re-entering after leaving, remove the door
    if game_states.room_visits["room_4_entryway"] > 0 and not game_states.door_disappeared:
        type_text("\nYou glance toward the front door...")
        type_text("\nIt's gone...")
        type_text("\nNothing remains but a blank wall where the door once stood...")

        game_states.door_disappeared = True  #Mark the door as gone
        game_states.front_door_warning_shown = True  #Ensures message only plays once

#======================================================================

#======================================================================
#Fuse box and darkness systems
#======================================================================

def check_fuse_box():
    #If power is already restored, display a short message and return
    if game_states.power_restored:
        type_text("\nThe fuse box hums softly. The lights are already on. No need to touch it again.")
        input("\nPress Enter to return.")
        return

    while True:
        type_text("\nYou open the fuse box. Some slots are empty, their labels barely visible.")
        print(ascii_art["fuse_box"])  #Show ASCII only when power isn't restored

        #Display the current fuse slots
        print(f"[1: {game_states.fuse_box[0]}]  [2: {game_states.fuse_box[1]}]  [3: {game_states.fuse_box[2]}]")
        print("\n1. Insert a fuse")
        print("2. Remove a fuse")
        print("3. Try to activate the fuse box")
        print("4. Nevermind")
        choice = input("> ").strip()

        if choice == "1":
            insert_fuse()
        elif choice == "2":
            remove_fuse()
        elif choice == "3":
            if activate_fuse_box():
                return  #Exit immediately if power is restored
        elif choice == "4":
            return
        else:
            print("\nInvalid choice. Try again.")

#======================================================================

def insert_fuse():
    #Get available fuses in inventory
    available_fuses = [f for f in game_states.inventory if "fuse" in f]

    if not available_fuses:
        type_text("\nYou don't have any fuses to insert.")
        return

    #Ask which fuse to insert
    print("\nWhich fuse do you want to insert?")
    for i, fuse in enumerate(available_fuses, 1):
        print(f"{i}. {fuse}")
    print(f"{len(available_fuses) + 1}. Nevermind")

    fuse_choice = input("> ").strip()

    if not fuse_choice.isdigit():
        print("\nInvalid input. Try again.")
        return insert_fuse()

    fuse_choice = int(fuse_choice)
    if fuse_choice < 1 or fuse_choice > len(available_fuses) + 1:
        print("\nInvalid choice. Try again.")
        return insert_fuse()
    if fuse_choice == len(available_fuses) + 1:
        return

    selected_fuse = available_fuses[fuse_choice - 1]

    #Ask which slot to insert the selected fuse into
    print("\nWhich slot do you want to insert the fuse into?")
    for i in range(3):
        print(f"{i + 1}. {game_states.fuse_box[i]}")
    print("4. Nevermind")

    slot_choice = input("> ").strip()

    if not slot_choice.isdigit():
        print("\nInvalid input. Try again.")
        return insert_fuse()

    slot_choice = int(slot_choice)
    if slot_choice < 1 or slot_choice > 4:
        print("\nInvalid choice. Try again.")
        return insert_fuse()
    if slot_choice == 4:
        return

    slot_index = slot_choice - 1

    #If the chosen slot is occupied, swap the fuses
    if game_states.fuse_box[slot_index] != "Empty":
        old_fuse = game_states.fuse_box[slot_index]
        game_states.fuse_box[slot_index] = selected_fuse
        game_states.inventory.remove(selected_fuse)
        game_states.inventory.append(old_fuse)
        print(f"\nThe slot was occupied by {old_fuse}. It has been swapped out for {selected_fuse}.")
    else:
        game_states.fuse_box[slot_index] = selected_fuse
        game_states.inventory.remove(selected_fuse)
        print(f"\nYou insert the {selected_fuse} into slot {slot_choice}.")

#======================================================================

def remove_fuse():
    print("\nCurrent fuse slots:")
    for i in range(3):
        print(f"{i + 1}: {game_states.fuse_box[i]}")
    print("4: Nevermind")

    slot_choice = input("\nWhich slot do you want to remove a fuse from? (Enter 1-3 or 4 to cancel): ").strip()

    if not slot_choice.isdigit():
        print("\nInvalid input. Try again.")
        return remove_fuse()
    slot_choice = int(slot_choice)
    if slot_choice < 1 or slot_choice > 4:
        print("\nInvalid slot number. Try again.")
        return remove_fuse()
    if slot_choice == 4:
        return

    slot_index = slot_choice - 1
    if game_states.fuse_box[slot_index] == "Empty":
        type_text("\nThat slot is already empty.")
        return remove_fuse()  #Allow the player to try another slot.

    removed_fuse = game_states.fuse_box[slot_index]
    game_states.inventory.append(removed_fuse)
    game_states.fuse_box[slot_index] = "Empty"
    print(f"\nYou remove the {removed_fuse} from slot {slot_choice} and return it to your inventory.")

#======================================================================

def activate_fuse_box():
    #Check if the fuse box has the correct order
    if game_states.fuse_box == ["red fuse", "green fuse", "blue fuse"]:
        type_text("\nYou hear a satisfying *CLICK* as the fuse box activates. The lights flicker back to life!")

        #Update game state
        game_states.power_restored = True

        input("\nPress Enter to return.")
        visit_room("room_4_entryway")  #Send player back to the Entryway
        return True  #Exit immediately

    else:
        type_text("\nThe fuse box hums loudly, then *buzz*... silence.")
        type_text("\nSomething isn't right. You should try again.")

        #Reset fuses on failure
        for i in range(3):
            if game_states.fuse_box[i] != "Empty":
                game_states.inventory.append(game_states.fuse_box[i])
                game_states.fuse_box[i] = "Empty"

        game_states.incorrect_fuse_attempts += 1

        #If the player fails 3 times, reset the game
        if game_states.incorrect_fuse_attempts == 3:
            type_text("\nA dark presence fills the room... Your vision fades to black...")
            reset_game()

        return False  #Stay in the fuse box menu if incorrect

#======================================================================

#======================================================================
#Safe puzzle
#======================================================================

def inspect_safe():
    type_text("\nThe safe is old and rusted. A 3-digit keypad is built into the front.")
    type_text("There must be hints somewhere...")

    while True:
        safe_code = input("\nEnter the 3-digit code: ").strip()

        #Check if input is valid 3 digits
        if not safe_code.isdigit() or len(safe_code) != 3:
            type_text("\nInvalid input! The passcode must be a 3-digit number.")
            game_states.incorrect_safe_attempts += 1

        elif safe_code == "673":  #Correct code unlocks the safe
            if "Skeleton Key" not in game_states.inventory:
                type_text("\nThe safe clicks open. Inside, you find an old brass Skeleton Key.")
                type_text("Perhaps it unlocks that spare room upstairs. (Skeleton Key obtained!)")
                game_states.inventory.append("Skeleton Key")
            else:
                type_text("\nThe safe is already open, nothing left inside.")

            game_states.safe_unlocked = True
            input("\nPress Enter to continue.")
            visit_room("room_7_basement")  #Move to basement after unlocking the safe
            break

        else:
            game_states.incorrect_safe_attempts += 1
            type_text("\nThe keypad beeps... incorrect code.")

            #Spooky warnings for wrong attempts
            if game_states.incorrect_safe_attempts == 1:
                type_text("\nA chill runs down your spine...")
            elif game_states.incorrect_safe_attempts == 2:
                type_text("\nThe rusted safe rattles slightly. A deep, guttural sound echoes from inside the darkness.")

        #Fail condition - resets game after 3 failed attempts
        if game_states.incorrect_safe_attempts >= 3:
            type_text("\nA suffocating darkness fills the room. The air grows ice cold around you.")
            type_text("A hand not your own grips your shoulder... Your vision fades...")
            type_text("\nYou awaken back in the car. The rain still falls. Harder than before. But you must still press on.")
            reset_game()
            break

        input("\nIncorrect code. Press Enter to try again.")

#======================================================================

#======================================================================
#Reset mechanic
#======================================================================

def reset_game():
    global door_disappeared, front_door_warning_shown, door_open, door_checked, inventory, fuse_order_hint_found, safe_order_hint_found

    #Reset the front door state
    door_disappeared = False
    front_door_warning_shown = False
    inventory.clear()
    fuse_order_hint_found = False
    safe_order_hint_found = False
#======================================================================

#total reset
def full_reset_game():
    #Resets ALL game states, including inventory, visited rooms, and progress

    #Reset core game tracking variables
    game_states.current_room = "room_1_car"
    game_states.last_room = None

    #Fully reset room visit counts
    game_states.room_visits = {room: 0 for room in game_states.room_visits}

    #Clear the player's inventory
    game_states.inventory.clear()

    #Reset all major puzzle and progress flags
    game_states.safe_unlocked = False
    game_states.power_restored = False
    game_states.fuse_box = ["Empty", "Empty", "Empty"]
    game_states.door_disappeared = False
    game_states.final_door_appeared = False
    game_states.final_sequence_started = False
    game_states.incorrect_fuse_attempts = 0
    game_states.incorrect_safe_attempts = 0
    game_states.front_door_warning_shown = False

    #Reset item discovery tracking (optional)
    game_states.fuse_order_hint_found = False
    game_states.safe_order_hint_found = False

    print("\n[DEBUG] Full game reset complete. Ready for a fresh start.")

#======================================================================
#Final/ending door mechanic
#======================================================================
def check_final_door():
    #Ensure the final door only appears after opening the Lockbox
    if "Lockbox Opened" in game_states.inventory and not game_states.final_door_appeared:
        type_text("\nA door you swear wasn’t there before now stands along the north wall.")
        type_text("A warm, soft light glows from beyond it, beckoning you forward.")
        type_text("It feels... safe. Familiar, somehow.")

        game_states.final_door_appeared = True
#======================================================================

