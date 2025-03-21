#======================================================================
Game Title: The House
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
   - Type "pause" to enter pause menu - access to save / load game features

#======================================================================

Game File and loop explanation

-main.py

    This is the starting point of the game.
    It initializes the game by calling the start menu.
    Also handles transitions to other major segments like loading rooms or returning to the start menu after game completion.

-start_menu.py

    Manages the game’s initial menu and instructions.
    Players can choose to start the game, exit, or access hidden debugging options.
    Sets the tone with a combination of text effects, ASCII art, and a brief introduction.

-game_intro.py

    Contains the introductory sequence when the player first begins the game.
    Introduces the mysterious, eerie atmosphere and hints at the player’s identity and the setting’s backstory.
    Starts the player in the car, establishing the premise that they’ve just emerged from a crash.

-game_states.py

    Holds global variables that track the game’s progress.
    Includes player information (like name and inventory), room visit counts, puzzle states (fuses, safe), and other key flags (doors opened, power restored).
    Essentially the central reference point for what the player has done and what’s currently happening.

-game_mechanics.py

    Defines core functions that handle movement between rooms, inventory management, waiting, and other repeatable actions.
    Provides the backbone of gameplay interaction—how the player’s choices are processed and how their actions affect the game world.

-pause_menu.py

    Adds a pause feature that players can access by typing “pause” during gameplay.
    Offers options to resume, save, load, return to the main menu, or exit.
    Provides a more seamless way to access game functions without quitting entirely.

-save_system.py

    Handles saving and loading game progress.
    Saves the player’s current state (location, inventory, puzzle progress, etc.) into a JSON file.
    Allows players to return to their previous state after exiting and reloading the game.

-room_loader.py handles actual room movement
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

-text_effects.py

    Adds various text effects for atmosphere, like slow typing and dotted text.
    Used to emphasize key moments, build suspense, and enhance the eerie tone.

-ascii_art.py

    Stores ASCII art representations of key rooms, objects, and moments.
    Provides a visual element to complement the text-based descriptions and reinforce the mood.

-debug_mode.py

    Contains special debugging tools and menus.
    Used during development to jump between rooms, trigger certain states, and test features without playing through the entire game.
    Remains accessible via a hidden “debug” input.


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

#ASCII Art in this game was sourced from the following websites:
#- [ASCII Art Archive](https://www.asciiart.eu/)
#- [FSymbols ASCII Art](https://fsymbols.com/text-art/)
#- [ASCII Art UK](https://ascii.co.uk/)
#All rights belong to their respective creators.

#======================================================================

Future Plans:
- Implement sound effects.
- Implement colors
- Smooth out game dialogue and transitions
- Add more dynamic interactions.
- Improve puzzle complexity.

#======================================================================






