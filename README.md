
The House

#======================================================================

Game Description:
A text-based psychological horror adventure where players explore a mysterious house, uncover hidden secrets, and piece together a forgotten past.

#======================================================================

Story Summary:
- You find yourself stranded on a stormy night after a car accident.
- Seeking shelter, you enter "The House"
- Strange events unfold, memories resurface, and you must discover the truth to escape.

#======================================================================

 How to Play:
1. Run the game:
   - If using Python:
     python main.py
   - If using an executable:
     - Double-click the_house.exe / main.exe  **version dependant**

2. Game Commands:
   - Type the number related to the action you wish to take
   - Type "debug" to enter the debug menu

#======================================================================

Game File and loop explanation
- main.py - The core game loop.
- rooms - Contains all room scripts (each room is an independent .py file).
- game_mechanics.py - Handles movement, inventory operations, and puzzles.
- game_states.py - Handles all trackers for mechanics as well as inventory, aliases, etc
- room_loader.py handles actual room movement
    -room calls the visit_room in mechanics
    -Checks if room_name has an alias and converts it if necessary.
    -Stores the previous room in game_states.last_room.
    -Updates game_states.current_room to the new room name.
    -Ensures game_states.room_visits[room_name] is tracked and capped at 5.
    -Calls load_room(room_name) to load the correct room function.

    -Uses importlib.import_module() to load  rooms/room_X.py file.
    -Searches inside that file for a function named after the room ex:"room_2_road" inside room_2_road.py
    -If found it returns that function so visit_room() can execute it.
    -Displays room description based on visit_count to change room states.
    -Presents choices (look around, move to another room, check inventory, etc.)
    -If the player moves again, it calls visit_room(new_room_name), repeating the process.
- ascii_art.py - Stores ASCII visuals for immersive text effects.
- game_intro.py/start_menu.py - Manages the introduction sequence.
- requirements.txt - Lists required Python packages


#======================================================================


Installation/Requirements:
If Running from Code:
- Requires Python 3
- Install dependencies (if needed):
  pip install -r requirements.txt

If Running from a .exe:
- No installation needed just extract and run the main exe

#======================================================================

Credits:
- Game Developed By: Jake Chrissinger
- Tools Used: Python, PyCharm

#======================================================================

Future Plans:
- Implement sound effects.
- Implement colors
- Smooth out game dialogue and transitions
- Add more dynamic interactions.
- Improve puzzle complexity.

#======================================================================
