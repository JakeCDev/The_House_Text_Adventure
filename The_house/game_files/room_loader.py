#======================================================================
#Room loader
#Room.loader.py
#======================================================================

#Internal imports
import game_states
from color_scheme import RED

#======================================================================

#External imports
import importlib

#======================================================================

#Function to load rooms
def load_room(room_name):
    try:
        module = importlib.import_module(f"rooms.{room_name}")  #Example: "rooms.room_1_car"
        return getattr(module, room_name)  #Look for "room_1_car()" inside "room_1_car.py"
    except (ModuleNotFoundError, AttributeError):
        print(f"\n{RED}ERROR: Room '{room_name}' does not exist.{RESET}")
        return None

#======================================================================
