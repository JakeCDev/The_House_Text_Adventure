#======================================================================
#Save system
#save_systems.py
#======================================================================

#internal imports

from text_effects import type_text
from color_scheme import GREEN, RED, DIM_WHITE, RESET
import game_states

#======================================================================

#external imports

import json
import os
import time

#======================================================================

#where to save and what to call it
SAVE_DIR = "game_saves"
SAVE_FILE = os.path.join(SAVE_DIR, "save_file.json")

#Ensure the save directory exists
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

#======================================================================
#save game function

def save_game():
    data = {
        #Player Info
        "player_name": game_states.player_name,
        "inventory": game_states.inventory,
        "item_descriptions": game_states.item_descriptions,

        #Room Progress
        "current_room": game_states.current_room,
        "last_room": game_states.last_room,
        "room_visits": game_states.room_visits,

        #Door States
        "door_open": game_states.door_open,
        "door_checked": game_states.door_checked,
        "door_disappeared": game_states.door_disappeared,
        "front_door_warning_shown": game_states.front_door_warning_shown,

        #Fuse Box
        "power_restored": game_states.power_restored,
        "fuse_box": game_states.fuse_box,
        "incorrect_fuse_attempts": game_states.incorrect_fuse_attempts,
        "fuse_order_hint_found": game_states.fuse_order_hint_found,

        #Safe
        "safe_unlocked": game_states.safe_unlocked,
        "incorrect_safe_attempts": game_states.incorrect_safe_attempts,
        "safe_order_hint_found": game_states.safe_order_hint_found,

        #Lockbox
        "just_used_screwdriver": game_states.just_used_screwdriver,

        #Final Room
        "final_door_appeared": game_states.final_door_appeared,
        "final_sequence_started": game_states.final_sequence_started,
    }

    #succesful save message
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f, indent=4)
    print(f"\n{GREEN}Game saved successfully!{RESET}")

#======================================================================

#load game function
def load_game():
    if not os.path.exists(SAVE_FILE):
        print(f"\n{RED}No save file found.{RESET}")
        return False

    with open(SAVE_FILE, "r") as f:
        data = json.load(f)

    #Load all saved values back into game state
    game_states.player_name = data.get("player_name", "")
    game_states.inventory = data.get("inventory", [])
    game_states.item_descriptions = data.get("item_descriptions", {})

    game_states.current_room = data.get("current_room", "room_1_car")
    game_states.last_room = data.get("last_room", "")
    game_states.room_visits = data.get("room_visits", {})

    game_states.door_open = data.get("door_open", False)
    game_states.door_checked = data.get("door_checked", False)
    game_states.door_disappeared = data.get("door_disappeared", False)
    game_states.front_door_warning_shown = data.get("front_door_warning_shown", False)

    game_states.power_restored = data.get("power_restored", False)
    game_states.fuse_box = data.get("fuse_box", ["Empty", "Empty", "Empty"])
    game_states.incorrect_fuse_attempts = data.get("incorrect_fuse_attempts", 0)
    game_states.fuse_order_hint_found = data.get("fuse_order_hint_found", False)

    game_states.safe_unlocked = data.get("safe_unlocked", False)
    game_states.incorrect_safe_attempts = data.get("incorrect_safe_attempts", 0)
    game_states.safe_order_hint_found = data.get("safe_order_hint_found", False)

    game_states.just_used_screwdriver = data.get("just_used_screwdriver", False)

    game_states.final_door_appeared = data.get("final_door_appeared", False)
    game_states.final_sequence_started = data.get("final_sequence_started", False)

    print(f"\n{GREEN}Game loaded successfully.{RESET}")
    type_text(f"\n{DIM_WHITE}You rub your wary eyes… as if waking from a long, drifting thought.{RESET}")
    time.sleep(1.5)
    type_text(f"\n{DIM_WHITE}Were you dreaming?{RESET}")
    type_text(f"{DIM_WHITE}No… you were here the whole time…{RESET}")
    time.sleep(1.5)
    type_text(f"{DIM_WHITE}Weren't you?{RESET}")
    time.sleep(1.5)
    type_text(f"\n{DIM_WHITE}Your mind re-anchors to reality. You are {game_states.player_name}.{RESET}")
    type_text(f"And this place... the {RED}house{RESET}... it never let you go.")
    time.sleep(2)

    return True

#======================================================================